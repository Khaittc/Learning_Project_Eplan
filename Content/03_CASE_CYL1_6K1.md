# Ca kiểm chứng: CYL1, 6K1 và khu vực Equipment Overview

Project: `TTC_Sample_Project_V1`. Chỉ sử dụng database và file export trong `TTC_Project`.

## Điều khiển và part

- Van điện từ `=ST101+JB01-6K1` điều khiển nhánh CYL1. Part number `SMC.SY5120-5LZ-01`, order number `SY5120-5LZ-01`, hãng `SMC`; Function text `Placer Arm Out`. [Project.aml](../Export_ProjectData/Page/Project.aml)
- Tín hiệu PLC `Q24.0` đi qua terminal `=ST101+JB01-OUTPUT:1` tới cuộn van `6K1:BR`. Kiểm tra từng đoạn dây theo source/target, không lấy tên dây phía PLC gán cho phía van. [Project.aml](../Export_ProjectData/Page/Project.aml), [Project.epj](../Export_ProjectData/Page/Project.epj)

## Tên ống lồng theo `Conductor/Wire`

| Đoạn | Connection designation | Color/Number | Cross-section/Diameter |
|---|---|---|---|
| Từ phía PLC đến `OUTPUT:1:1` | `Q24.0/CYL1` | `22` | `0,5 mm²` |
| Từ `OUTPUT:1:2` đến `6K1:BR` | `CYL1` | `RD` | `0,5 mm²` |
| Tín hiệu vị trí BG1 phía PLC | `CYL1-BG1` | `20` | `0,5 mm²` |
| Tín hiệu vị trí BG2 phía PLC | `CYL1-BG2` | `21` | `0,5 mm²` |

Giá trị của dây phía PLC có trong [Project.aml](../Export_ProjectData/Page/Project.aml#L9710); thuộc tính tiết diện và dây tới van có trong [Project.epj](../Export_ProjectData/Page/Project.epj#L240795) và [Project.epj](../Export_ProjectData/Page/Project.epj#L241054). Phía field của BG1/BG2 có thể có Color/Number `RD`; không gộp hai phía terminal.

## Hai cảm biến liên quan CYL1

| Tên tín hiệu/ống lồng | Thiết bị | Model, hãng | Function text | PLC |
|---|---|---|---|---|
| `CYL1-BG1` | `=ST101+FD-9S2` | `DMSG`, Airtac | `Lid Placer / Arm Bin` | `I4.6` |
| `CYL1-BG2` | `=ST101+FD-9S3` | `DMSG`, Airtac | `Lid Placer / Arm Lids` | `I4.5` |

Hai cảm biến là loại magnetic spring sensor theo part description. `CYL1-BG1` và `CYL1-BG2` cũng xuất hiện trong `Mounting site (describing)` của `9S2` và `9S3`. Chúng là tên tín hiệu/vị trí mô tả, **không phải DT của cảm biến**. Dữ liệu hiện có chưa xác nhận BG1/BG2 ứng với hành trình thu vào hay đẩy ra. [Bill_of_materials.XML](../Export_ProjectData/PLC/Bill_of_materials.XML#L793), [Project.aml](../Export_ProjectData/Page/Project.aml#L4887)

## Trang layout `==FILL-103=ST101#EL&07/1`

| Object | Loại | Placement | Function text | Part |
|---|---|---|---|---|
| `=ST101+-1U1` | Mounting panel | `07/1.6` | `Equipment Overview` | `OEM.ME-M-COMPO2` trong export mới |
| `=ST101+-CYL1` | Black box | `07/1.8` | Trống | Trống |
| `=ST101+-CYL1` | Black box | `07/1.5` | Trống | `MISUMI.ME-P-0001` |

`07/1.8` không phải khóa vị trí duy nhất: nhiều Black box khác cũng có ô placement này. Hai Black box CYL1 cùng DT nhưng khác object ID và khác part. [Bill_of_materials.XML](../Export_ProjectData/PLC/Bill_of_materials.XML#L426), [Bill_of_materials.XML](../Export_ProjectData/PLC/Bill_of_materials.XML#L534), [Blackbox.edc](../Export_ProjectData/External_editing/Blackbox.edc#L3766)

`Project_External_Document.aml` là export cập nhật: part reference của `1U1` là `OEM.ME-M-COMPO2`, order number `Component 2`, hãng `OEM`, số lượng `1`, variant `1`. Part có hai đường dẫn External document, designation `Rev1` và `Rev2`. BOM cũ ghi part của `1U1` trống vì phản ánh snapshot trước khi cập nhật. Chỉ tra metadata và đường dẫn, không đọc nội dung PDF. [Project_External_Document.aml](../Export_ProjectData/Page/Project_External_Document.aml#L18), [part class](../Export_ProjectData/Page/Project_External_Document.aml#L18727)

### Quan hệ trực tiếp với `1U1`

`Project.aml` ghi `Mounting panel (identifying) = =ST101+-1U1` cho **10 đối tượng đặt trên panel**: `=ST101+FD-7S2`, `7S4`, `7S5`, `=ST101+FD-5M1`, và `=ST101+JB01-6K1` đến `6K6`. Đây là liên kết trực tiếp có thể truy vấn. Chú ý `Function definition` của chúng có thể là `Valve, single`, `Switch, NO contact` hoặc `Black box`; loại placement trên trang là *part placement*. [Project.aml](../Export_ProjectData/Page/Project.aml#L10276)

Trang này có **20 Black box** với 10 DT khác nhau: `CYL1–CYL4`, `LS-CAP`, `LS-HOME`, `M1`, `SEN1-I`, `VALVE1`, `VALVE2`; mỗi DT xuất hiện hai lần. Không tìm thấy Structure box trên trang trong export EPJ. Black box CYL1 tại `07/1.8` **không có thuộc tính `Mounting panel (identifying)` trong export hiện tại**. Vì vậy, kết luận CYL1 thuộc vùng `Equipment Overview` là suy luận bố cục cùng trang đã được người dùng xác nhận đúng, nhưng chưa được chứng minh bằng liên kết trực tiếp hoặc phép kiểm tra hình học X/Y. [Project.epj](../Export_ProjectData/Page/Project.epj#L202220)

## Kết luận báo cáo có thể dùng

> CYL1 được thể hiện bằng Black box `=ST101+-CYL1` tại trang Panel Layout `==FILL-103=ST101#EL&07/1`, ô `07/1.8`. Trên trang có Mounting panel `=ST101+-1U1`, Function text `Equipment Overview`; vùng này là kết luận bố cục, chưa có trường liên kết trực tiếp từ Black box CYL1 tới panel trong export hiện tại.
