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
6. Khi hỏi **tuyến cáp**, mặc định trả lời `Cable DT | Source Location | Target Location` theo quyết định `EDT-005/F04 APPROVED`; đồng thời giữ nguyên `Cable Source/Target` ở cấp Device (`20376/20377`) cho truy vết và tách riêng Endpoint Device/Pin của từng Core. Đọc [Cable Route addendum](CABLE_ROUTE_ADDENDUM.md); không tách Location từ DT bằng dấu `-` đơn giản.
7. Khi hỏi **nguyên lý hoạt động, tài liệu đính kèm, hoặc trạng thái đèn/báo lỗi của thiết bị**, áp dụng quy trình 4 bước chuẩn hóa (LL-004 APPROVED): Tuyệt đối không suy diễn dựa trên ký tự DT; bóc tách mã part chính xác, quét link tài liệu hãng (`P22149` / `P22280`), đối chiếu sơ đồ chân đấu nối thực tế trong tủ (`Connection.edc`), và tra cứu tài liệu chính hãng để giải thích chi tiết.

## Quy trình tra cứu tài liệu và phân tích nguyên lý thiết bị (LL-004 APPROVED)

Để ngăn chặn việc suy luận chủ quan hoặc tạo sinh nội dung thiếu căn cứ (hallucination) khi người dùng hỏi về tài liệu kỹ thuật (Manual/Datasheet) hoặc nguyên lý vận hành sâu (trạng thái đèn LED, mã lỗi, chu trình reset), Agent phải tuân thủ nghiêm ngặt 4 bước:

1. **Bóc tách mã linh kiện chuẩn (Part Master Data):**
   - Lấy Full DT (`P20006`), Part Number (`P20100` / `P22001` / `P_ARTICLEREF_PARTNO`), Order Number (`P20919` / `P22003`), Nhà sản xuất (`P22007` / `P_ARTICLE_MANUFACTURER`).
   - Kiểm tra `P22009` / `P_ARTICLE_NOTE` để lấy đoạn mô tả tóm tắt kỹ thuật gốc đa ngôn ngữ từ thư viện Eplan.
2. **Tìm kiếm tài liệu & Hyperlink trong file Export:**
   - Quét trường **`P22149`** trong `Project.epj`: Lấy URL tài liệu kỹ thuật trực tuyến / Datasheet chính hãng (ví dụ link Phoenix Contact, Siemens, Omron...).
   - Quét trường **`P22280` / `P22279`** trong `Project_External_Document.aml`: Kiểm tra tài liệu PDF/DOC đính kèm offline nếu có trong dự án.
   - Báo cáo rõ ràng tình trạng tài liệu: có link trực tuyến hay có file offline trong export.
3. **Đối chiếu mạch đấu nối thực tế trong tủ (Circuit & Wiring Context):**
   - Tra cứu [Connection.edc](../../Export_ProjectData_Sanitized/External_editing/Connection.edc) và [Wiring.epdz](../../Export_ProjectData_Sanitized/External_editing/Wiring.epdz):
     - Xác định chân cấp nguồn (ví dụ A1 = 24VDC, A2 = 0VDC).
     - Xác định tín hiệu kích hoạt / vòng lặp cảm biến (ví dụ S11, S12, S22).
     - Xác định chế độ vận hành (ví dụ: chân S34 nối nút ấn Reset thì là *Manual Monitored Start*, nối tắt thì là *Auto Start*).
     - Xác định tiếp điểm ngõ ra (ví dụ: chân 13-14 cấp nguồn an toàn cho khối nào).
4. **Tra cứu tài liệu chuẩn của hãng và kết hợp với mạch thực tế:**
   - Tra cứu đúng tài liệu/datasheet từ mã Part No để lấy thông tin chi tiết: bảng trạng thái LED, mã lỗi, thời gian trễ.
   - **Tách bạch 3 trạng thái khi trình bày:**
     - **Bình thường (Normal/Running):** Mạch an toàn thông, đã kích hoạt/reset, tiếp điểm an toàn đóng, LED nguồn và LED an toàn cùng sáng.
     - **Trạng thái an toàn kích hoạt (Safety Tripped):** Sự cố hở mạch an toàn/nhấn E-stop, tiếp điểm an toàn mở ngắt nguồn máy, LED an toàn tắt.
     - **Trạng thái chờ Reset (Awaiting Reset):** Hết sự cố nhưng chưa nhấn nút Reset, ngõ ra vẫn mở, LED an toàn vẫn tắt.
   - Luôn phân biệt: **Đặc tính chung của thiết bị** vs. **Hành vi thực tế trong mạch của dự án**.

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
- [Quy tắc tuyến cáp theo Location](../../Content/13_CABLE_ROUTE_LOCATION_RULES.md)
- [Hướng dẫn truy vấn tuyến cáp (Addendum)](CABLE_ROUTE_ADDENDUM.md)
- [Tổng hợp cốt lõi dự án](../../Content/00_PROJECT_OVERVIEW.md)
- [Kỹ năng xử lý sự cố Troubleshooting](../eplan-troubleshooting/SKILL.md)

Các đường dẫn trên là tài liệu riêng của project TTC; khi dùng skill cho project khác, thay chứng cứ ca mẫu bằng export của project đó.
