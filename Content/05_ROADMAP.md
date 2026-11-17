# Roadmap: Agent phân tích bản vẽ Eplan từ source

Mục tiêu là trả lời câu hỏi về **mọi loại trang và đối tượng có trong một project Eplan** từ source/export, kèm chứng cứ truy vết được. Đây là lộ trình năng lực, không phải tuyên bố đã hỗ trợ đầy đủ mọi project Eplan.

## Năng lực đã kiểm chứng trên TTC_Sample_Project_V1

| Năng lực | Trạng thái | Chứng cứ mẫu |
|---|---|---|
| Ghép `DT (full)` với function, part, hãng, model | Đã kiểm chứng | `6K1` và `1U1` trong AML; xem [ca TTC](03_CASE_CYL1_6K1.md). |
| Truy nguồn/đích từng đoạn dây, tên ống lồng, màu/số, tiết diện | Đã kiểm chứng với các dây CYL1 | `Project.aml` + `Project.epj`; không gộp qua terminal. |
| Truy PLC I/O tới thiết bị | Đã kiểm chứng với `Q24.0`, `I4.5`, `I4.6` | Function và connection trong AML. |
| Liên kết trực tiếp part placement tới Mounting panel | Đã kiểm chứng | 10 function có `Mounting panel (identifying) = =ST101+-1U1`. |
| Xác nhận Black box nằm trong vùng bằng X/Y và biên | Chưa kiểm chứng | CYL1 trên cùng trang với `1U1`, nhưng export thiếu quan hệ parent/tọa độ đủ dùng. |
| Đọc metadata External document của part | Đã kiểm chứng | `1U1` trong `Project_External_Document.aml`; không đọc PDF. |
| Truy từng đoạn dây bằng `Connection.edc` | Đã kiểm chứng với CYL1 | 141 cặp Source–Target; xem [đánh giá report](09_REPORT_ONLY_AUDIT.md). |
| Nối connection với lõi cáp và hai đầu cáp chỉ từ report | Đã kiểm chứng qua `Wiring.epdz` | `Wiring.epdz` (SQLite `manifest.db`) chứa trực tiếp Cable definition, Conductor placement và 151 merged connections; `Cable_v2.edc` chứa Source/Target cáp. |
| Phân tích nguyên lý thiết bị và tra cứu tài liệu/Hyperlink | Đã kiểm chứng với `15K4` | `Project.epj` (`P22149` datasheet link), `Bill_of_materials.XML` (`P_ARTICLE_NOTE`), đối chiếu `Connection.edc` để xác định trạng thái đèn LED và chế độ Monitored Reset; xem [LL-004](06_LEARNING_LOG.md). |

## Các chặng tiếp theo

### 1. Chuẩn hóa dữ liệu đầu vào

Xác định export tối thiểu theo phiên bản Eplan: trang, function, part reference, connection, PLC, layout placement và external document. Dùng [gói export](08_EXPORT_ONLY_PACKAGE.md) và [kiểm kê report EDC](09_REPORT_ONLY_AUDIT.md); kiểm tra connections có thực sự được xuất. Ghi thời điểm/snapshot từng file để tránh ghép dữ liệu cũ với dữ liệu mới. Trước khi nạp vào Agent, tạo bản export sạch theo [ranh giới dữ liệu riêng](07_PRIVACY_BOUNDARY.md). **Hoàn tất khi** cùng một truy vấn có thể chỉ ra file nào cung cấp từng thuộc tính, phát hiện giá trị mâu thuẫn giữa snapshot và chỉ dùng bản đã được chủ project xác nhận sạch.

Thiết lập các scheme External editing theo [hướng dẫn scheme TTC](10_EXTERNAL_EDITING_SCHEMES.md) và manifest cho mỗi lần xuất bản bộ dữ liệu; không lấy tên file làm bằng chứng về object type/filter.

### 2. Tạo mô hình đối tượng và quan hệ

Dùng khóa `project + page + object ID + DT (full)` cho placement; tách `device`, `function`, `part reference`, `connection`, `page`, `mounting panel/structure box`, `graphic placement`. **Hoàn tất khi** hai Black box CYL1 cùng DT nhưng khác placement không bị nhập làm một và part của `07/1.5` không bị gán sang `07/1.8`.

### 3. Xác định vị trí layout

Thu X/Y, đơn vị, hệ gốc, góc xoay và biên của thiết bị/vùng. Ưu tiên quan hệ `Mounting panel (identifying)`; với Black box thiếu liên kết, tính quan hệ nằm trong vùng từ hình học và ghi phương pháp. Xem [yêu cầu export](04_LAYOUT_EXPORT.md). **Hoàn tất khi** Agent trả lời được trang, loại đối tượng, DT, Function text và vùng chứa CYL1 bằng chứng cứ dữ liệu độc lập với PDF.

### 4. Mở rộng theo loại trang

Lập ca kiểm chứng riêng cho sơ đồ điện nhiều/single-line, PLC, khí nén, Panel Layout và các loại trang xuất hiện trong project mới. Với mỗi loại, ghi thuộc tính và quan hệ đặc thù, các trường chưa export được và trường hợp đối tượng có nhiều representation. **Hoàn tất khi** mỗi loại trang được chọn có ít nhất một câu hỏi kiểm chứng đầy đủ và một câu hỏi thể hiện giới hạn.

### 5. Tự động hóa truy vấn và kiểm chứng

Chỉ tạo parser/script khi cùng thao tác đã lặp lại đủ để cần kết quả nhất quán: đọc XML/AML/EDC, nối ID, kiểm tra snapshot, xuất bảng chứng cứ. Chạy thử trên ca TTC và project khác khi có. **Hoàn tất khi** kết quả máy tạo khớp các ca mẫu, báo thiếu dữ liệu thay vì đoán, và dẫn được tới bản ghi nguồn.

- **EDT-005/F04 — APPROVED (rule):** Cable Route default Source Location → Target Location; raw endpoints preserved. Acceptance test for automatic location resolution and per-core joins remains PARTIAL. See [Cable Route rules](13_CABLE_ROUTE_LOCATION_RULES.md) and [EDT-005](../Tests/EDT-005_CABLE_ROUTE_AND_CORE_VALIDATION.md).
- **EDT-009 — PENDING RE-TEST:** Re-export and compare BOM Object IDs after reopen, edit, copy, and delete/recreate; do not claim stable cross-snapshot object keys before evidence. See [EDT-009](../Tests/EDT-009_OBJECT_ID_STABILITY.md).

## Quy tắc cập nhật roadmap

Sau mỗi ca mới: ghi phát hiện vào [nhật ký](06_LEARNING_LOG.md), cập nhật skill hoặc bản đồ trường nếu quy tắc dùng lại được, rồi đổi trạng thái hạng mục liên quan ở đây. Một xác nhận bằng lời của người dùng giúp đánh giá suy luận nhưng không thay thế chứng cứ liên kết trực tiếp trong export.
