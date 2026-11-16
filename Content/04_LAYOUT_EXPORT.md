# Chuẩn thể hiện và export vị trí trên Panel Layout (I)

## Mục tiêu truy vấn

Trả lời cho từng thiết bị: trang nào, loại đối tượng nào, nằm trong vùng/panel nào, DT và Function text của vùng, tọa độ X/Y và mức chắc chắn của quan hệ bao.

## Cách thể hiện trong Eplan

1. Dùng một đối tượng Eplan có `DT (full)` cho mỗi vị trí thiết bị cần truy vấn; cùng DT ở nhiều vị trí phải có object ID/placement riêng.
2. Dùng `Mounting panel` hoặc `Structure box` có DT và Function text rõ ràng để đặt tên khu vực. Nếu vẽ biên dạng bằng line, line chỉ là đồ họa; cần một đối tượng vùng có danh tính để tra cứu vùng.
3. Đặt thiết bị ở đúng vị trí tương đối với vùng bao. Quy định điểm chuẩn tọa độ của thiết bị và vùng, đơn vị đo và hệ gốc.
4. Nếu có thể, dùng part placement thực sự trên mounting panel: export TTC đã cho thấy `Mounting panel (identifying)` tạo được quan hệ trực tiếp. Với Black box dùng để mô tả thiết bị trên layout, cần export thêm quan hệ parent hoặc tọa độ để xác minh nằm trong vùng.

## File và trường nên export

| Bảng / file | Trường tối thiểu |
|---|---|
| Page | Project, full page name, page type, unit, scale, origin. |
| Placement thiết bị | Object ID/GUID, `DT (full)`, `Function definition`, `Function text`, full page name, X/Y trang, rotation, kích thước hoặc bounding box. |
| Placement vùng | Object ID/GUID, loại `Mounting panel`/`Structure box`/`Black box`, `DT (full)`, `Function text`, full page name, X/Y và biên dạng. |
| Quan hệ | `Mounting panel (identifying)` / ID `20465`, parent ID nếu có, hoặc dữ liệu hình học đủ để thử phép nằm-trong-vùng. |
| Part/connection/PLC | Part number, order number, manufacturer, source, target, connection designation, color/number, cross-section/diameter, PLC address. |

`X coordinate`/`Y coordinate` của placement là ID `19002/19003`. `X coordinate Handle`/`Y coordinate Handle` của part placement là `20208/20209`; không dùng thay cho nhau. `Placement` ID `19007` là trang/cột/hàng, không phải tọa độ. Tham chiếu: [Eplan Properties](https://eplan.help/en-us/Infoportal/Content/Plattform/2025/Content/htm/properties_o_main.htm).

## Kiểm tra sau export

- Với một part placement như `6K1`, xác nhận export có `Mounting panel (identifying) = =ST101+-1U1`.
- Với một Black box như CYL1 `07/1.8`, xác nhận export có X/Y của nó và X/Y/biên của `1U1`, hoặc có parent ID trực tiếp.
- Nếu chỉ có `07/1.8`, ghi vị trí ở mức trang/ô; không kết luận tọa độ hay quan hệ bao trực tiếp.
- Kiểm tra cả hai placement CYL1 `07/1.5` và `07/1.8` để tránh gán part của placement này cho placement kia.

Một bảng CSV/XML riêng, mỗi dòng một placement, là thuận tiện nhất để truy vấn. Nếu giao diện export không đưa ra được parent và X/Y, Eplan API có thuộc tính `Placement.Location` để xuất tọa độ của đối tượng trên trang: [Eplan API Placement](https://www.eplan.help/en-us/Infoportal/Content/api/2023/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html).
