# Cách tổ chức export External editing

## Một file hay nhiều file?

Trong Eplan, **mỗi scheme External editing gắn với một object type**. Vì vậy nên giữ `Device.edc`, `Connection.edc`, `Cable.edc` và report `Page` (nếu tạo) thành **các file riêng**. Cùng một lần xuất bản dữ liệu, có thể chạy nhiều scheme liên tiếp bằng thao tác hoặc Eplan action rồi đóng gói các file thành một snapshot. Không ghép thẳng nội dung XML của nhiều `.edc` thành một file EDC, vì mỗi file có `DataConfiguration` và loại bản ghi riêng. Nếu Agent cần một nguồn tra cứu thống nhất, nối các bảng sau export bằng parser và khóa đối tượng.

Eplan ghi rõ object type được chọn khi tạo scheme và không đổi được sau đó: [Settings: External editing](https://eplan.help/en-us/Infoportal/Content/Plattform/2027/Content/htm/macrosgui_d_pxfeinstellungenexport.htm), [External Editing: Functionality](https://eplan.help/en-us/Infoportal/Content/Plattform/2025/Content/htm/pxfinterface_k_arbeitsweise.htm).

## Scheme đề xuất cho bộ TTC

| Scheme/object type | Giữ các trường hiện có | Nên bổ sung nếu Eplan cho chọn trong scheme |
|---|---|---|
| **Device / Function** | Object ID `A1`, `DT (full)`, Function text, part number `[1]`, quantity `[1]` | `Function definition` dạng chữ (`20026`), full page name, vị trí trên trang (`19007`), representation/loại placement, order number, manufacturer, `Mounting panel (identifying)` (`20465`), mounting site, các part reference `[2+]` nếu dùng. |
| **Connection** | Object ID, Source `31019`, Target `31020`, Connection designation `31011`, Color/Number `31004`, tiết diện kèm đơn vị `31007` | DT cáp đầy đủ và `Connection: Association` để nối lõi với cáp; full page name/placement nếu cần truy ngược bản vẽ; tiết diện thô `31002` nếu cần chuẩn hóa số. Kiểm tra các connection có trường đang trống. |
| **Cable** | Cable DT, Function text, part `[1]`, type `20040`, số lõi/tiết diện `20071`, điện áp `20044` | Source/Target cáp, chiều dài, order number/manufacturer, danh sách connection/lõi hoặc ID nối sang connection report, trang/placement. |
| **Page** *(scheme mới)* | — | Full page name, page type, page description và ID trang; loại trang giúp phân biệt sơ đồ điện, PLC, khí nén, Panel Layout. |
| **Layout placement** *(nếu External editing không có đủ thì xuất riêng bằng API)* | — | Object ID, DT, page, loại Black box/Part placement/Mounting panel/Structure box, parent/panel ID, X/Y, biên/kích thước, góc xoay, đơn vị và gốc tọa độ. |

Các trường gián tiếp như `Function definition (string)` và vị trí sơ đồ có thể được xuất để tham khảo nhưng Eplan không nhập ngược một số trường này khi dùng External editing. Điều đó không cản trở mục đích **đọc/tra cứu**. [Eplan: External Editing Functionality](https://eplan.help/en-us/Infoportal/Content/Plattform/2025/Content/htm/pxfinterface_k_arbeitsweise.htm).

## Quy trình xuất một snapshot nhất quán

1. Chốt project và thời điểm export; chạy các scheme riêng trên **toàn project**, cùng ngôn ngữ và cùng phiên bản Eplan.
2. Giữ tên file thể hiện object type; ghi manifest gồm tên file, scheme, object type, số bản ghi, thời điểm export và phiên bản project. Dùng cùng một snapshot cho AML, EPJ, BOM và PLC nếu các file này cũng được cấp cho Agent.
3. Kiểm tra ca mẫu: `1U1`/`6K1` có part, CYL1 có hai placement, `Q24.0/CYL1` và `CYL1` là hai connection khác nhau, 10 liên kết panel `1U1` còn nguyên.
4. Khử metadata riêng trong mọi file trước khi cấp cho Agent, đặc biệt thuộc tính root `SourceProject` của EDC; xem [ranh giới dữ liệu riêng](07_PRIVACY_BOUNDARY.md).

`Blackbox.edc` hiện có 639 object ID và tất cả đều xuất hiện trong `Device.edc` (640 bản ghi). Với cấu hình hiện tại, không cần duy trì thêm một lần export Blackbox nếu Device đã chứa những trường bạn muốn; giữ lại khi cần một scheme lọc hoặc cột khác và xác minh độ phủ sau export. Xem [kiểm kê thực tế](09_REPORT_ONLY_AUDIT.md).

## Kiểm tra trường còn trống

`Connection.edc` hiện có 8/141 connection trống `Connection designation` và 4/141 trống màu/số hoặc tiết diện. Cần kiểm tra bản vẽ Eplan để phân biệt **chưa gán giá trị** với **giá trị không được xuất**; việc thêm cột trong scheme không tự tạo dữ liệu còn thiếu.
