# Bộ dữ liệu chỉ gồm export cho Agent

## Kết luận

Agent **không cần `.edb` và `.elk`** để trả lời các câu hỏi đã kiểm chứng trên TTC nếu các export đã chứa đủ đối tượng và thuộc tính. `.elk` là file đại diện để Eplan mở standard project; `.edb` là thư mục database/master data đi kèm. Chỉ cần cả hai khi một người hoặc công cụ có Eplan phải mở project native để tạo lại export hay kiểm tra thông tin chưa xuất ra. Tham chiếu: [Eplan Projects: Principle](https://eplan.help/en-us/Infoportal/Content/Plattform/2024/Content/htm/projects_k_prinzip.htm).

Không có một file export đơn lẻ nào được xác nhận đáp ứng **mọi** câu hỏi trên mọi loại bản vẽ. Chọn bộ export theo năng lực truy vấn và kiểm tra từng trường quan trọng sau khi xuất.

## Gói tối thiểu theo câu hỏi

| Câu hỏi | File/nhóm dữ liệu Agent cần | Trường quyết định |
|---|---|---|
| Thiết bị, chức năng, model, hãng | AML function/part + BOM/XML | `DT (full)`, `Function definition`, `Function text`, part number, order number, manufacturer. |
| PLC và mạch điều khiển | AML/PLC export + connection export | PLC address, source, target, connection points. |
| Tên ống lồng, màu/số, tiết diện | Connection export đầy đủ hoặc EPJ **có connections** | `Connection designation`, `Color/Number`, `Cross-section/Diameter`, source, target; một dòng cho mỗi đoạn dây. |
| Trang và ô placement | Page export EPJ + BOM/placement table | Full page name, page type, object ID, placement. |
| Quan hệ với Mounting panel | Function/part placement AML | `Mounting panel (identifying)` (`20465`). |
| Black box nằm trong vùng layout | Export placement và hình học/parent | X/Y, đơn vị, gốc tọa độ, biên/rotation, parent ID hoặc panel ID của cả vùng và thiết bị. |
| External document của part | AML part/class export | Part number, đường dẫn/hyperlink, designation; không cần đọc nội dung file nếu chỉ hỏi metadata. |

`Project.aml` của TTC đã cho nhiều function và connection nhưng không bao phủ mọi đoạn dây; `Project.epj` đã giúp tra tiếp các dây CYL1. Nếu xuất EPJ bằng API, Eplan ghi **mặc định không kèm connections** (`EXPORTCONNECTIONS=0`); cần bật `EXPORTCONNECTIONS=1` hoặc xuất connections riêng. Tham chiếu: [Eplan API export](https://eplan.help/en-us/Infoportal/Content/api/2026/export.html).

## Điều kiện để gọi là đủ

1. Cùng một snapshot cho các bảng page, function, part, connection, PLC và layout; có project/version/export time để tránh trộn bản cũ với bản mới.
2. Các bảng có khóa nối: `DT (full)` và object/placement ID, full page name, source/target của connection, part reference ID.
3. Với mỗi câu hỏi mẫu, Agent tìm được giá trị và nguồn; nếu thiếu, báo thiếu trường cụ thể. Thử các ca CYL1 `07/1.5` và `07/1.8`, 6K1, BG1/BG2 và 10 quan hệ trực tiếp với 1U1.
4. Trước khi cấp cho Agent, bản export phải được chủ project khử dữ liệu riêng và đánh dấu sạch theo [ranh giới dữ liệu riêng](07_PRIVACY_BOUNDARY.md). Không đưa `.edb/.elk` gốc vào workspace Agent nếu mục tiêu là chỉ chia sẻ dữ liệu kỹ thuật.

Nếu mục tiêu chỉ là các câu hỏi điện/PLC/part hiện tại, gói export đã khá đủ. Nếu mục tiêu là xác định **mọi vùng bao và tọa độ** trên Panel Layout, cần bổ sung export placement/hình học theo [chuẩn layout](04_LAYOUT_EXPORT.md); cấp `.edb/.elk` cho Agent không tự tạo ra các trường còn thiếu trong export.

Sau khi bổ sung `Device.edc`, `Connection.edc`, `Cable.edc`, đánh giá **toàn bộ** bộ export trong [kiểm kê kết hợp](09_REPORT_ONLY_AUDIT.md); không đánh giá ba EDC riêng lẻ như bộ dữ liệu duy nhất.
