---
name: eplan-source-analysis
description: Tra cứu thiết bị, part, dây, PLC và vị trí layout từ project Eplan cùng các file export EPJ, AML, EDC, XML; phân biệt liên kết trực tiếp với suy luận hình học.
---

# Phân tích bản vẽ từ nguồn Eplan

Trước khi đọc source/export của TTC, kiểm tra [trạng thái dữ liệu riêng](../../Content/07_PRIVACY_BOUNDARY.md). Nếu snapshot chưa được khử và người dùng không yêu cầu kiểm kê dữ liệu riêng, chỉ sử dụng tài liệu đã tổng hợp, không mở source/export. Quy tắc trong skill không tạo quyền chặn đọc ở mức hệ thống.

Ưu tiên dữ liệu project và export. Nếu yêu cầu đánh giá dữ liệu Eplan, không dùng PDF để điền phần còn thiếu. Giữ nguyên giá trị Eplan khi trích xuất và chỉ diễn giải sau khi đã xác định đối tượng, trang và thuộc tính.

## Cách tra cứu

1. Xác định project, bản export và đối tượng bằng `DT (full)`; cùng DT có thể có nhiều placement hoặc representation.
2. Đánh giá toàn bộ export của cùng project như một bộ dữ liệu: `Project.aml` và `Project_External_Document.aml` cho function, part, panel và external document; `Connection.edc` cho từng đoạn dây; `Device.edc`/`Cable.edc` cho function/cáp; `Project.epj` cho đối tượng và hình học trang; BOM/XML cho part và placement; PLC export cho I/O. Khi export thiếu trường, yêu cầu export bổ sung trước khi cần project native. Ghi rõ snapshot nếu file được xuất ở các thời điểm khác nhau.
3. Với dây, chỉ lấy tên ống lồng từ `Connection designation` của `Conductor/Wire`; lấy màu/số từ `Color/Number`, tiết diện từ `Cross-section/Diameter`. Báo từng đoạn dây theo source và target, không gộp qua terminal.
4. Với layout, phân biệt **loại đối tượng của thiết bị** và **vùng bao quanh nó**. Ưu tiên quan hệ trực tiếp như `Mounting panel (identifying)`; cùng trang, cùng ô placement, hoặc cùng tên là dấu hiệu để kiểm tra tiếp, chưa tự chứng minh quan hệ bao.
5. Ghi kết quả cùng đường dẫn nguồn và trạng thái chứng cứ: `trực tiếp`, `suy luận có cơ sở`, hoặc `chưa xác nhận`. Nêu rõ thuộc tính còn thiếu nếu câu hỏi cần tọa độ hay quan hệ hình học.

## Tích lũy kiến thức sau truy vấn

Khi một truy vấn làm rõ thêm cách đọc Eplan, cập nhật tài liệu trong project để Agent sau dùng lại. Đưa quy tắc dùng chung vào skill hoặc bản đồ thuộc tính; đưa giá trị riêng của project vào ca nghiên cứu. Ghi nguồn, snapshot export, kết luận và giới hạn trong nhật ký. Nếu phát hiện thiếu dữ liệu hoặc công cụ, đưa thành hạng mục có điều kiện nghiệm thu trong roadmap. Không nâng suy luận thành liên kết trực tiếp chỉ vì kết quả được người dùng xác nhận đúng.

## Tài liệu trong TTC_Project

- [Nguồn và mức chứng cứ](../../Content/01_EVIDENCE_AND_SOURCES.md)
- [Tên trường Eplan và cách dùng](../../Content/02_PROPERTY_MAP.md)
- [Ví dụ CYL1, 6K1, BG1/BG2 và 1U1](../../Content/03_CASE_CYL1_6K1.md)
- [Chuẩn thể hiện và export layout](../../Content/04_LAYOUT_EXPORT.md)
- [Roadmap năng lực](../../Content/05_ROADMAP.md)
- [Nhật ký học được](../../Content/06_LEARNING_LOG.md)
- [Ranh giới dữ liệu riêng](../../Content/07_PRIVACY_BOUNDARY.md)
- [Bộ dữ liệu chỉ gồm export](../../Content/08_EXPORT_ONLY_PACKAGE.md)
- [Đánh giá toàn bộ export sau khi bổ sung EDC](../../Content/09_REPORT_ONLY_AUDIT.md)
- [Tổ chức scheme External editing](../../Content/10_EXTERNAL_EDITING_SCHEMES.md)
- [Báo cáo trích xuất Wiring.epdz và lõi cáp](../../Content/11_WIRING_EPDZ_EXTRACTION.md)
- [Cấu hình Elements cho Scheme Cable](../../Content/12_CABLE_EXTERNAL_EDITING_ELEMENTS.md)
- [Tổng hợp cốt lõi dự án](../../Content/00_PROJECT_OVERVIEW.md)

Các đường dẫn trên là tài liệu riêng của project TTC; khi dùng skill cho project khác, thay chứng cứ ca mẫu bằng export của project đó.
