# Tổng hợp nội dung cốt lõi — TTC_Project

> [!IMPORTANT]
> `PRIVACY_STATUS: UNSANITIZED` — Các file gốc trong `Source_Eplan/` và `Export_ProjectData/` **chưa được khử thông tin riêng**. Agent chỉ được đọc tài liệu tổng hợp trong `Content/` cho các tác vụ thông thường.

---

## 1. Mục đích tổng thể

**TTC_Project** là workspace nghiên cứu cách tra cứu bản vẽ từ **dữ liệu Eplan** (project `TTC_Sample_Project_V1`), không dùng PDF làm chứng cứ. Mọi kết luận phải truy vết được tới file export cụ thể và số dòng.

---

## 2. Cấu trúc thư mục

```
TTC_Project/
├── Source_Eplan/          # Project native (.elk + .edb) — KHÔNG cấp cho Agent thông thường
├── Export_ProjectData/
│   ├── Page/              # Project.epj, Project.aml, Project_External_Document.aml
│   ├── External_editing/  # Blackbox.edc, Device.edc, Connection.edc, Cable.edc, Cable_v2.edc, Wiring.epdz
│   └── PLC/               # Bill_of_materials.XML, PLC_data.aml, Assignment_lists.SDF
├── Part/                  # ME-M-0001.xml, ME-M-0001_V2.xml
├── Content/               # Tài liệu quy tắc, ca nghiên cứu, roadmap, báo cáo kiểm tra
└── Skills/eplan-source-analysis/SKILL.md
```

---

## 3. Quy tắc chứng cứ (01 — 03)

### Ba mức chứng cứ

| Mức | Mô tả | Ví dụ |
|---|---|---|
| **Trực tiếp** | Thuộc tính lấy thẳng từ export | `6K1` có `Part number = SMC.SY5120-5LZ-01`; `Mounting panel (identifying) = =ST101+-1U1` |
| **Suy luận có cơ sở** | Từ bố cục/vị trí tương đối | Black box CYL1 cùng trang với panel `1U1`; người dùng xác nhận đúng nhưng chưa có liên kết parent |
| **Chưa xác nhận** | Tọa độ X/Y, hành trình xy lanh, khu vực chỉ vẽ bằng line | Black box CYL1 `07/1.8` chưa có `Mounting panel (identifying)` trong export |

### Khóa tra cứu placement
> **project + full page name + object ID + DT (full)**  
> Không dùng chỉ ô `07/1.8` hoặc tên ngắn.

---

## 4. Bản đồ thuộc tính chính (02)

| Câu hỏi | Thuộc tính Eplan | ID |
|---|---|---|
| Thiết bị nào? | `DT (full)` | `20006` |
| Loại đối tượng? | `Function definition` | `20026` |
| Chức năng? | `Function text` | `20011` |
| Model/part/hãng? | `Part number`, `Order number`, `Manufacturer` | `20100`, `20919`, `20921` |
| Trang và ô sơ đồ? | `Page name (full)`, `Placement` | `19023`, `19007` |
| Lắp trên panel nào? | `Mounting panel (identifying)` | `20465` |
| Tọa độ X/Y trên trang? | `X coordinate`, `Y coordinate` | `19002`, `19003` |
| Dây đi từ–đến? | `Source`, `Target` | `31019`, `31020` |
| Tên ống lồng? | `Connection designation` | `31011` |
| Màu/số dây? | `Color/Number` | `31004` |
| Tiết diện dây? | `Cross-section/Diameter` | `31002` / `31007` |
| PLC I/O? | `PLC address` | `20400` |

---

## 5. Ca kiểm chứng CYL1 & 6K1 (03)

* Van `=ST101+JB01-6K1`: Part `SMC.SY5120-5LZ-01`, SMC, Function text `Placer Arm Out`, tín hiệu PLC `Q24.0` qua terminal `OUTPUT:1`.
* Cảm biến `=ST101+FD-9S2` (`CYL1-BG1`, Airtac DMSG, `I4.6`) và `=ST101+FD-9S3` (`CYL1-BG2`, Airtac DMSG, `I4.5`).
* Trang Panel Layout `==FILL-103=ST101#EL&07/1`: 10 đối tượng có `Mounting panel (identifying) = =ST101+-1U1`. Riêng Black box `=ST101+-CYL1` tại `07/1.8` chưa có liên kết trực tiếp này trong export.

---

## 6. Đánh giá bộ file Export

* **`Project.epj`**: Export trang đồ họa, vị trí placement, có thể thiếu connection nếu không bật cờ API.
* **`Project.aml` / `Project_External_Document.aml`**: Rất giàu thuộc tính; chứa cả liên kết lồng lõi vào cáp và quan hệ Mounting panel.
* **`External_editing/*.edc`**: Bảng dữ liệu theo scheme, thuận tiện cho join và truy vấn tabular.
* **`Wiring.epdz`**: Gói 7z chứa SQLite `manifest.db` và SVG đồ họa. Cung cấp trực tiếp danh sách lõi cáp dùng/dự phòng và 151 merged connections.

---

## 7. Quy tắc cập nhật tri thức cho Agent

Mọi phát hiện mới phải được ghi lại theo chu trình:
1. **[06_LEARNING_LOG.md](06_LEARNING_LOG.md)**: Ghi lại bài học kinh nghiệm, bằng chứng và giới hạn.
2. **[05_ROADMAP.md](05_ROADMAP.md)**: Cập nhật trạng thái năng lực (Đã kiểm chứng / Chưa kiểm chứng).
3. **[Skills/eplan-source-analysis/SKILL.md](../Skills/eplan-source-analysis/SKILL.md)**: Cập nhật quy tắc truy vấn tái sử dụng.
4. **[Skills/eplan-troubleshooting/SKILL.md](../Skills/eplan-troubleshooting/SKILL.md)**: Cập nhật quy tắc chẩn đoán và xử lý sự cố.
5. **`README.md`**: Cập nhật mục lục tài liệu.
