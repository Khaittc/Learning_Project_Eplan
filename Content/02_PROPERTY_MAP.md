# Bản đồ thuộc tính để tra cứu

Các ID dưới đây được thấy trong export TTC hoặc đã đối chiếu với tên trường Eplan. Cùng tên hiển thị có thể thuộc loại đối tượng khác nhau; luôn kiểm tra ngữ cảnh function, connection hay placement.

| Câu hỏi | Thuộc tính | Cách dùng |
|---|---|---|
| Thiết bị nào? | `DT (full)` / `20006` | Khóa logic của thiết bị; có thể có nhiều placement. |
| Là đối tượng gì? | `Function definition` / `20026`, `P_FUNC_COMPONENTTYPE` | Phân biệt Black box, Mounting panel, Valve, Switch... |
| Chức năng gì? | `Function text` / `20011`, `Function text (automatic)` / `20031` | Nếu rỗng, báo rỗng; không thay bằng tên khu vực. |
| Model/part/hãng? | `Part number` / `20100`, `Order number` / `20919`, `Manufacturer` / `20921` | Gắn vào đúng function hoặc part reference; đừng gán part của placement khác cùng DT. |
| Trang, ô sơ đồ? | `Page name (full)` / `19023`, `Placement` / `19007` | `07/1.8` là vị trí theo trang/ô, không phải X/Y. |
| Vùng lắp xác định trực tiếp? | `Mounting panel (identifying)` / `20465` | Giá trị là DT của panel, ví dụ `=ST101+-1U1`. |
| Nơi lắp mô tả? | `Mounting site (describing)` / `20024` | Text mô tả; không tự động là quan hệ hình học. |
| Tọa độ trên trang? | `X coordinate` / `19002`, `Y coordinate` / `19003` | Cần export trên đúng placement; ghi đơn vị và hệ gốc. |
| Vị trí tay nắm part placement? | `X coordinate Handle` / `20208`, `Y coordinate Handle` / `20209` | Phân biệt với tọa độ trang; cần quy ước điểm chuẩn. |
| Dây đi từ đâu đến đâu? | `Source` / `31019`, `Target` / `31020` | Xác định từng đoạn, nhất là hai phía terminal. |
| Tên ống lồng? | `Connection designation` / `31011` | Quy ước của người dùng: tên ống lồng của function definition `Conductor/Wire`. |
| Màu/số dây? | `Color/Number` / `31004` | `RD` là màu đỏ; `22` là số dây, không phải màu. |
| Tiết diện? | `Cross-section/Diameter` / `31002` | Ví dụ `0.5` nghĩa là `0,5 mm²` khi đơn vị project là mm². |
| PLC I/O? | `PLC address` / `20400` | Đối chiếu với function text và connection. |

## Quy tắc kết hợp

- `Part number`, `Order number` và hãng lấy từ **part reference** của đúng function; không suy từ một Black box khác cùng DT.
- `Connection designation` thuộc **đoạn dây**, không phải thuộc tính cố định của van hoặc xy lanh. Dây qua terminal có thể đổi tên và Color/Number ở hai phía.
- `Mounting panel (identifying)` là liên kết trực tiếp. Việc hai đối tượng nằm trên cùng trang hoặc cùng ô placement không chứng minh quan hệ chứa.
- `Function text` của Black box CYL1 tại `07/1.8` rỗng; `Equipment Overview` là Function text của Mounting panel `1U1`.

## Tuyến cáp và lõi cáp (Cable Route & Core)

| Câu hỏi | Thuộc tính nguồn | Cách dùng |
|---|---|---|
| Tuyến cáp đi từ Location nào đến Location nào? | Cable `Source` / `20376`; `Target` / `20377` + cấu trúc Location của project | Giữ nguyên raw endpoints; chuẩn hóa sang `Source Location → Target Location` cho báo cáo. Location được derived phải xác nhận bằng structure index. |
| Đầu cáp có plug? | `20383` / `20385` | Lưu riêng Source/Target có plug, không thay Location. |
| Có bao nhiêu lõi thiết kế? | `20042` | Đếm một lần mỗi cable DT, không cộng các Cable Definition placements trùng DT. |
| Lõi nối tới đâu? | Connection `31019` / `31020`, association đến Cable | Dữ liệu Device/Pin ở cấp Core/Connection; không dùng thay Route. |

> [!NOTE]
> **EDT-005/F04 APPROVED**. Dùng [13_CABLE_ROUTE_LOCATION_RULES.md](13_CABLE_ROUTE_LOCATION_RULES.md) làm tài liệu chuẩn (normative source). Độ ổn định Object ID (`EDT-009`) vẫn đang chờ bản export mới (`PENDING RE-TEST`).

Nguồn tham chiếu ID thuộc tính Eplan: [Eplan Properties](https://eplan.help/en-us/Infoportal/Content/Plattform/2025/Content/htm/properties_o_main.htm).
