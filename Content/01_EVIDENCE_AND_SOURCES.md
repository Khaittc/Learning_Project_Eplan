# Nguồn dữ liệu và mức chứng cứ

## Mục đích

Trả lời câu hỏi về bản vẽ bằng dữ liệu Eplan. Trong đợt đánh giá này **không đọc PDF**. Không suy ra model, chức năng hay vị trí vật lý chỉ từ hình thức tên DT.

## Các nguồn hiện có

| Nguồn | Nội dung hữu ích | Giới hạn cần nhớ |
|---|---|---|
| [`Source_Eplan/TTC_Sample_Project_V1.edb`](../Source_Eplan/TTC_Sample_Project_V1.edb) và [`TTC_Sample_Project_V1.elk`](../Source_Eplan/TTC_Sample_Project_V1.elk) | Project Eplan native: `.elk` đại diện project, `.edb` chứa database/master data đi kèm. | Không cần cấp cho Agent nếu bản export đã đủ. Nhiều `.eod/.eox` là nhị phân; chuỗi đọc rời rạc chưa đủ để chứng minh quan hệ. |
| [`Export_ProjectData/Page/Project.epj`](../Export_ProjectData/Page/Project.epj) | XML export trang, các đối tượng và thuộc tính/hình học. | Cần nối đúng đối tượng với trang và hình học; số ô placement không phải tọa độ X/Y. |
| [`Export_ProjectData/Page/Project.aml`](../Export_ProjectData/Page/Project.aml) | Function, part, PLC, một số connection và `Mounting panel (identifying)`. | Không bao phủ mọi đoạn dây hoặc mọi liên kết bố cục. |
| [`Export_ProjectData/Page/Project_External_Document.aml`](../Export_ProjectData/Page/Project_External_Document.aml) | Export mới hơn có part của `1U1` và thuộc tính External document của part. | Không dùng giá trị part trống trong BOM/export cũ để phủ định bản cập nhật này; chỉ đọc đường dẫn tài liệu, không đọc PDF. |
| [`Export_ProjectData/External_editing/Blackbox.edc`](../Export_ProjectData/External_editing/Blackbox.edc) | Function được chọn khi export, DT, part và một số text. | Chỉ là tập function theo cấu hình export. |
| [`Device.edc`](../Export_ProjectData/External_editing/Device.edc), [`Connection.edc`](../Export_ProjectData/External_editing/Connection.edc), [`Cable.edc`](../Export_ProjectData/External_editing/Cable.edc) | Report EDC mới về function/part, từng đoạn connection và cáp. | Xem [kiểm kê trường và khoảng trống](09_REPORT_ONLY_AUDIT.md); tên file không chứng minh filter hoặc độ phủ. |
| [`Export_ProjectData/PLC/Bill_of_materials.XML`](../Export_ProjectData/PLC/Bill_of_materials.XML) | DT, component type, part, hãng, trang và placement. | BOM có thể chứa đối tượng không có part; `placement` chỉ là trang/ô. |
| [`Export_ProjectData/PLC/PLC_data.aml`](../Export_ProjectData/PLC/PLC_data.aml), [`Assignment_lists.SDF`](../Export_ProjectData/PLC/Assignment_lists.SDF) | Đối chiếu địa chỉ và tín hiệu PLC. | Không thay thế sơ đồ kết nối hoặc layout. |
| [`Part/`](../Part) | Export part riêng. | Chỉ gán cho thiết bị khi có part reference tương ứng. |

## Mức chứng cứ khi trả lời

| Mức | Ví dụ |
|---|---|
| **Trực tiếp** | Function `6K1` có `Part number = SMC.SY5120-5LZ-01`; function có `Mounting panel (identifying) = =ST101+-1U1`; connection có source, target và `Connection designation`. |
| **Suy luận có cơ sở** | Một Black box và một Mounting panel cùng trang layout; bố cục gợi ý Black box nằm trong panel, nhưng export chưa có liên kết parent hoặc tọa độ kiểm tra hình học. |
| **Chưa xác nhận** | Tọa độ X/Y, trạng thái xy lanh thu vào/đẩy ra, hoặc khu vực con chỉ vẽ bằng line mà không có liên kết đối tượng. |

Một DT có thể xuất hiện nhiều lần. Khóa tra cứu placement nên gồm **project + full page name + object ID + DT (full)**, không chỉ tên ngắn hay ô `07/1.8`.
