# Đánh giá toàn bộ bộ export sau khi bổ sung ba report EDC

**Phạm vi đánh giá là toàn bộ `Export_ProjectData/`**, gồm EPJ, hai AML trang, BOM/XML, PLC, Blackbox.edc và ba report mới `Device.edc`, `Connection.edc`, `Cable.edc`. Ba EDC là phần bổ sung, không phải bộ dữ liệu độc lập. Chỉ xét cấu trúc và thuộc tính kỹ thuật; không đưa metadata cá nhân vào tài liệu.

## Kết luận cho bộ export kết hợp

| Nhóm câu hỏi | Đánh giá | Các nguồn phối hợp |
|---|---|---|
| DT, function, part/model/hãng/order | **Đủ cho các ca đã thử** | Device.edc + AML mới + BOM/XML. `1U1` có part cập nhật; `6K1` và cảm biến có part/hãng. |
| PLC và từng đoạn dây, tên ống lồng, màu/số, tiết diện | **Đủ cho các ca CYL1 đã thử** | Connection.edc + Project.aml + PLC export. 141 connection có Source/Target; 8 chưa có designation trong report. |
| Trang, ô placement và phân biệt hai CYL1 cùng DT | **Đủ** | BOM/XML + EPJ + Blackbox/Device.edc theo object ID/DT. |
| 10 liên kết trực tiếp tới Mounting panel `1U1` | **Đủ** | Project.aml có `Mounting panel (identifying) = =ST101+-1U1`. |
| Part `1U1` và metadata External document | **Đủ** | Project_External_Document.aml; không cần đọc PDF. |
| Tọa độ X/Y và phép chứng minh Black box CYL1 nằm trong vùng bao | **Chưa đủ ở dạng report trực tiếp** | EPJ có dữ liệu đồ họa, nhưng không có property placement `P19002/P19003` được xuất trực tiếp; chưa có parent/bounding box gắn với từng Black box. |
| Dây/lõi nào thuộc cáp nào, hai đầu và chiều dài cáp | **Chưa đủ ở dạng quan hệ trực tiếp đã kiểm chứng** | Cable.edc chưa có trường nối tới connection; cần bổ sung hoặc chứng minh được từ export khác. |

Vì vậy, **không cần `.edb/.elk` để trả lời các câu hỏi TTC đã kiểm chứng**. Muốn hỗ trợ mọi câu hỏi về layout và cáp từ report, cần bổ sung đúng trường/quan hệ trong export. Các file hiện có được xuất ở thời điểm khác nhau; khi có giá trị mâu thuẫn phải báo snapshot, không tự coi mọi file là cùng phiên bản.

## Đóng góp của ba report mới

| Report | Bản ghi | Trường hữu ích | Giới hạn |
|---|---:|---|---|
| [`Device.edc`](../Export_ProjectData/External_editing/Device.edc) | 640 (506 `O17`, 134 `O59`); 78 DT khác nhau | DT full/displayed, function text, part number `[1]`, quantity `[1]`, mã function category/group/definition | Không có tên function definition đọc được, order number, hãng, page/placement, `Mounting panel (identifying)`, X/Y. Chỉ lấy part index `[1]`. |
| [`Connection.edc`](../Export_ProjectData/External_editing/Connection.edc) | 141; 141 cặp Source–Target khác nhau | Connection designation `31011`, Color/Number `31004`, Cross-section/Diameter **kèm đơn vị** `31007`, Source `31019`, Target `31020` | 8 bản ghi trống designation; 4 trống Color/Number và tiết diện. Không có cable DT, page/placement hoặc part/cáp liên quan. |
| [`Cable.edc`](../Export_ProjectData/External_editing/Cable.edc) | 13 placement, 6 DT cáp khác nhau | Cable DT, function text, part `[1]`, type `20040`, số lõi/tiết diện `20071`, điện áp `20044` | Chỉ 6/13 bản ghi có part/type/tiết diện; 2/13 có điện áp. Không có hai đầu cáp, chiều dài, danh sách lõi hoặc liên kết tới 141 connection. |
| [`Cable_v2.edc`](../Export_ProjectData/External_editing/Cable_v2.edc) | 13 placement, 6 DT cáp — snapshot mới hơn | Thêm Source (`20376`), Source with plug (`20383`), Target (`20377`), Target with plug (`20385`), số lõi (`20042`), tiết diện lõi (`20043`), chiều dài với đơn vị (`20041`), Designation in graphic (`20067`), và nhiều trường tổng hợp read-only. | Chiều dài (`20041`, `20257`, `20078`, `20079`) vẫn trống toàn bộ. Không có order number/hãng. Vẫn không liên kết được lõi–connection trực tiếp từ file này. |

`Blackbox.edc` cũ có 639 object ID và **cả 639 đều nằm trong** `Device.edc` mới; nó không phải tập chỉ gồm Black box theo nghĩa function definition. Tên file export không chứng minh phạm vi filter. `Device.edc` có thêm một object ID so với `Blackbox.edc` cũ, vì vậy các report là các snapshot/phạm vi khác nhau; không cộng số bản ghi của chúng thành tổng thiết bị.

## Ca kiểm chứng từ report mới

- `Device.edc` có `1U1` với part `OEM.ME-M-COMPO2`, `6K1` với part `SMC.SY5120-5LZ-01`, và hai bản ghi Black box CYL1 cùng DT nhưng part khác nhau. Không thể xác định bản ghi CYL1 nào là `07/1.8` chỉ từ `Device.edc`, vì thiếu page/placement.
- `Connection.edc` có đoạn `Q24.0/CYL1` từ PLC tới `OUTPUT:1:1`, đoạn `CYL1` từ `OUTPUT:1:2` tới `6K1:BR`, và các đoạn `CYL1-BG1/BG2` hai phía terminal. Các giá trị màu/số và tiết diện được ghi riêng cho từng đoạn.
- `Cable.edc` cho biết cáp và part của một số placement nhưng chưa nối được lõi/connection cụ thể vào cáp theo các cột hiện có.

## Phần cần bổ sung cho mục tiêu rộng hơn

Các trường dưới đây phục vụ mục tiêu tra cứu mọi bản vẽ từ report, không phải điều kiện bắt buộc để trả lời lại các câu hỏi TTC đã kiểm chứng. Xem [gói export](08_EXPORT_ONLY_PACKAGE.md).

## Trường nên bổ sung ở lần export tiếp theo

| Report | Trường cần thêm |
|---|---|
| Device | Function definition dạng text `20026`, order number, manufacturer, toàn bộ part reference/index cần dùng, `Page name (full)` `19023`, `Placement` `19007`, `Mounting panel (identifying)` `20465`, object/placement ID. |
| Connection | Cable DT hoặc ID cáp, trang, connection ID, Cross-section/Diameter thô `31002` nếu cần thống nhất số thập phân; giữ Source, Target và `31007`. Kiểm tra 8 connection chưa có designation. |
| Cable | Source/Target cáp, length, lõi/conductor và các connection tương ứng, part/order/manufacturer, page/placement. |
| Layout report riêng | Page type, full page name, DT, object ID, loại placement (Black box/Part placement/Mounting panel/Structure box), parent/panel ID, X/Y, đơn vị, gốc, rotation và bounding box/biên. |

Một report chỉ đủ khi chạy được câu hỏi mẫu và dẫn về đúng bản ghi nguồn, kể cả trường hợp hai placement cùng DT. Không coi trường trống là lỗi export nếu bản vẽ Eplan thực sự chưa gán giá trị; cần phân biệt hai nguyên nhân khi đánh giá.
