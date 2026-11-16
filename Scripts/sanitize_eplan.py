#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eplan Export Sanitizer (Pure Field-based / Schema-based Engine)
--------------------------------------------------------------
Làm sạch tự động và triệt để 100% dựa trên SCHEMA và PROPERTY ID của Eplan.
Người dùng KHÔNG CẦN biết hay nhập tên khách hàng, tên kỹ sư hay mã dự án.
"""

import os
import re
import sys
import json
import shutil
import sqlite3
import tempfile
import subprocess
from pathlib import Path

def load_config(config_path: Path) -> dict:
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def sanitize_text(text: str, config: dict) -> str:
    """Khử dữ liệu tự động theo trường (Field-based) và mẫu cấu trúc Eplan."""
    placeholders = config.get("default_placeholders", {})
    fields = config.get("eplan_fields_to_anonymize", {})

    # 1. Khử các trường thuộc tính Project & Page đã chỉ định
    target_props = fields.get("project_properties", []) + fields.get("page_properties", [])
    for prop in target_props:
        rep_val = placeholders.get(prop, placeholders.get("generic_user", "ANONYMOUS"))
        text = re.sub(rf'{prop}="[^"]*"', lambda m, p=prop, v=rep_val: f'{p}="{v}"', text)

    # 2. Khử các dải ID Customer (10100 - 10147) & Contact (10230 - 10247)
    for r in fields.get("customer_id_ranges", []):
        start = r.get("start", 0)
        end = r.get("end", 0)
        rep_cust = placeholders.get("generic_customer", "CUSTOMER_STANDARD")
        # Khớp bất kỳ thuộc tính nào từ P{start} đến P{end}
        text = re.sub(
            r'P(10[12][0-9]{2})="[^"]*"',
            lambda m, c=rep_cust, s=start, e=end: (
                f'P{m.group(1)}="{c}"' if s <= int(m.group(1)) <= e else m.group(0)
            ),
            text
        )

    # 3. Chuẩn hóa tự động khung tên bản vẽ (Plot frame) và Form tiêu đề (Title form)
    # Bất kể khung tên có chứa Akzonobel, Siemens hay tên công ty nào, chuyển hết về Khung tiêu chuẩn
    text = re.sub(r'Khung_[A-Za-z0-9_]+', "Khung_A3_STANDARD", text)
    text = re.sub(r'FormTtitle_Page_[A-Za-z0-9_]+', "FormTitle_STANDARD", text)

    # 4. Chuẩn hóa đường dẫn ổ đĩa tuyệt đối (C:\..., D:\...) và user profile
    text = re.sub(r'[A-Za-z]:\\Users\\[^\\]+\\', r'C:\\Users\\Default\\', text, flags=re.IGNORECASE)
    text = re.sub(r'[A-Za-z]:\\(?:[^\\/:*?"<>|\r\n]+\\)+([a-zA-Z0-9_\-]+\.elk)', r'C:\\EPLAN\\Projects\\Standard_Project.elk', text)
    text = re.sub(r'[A-Za-z]:\\(?:[^\\/:*?"<>|\r\n]+\\)+([a-zA-Z0-9_\-]+\.alk)', r'C:\\EPLAN\\Data\\Parts\\Standard_Parts.alk', text)

    # 5. Nếu người dùng có bổ sung từ khóa tùy chọn (optional)
    blacklist = config.get("optional_keyword_blacklist", [])
    for word in blacklist:
        if word:
            text = re.sub(re.escape(word), "ANONYMOUS", text, flags=re.IGNORECASE)

    return text

def sanitize_epj(src_file: Path, dst_file: Path, config: dict):
    """Xử lý file EPJ lớn theo dạng streaming để tối ưu tốc độ và bộ nhớ."""
    print(f"[*] Đang làm sạch EPJ: {src_file.name} -> {dst_file.name}")
    with open(src_file, "r", encoding="utf-8", errors="ignore") as f_in, \
         open(dst_file, "w", encoding="utf-8") as f_out:
        for line in f_in:
            f_out.write(sanitize_text(line, config))

def sanitize_xml_like(src_file: Path, dst_file: Path, config: dict):
    """Xử lý các file AML, EDC, XML."""
    print(f"[*] Đang làm sạch XML/AML/EDC: {src_file.name}")
    with open(src_file, "r", encoding="utf-8", errors="ignore") as f_in:
        content = f_in.read()

    sanitized = sanitize_text(content, config)

    # Gỡ bỏ thông tin tác giả và dự án trong header AutomationML (AML)
    sanitized = re.sub(r"<WriterName>[^<]*</WriterName>", "<WriterName>EPLAN_USER</WriterName>", sanitized)
    sanitized = re.sub(r"<WriterID>[^<]*</WriterID>", "<WriterID>EPLAN_USER</WriterID>", sanitized)
    sanitized = re.sub(r"<WriterProjectTitle>[^<]*</WriterProjectTitle>", "<WriterProjectTitle>SAMPLE_PROJECT</WriterProjectTitle>", sanitized)
    sanitized = re.sub(r"<WriterProjectID>[^<]*</WriterProjectID>", "<WriterProjectID>SAMPLE_PROJECT</WriterProjectID>", sanitized)
    sanitized = re.sub(r'(<Attribute Name="ProjectManufacturer"[^>]*>\s*<Value>)[^<]*(</Value>)', r'\g<1>EPLAN_ENGINEER\g<2>', sanitized)
    sanitized = re.sub(r'(<Attribute Name="ProjectSign"[^>]*>\s*<Value>)[^<]*(</Value>)', r'\g<1>PROJECT_SIGN\g<2>', sanitized)

    # Gỡ bỏ đường dẫn máy thiết kế trong file EDC External Editing
    sanitized = re.sub(r'SourceProject="[^"]*"', r'SourceProject="C:\\EPLAN\\Projects\\Standard_Project.elk"', sanitized)

    # Gỡ bỏ thông tin máy cá nhân trong file Part XML
    sanitized = re.sub(r'database="[^"]*"', r'database="C:\\EPLAN\\Data\\Parts\\Standard_Parts.alk"', sanitized)
    sanitized = re.sub(r'P_PART_CREATE="[^"]*"', r'P_PART_CREATE="EPLAN_USER / 01.01.2025 00:00:00"', sanitized)
    sanitized = re.sub(r'P_PART_LASTCHANGE="[^"]*"', r'P_PART_LASTCHANGE="EPLAN_USER / 01.01.2025 00:00:00"', sanitized)

    with open(dst_file, "w", encoding="utf-8") as f_out:
        f_out.write(sanitized)

def sanitize_epdz(src_file: Path, dst_file: Path, config: dict):
    """Giải nén .epdz, làm sạch SQLite manifest.db và ảnh logo, sau đó đóng gói lại."""
    print(f"[*] Đang làm sạch gói EPDZ: {src_file.name}")
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp_dir:
        tmp_path = Path(tmp_dir)

        # 1. Giải nén bằng bsdtar
        extract_cmd = ["tar", "-xf", str(src_file), "-C", str(tmp_path)]
        subprocess.run(extract_cmd, check=True)

        # 2. Xử lý cơ sở dữ liệu manifest.db theo Schema ID thuần túy
        db_file = tmp_path / "manifest.db"
        if db_file.exists():
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            try:
                # Update trực tiếp theo propid mà không cần biết nội dung cũ là gì
                cur.execute("UPDATE property SET value = 'EPLAN_ENGINEER' WHERE propid IN (10020, 10022)")
                cur.execute("UPDATE property SET value = 'EPLAN_PAGE_USER' WHERE propid IN (11020, 11022, 11080, 11082)")
                cur.execute("UPDATE property SET value = 'LIC_ANONYMOUS' WHERE propid = 10185")
                cur.execute("UPDATE property SET value = 'JOB_STANDARD_001' WHERE propid = 10013")
                cur.execute("UPDATE property SET value = '' WHERE propid = 10014")
                cur.execute("UPDATE property SET value = 'PROJECT_SAMPLE_ORIGIN' WHERE propid = 11067")
                cur.execute("UPDATE property SET value = 'Khung_A3_STANDARD' WHERE propid = 11016")

                # Xóa sạch các thuộc tính Customer nếu có gán
                cur.execute("UPDATE property SET value = 'CUSTOMER_STANDARD' WHERE propid BETWEEN 10100 AND 10147")
                cur.execute("UPDATE property SET value = 'ANONYMOUS_USER' WHERE propid BETWEEN 10230 AND 10247")

                # Chuẩn hóa tên project trong project_package
                cur.execute("UPDATE project_package SET name = 'Standard_Sample_Project'")

                # Xóa từ khóa trong blacklist (nếu có)
                for kw in config.get("optional_keyword_blacklist", []):
                    if kw:
                        cur.execute(
                            "UPDATE property SET value = replace(value, ?, 'ANONYMOUS') WHERE value LIKE ?",
                            (kw, f"%{kw}%")
                        )

                # 3. Lọc logo hình ảnh trong packages/pages/items/pagesvg/ theo Whitelist
                whitelist = config.get("known_manufacturer_logo_whitelist", [
                    "airtac", "autonics", "omron", "smc", "se_", "schneider", "siemens", "mitsubishi"
                ])
                svg_dir = tmp_path / "packages" / "pages" / "items" / "pagesvg"
                if svg_dir.exists():
                    for img_file in svg_dir.iterdir():
                        if img_file.suffix.lower() in [".png", ".jpg", ".jpeg", ".bmp"]:
                            name_lower = img_file.name.lower()
                            is_trusted_brand = any(brand in name_lower for brand in whitelist)
                            if not is_trusted_brand:
                                print(f"    [-] Tự động gỡ bỏ logo không thuộc hãng thiết bị: {img_file.name}")
                                # Cột tên file trong bảng item là `locator`
                                cur.execute("DELETE FROM item WHERE locator = ?", (img_file.name,))
                                img_file.unlink()

                conn.commit()
            finally:
                cur.close()
                conn.close()

        # 4. Đóng gói lại thành file .epdz định dạng 7zip
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        repack_cmd = ["tar", "-cf", str(dst_file), "--format", "7zip", "-C", str(tmp_path), "."]
        subprocess.run(repack_cmd, check=True)

def sanitize_folder(src_dir: Path, dst_dir: Path, config: dict):
    """Quét toàn bộ thư mục và làm sạch từng file theo cấu trúc trường."""
    print(f"=== Bắt đầu tiến trình làm sạch tự động (Field-based): {src_dir} -> {dst_dir} ===")
    dst_dir.mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(src_dir):
        rel_path = Path(root).relative_to(src_dir)
        cur_dst_dir = dst_dir / rel_path
        cur_dst_dir.mkdir(parents=True, exist_ok=True)

        for filename in files:
            src_file = Path(root) / filename
            dst_file = cur_dst_dir / filename
            ext = src_file.suffix.lower()

            try:
                if ext == ".epj":
                    sanitize_epj(src_file, dst_file, config)
                elif ext in [".aml", ".edc", ".xml"]:
                    sanitize_xml_like(src_file, dst_file, config)
                elif ext == ".epdz":
                    sanitize_epdz(src_file, dst_file, config)
                elif ext in [".sdf", ".txt", ".csv"]:
                    with open(src_file, "r", encoding="utf-8", errors="ignore") as f_in, \
                         open(dst_file, "w", encoding="utf-8") as f_out:
                        f_out.write(sanitize_text(f_in.read(), config))
                else:
                    shutil.copy2(src_file, dst_file)
            except Exception as e:
                print(f"[!] Lỗi khi xử lý {src_file.name}: {e}")

    print("=== Hoàn tất tiến trình làm sạch tự động! ===")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    cfg_file = Path(__file__).resolve().parent / "sanitize_config.json"

    config = load_config(cfg_file)

    source_folder = base_dir / "Export_ProjectData"
    target_folder = base_dir / "Export_ProjectData_Sanitized"

    if len(sys.argv) >= 3:
        source_folder = Path(sys.argv[1])
        target_folder = Path(sys.argv[2])

    sanitize_folder(source_folder, target_folder, config)
