# Ranh giới dữ liệu riêng trong TTC_Project

`PRIVACY_STATUS: UNSANITIZED`

**Trạng thái hiện tại: CHƯA KHỬ THÔNG TIN RIÊNG.** Không cấp `Source_Eplan/` hoặc `Export_ProjectData/` của snapshot này cho Agent chỉ được phép xem dữ liệu kỹ thuật. Tài liệu này chỉ ghi tên trường, ID và vị trí file; không ghi giá trị cá nhân.

## Các trường đã thấy có giá trị trong snapshot hiện tại

| Nguồn | Trường / ID | Lưu ý |
|---|---|---|
| [`ProjectInfo.xml`](../Source_Eplan/TTC_Sample_Project_V1.edb/ProjectInfo.xml) trong `.edb` | `Creator` 10020; `Last editor: Sign-in name` 10022 | Metadata người tạo/sửa project. |
| Cùng file | `Job number` 10013; `Commission` 10014; `Project path (full)` 10045; `Data backup: Backup directory` 10517; `Data backup: Description` 10518 | Có thể để lộ tên khách hàng, tổ chức, máy tính hoặc đường dẫn cá nhân; kiểm tra từng giá trị trong Eplan trước khi chia sẻ. |
| Cùng file | `License number of dongle` 10185 | Mã định danh license; nên coi là thông tin riêng. |
| [`Project.epj`](../Export_ProjectData/Page/Project.epj) | `P10020` ở thuộc tính project; `P11020` và `P11022` trên nhiều trang; `P10185` xuất hiện trong export | Tương ứng Creator project, Creator/Last editor của trang và mã license. Đã đếm 55 lần cho mỗi trường trang `P11020`/`P11022`; không phải chỉ một chỗ ở đầu file. |
| [`Project.aml`](../Export_ProjectData/Page/Project.aml), [`Project_External_Document.aml`](../Export_ProjectData/Page/Project_External_Document.aml), [`PLC_data.aml`](../Export_ProjectData/PLC/PLC_data.aml) | `WriterHeader/WriterName`, `WriterHeader/WriterID` | Header của từng file AML, không phụ thuộc trường Creator trong project. Kiểm tra thêm `WriterProjectTitle` và `WriterProjectID` nếu tên project cũng cần ẩn. |
| [`Device.edc`](../Export_ProjectData/External_editing/Device.edc), [`Connection.edc`](../Export_ProjectData/External_editing/Connection.edc), [`Cable.edc`](../Export_ProjectData/External_editing/Cable.edc) và [`Blackbox.edc`](../Export_ProjectData/External_editing/Blackbox.edc) | Thuộc tính root `SourceProject` | Chứa đường dẫn tuyệt đối tới project gốc; tiết lộ đường dẫn ổ đĩa/thư mục/máy tính của người thiết kế dù các cột report đã lọc. |
| [`Project.epj`](../Export_ProjectData/Page/Project.epj) | Khung tên / Plot frame `P11016` (`Khung_A3_TTC_Akzonobel_2025`, `Khung_A3_QT_Akzonobel_2023`, `FormTtitle_Page_TTC_Akzonobel_2025`) | Lộ trực tiếp tên khách hàng **Akzonobel**, công ty/đơn vị thiết kế **TTC**, **QT** trong tên khung vẽ và biểu mẫu. |
| Cùng file | Thuộc tính trang `P11067` | Chứa tên nguồn gốc dự án cũ: `QT_Akzonobel_IBC_Tank2023`, `LID_DISPENSER_FIL103`. |
| [`Wiring.epdz`](../Export_ProjectData/External_editing/Wiring.epdz) | `manifest.db` & `packages/pages/items/pagesvg/` | Chứa logo đối tác `Icon_Real Group v1 - Copy.png`, trường người tạo `TRANQ` (`P11020`), và Job number `2603-ANBH-FIL103-LID-ELEC`. |
| [`Part/ME-M-0001.xml`](../Part/ME-M-0001.xml) | Thuộc tính `database`, `P_PART_CREATE`, `P_PART_LASTCHANGE`, `P_ARTICLE_EXTERNAL_DOCUMENT` | Lộ đường dẫn database nội bộ `TTC_MACHANICAL.alk`, username `TRANQ`, và đường dẫn tài liệu bản vẽ cơ khí `DWG-ME-0001_RevA.pdf`. |

Dù các nhóm property chuẩn Customer/End customer (`10100`–`10147`) để trống trong project properties, tên khách hàng (**Akzonobel**) và các đơn vị đối tác (**TTC**, **QT**, **Real Group**) vẫn hiện diện rõ ràng qua tên khung bản vẽ (plot frame), tên form, thuộc tính nguồn gốc trang (`P11067`), mã dự án (`P10013`) và file ảnh logo nhúng trong dự án.

## Nhóm trường cần rà soát khi khử dữ liệu

- **Project:** Creator 10020, Last editor 10022, Responsible for project 10025, Company/address 10015–10017, Customer 10100–10117, End customer 10130–10147, Creator contact 10230–10247, Approved/Checked và revision; cả Job number, Commission, Project description, đường dẫn và backup text.
- **Page:** Creator 11020, Last editor 11022, Approved by 11080, Checked by 11082 và các trường revision có tên người. Tên trang, Page description và title block cũng có thể chứa dữ liệu tự do.
- **AutomationML:** `WriterHeader`, tên project và các thuộc tính export được cấu hình thêm. Mỗi lần export mới có thể tái sinh WriterName/WriterID.
- **Nguồn khác:** `.edb` nhị phân, thư mục `DOC/`, external document paths, macro/plot frame, part description, free text và user-defined properties. Không kết luận đã sạch chỉ vì vài property chuẩn đã trống.

Tham chiếu tên/ID property: [Eplan Properties](https://eplan.help/en-us/Infoportal/Content/Plattform/2025/Content/htm/properties_o_main.htm). Eplan mô tả Creator project 10020 là trường được gán tự động; vì vậy xóa trong giao diện có thể không khả dụng. [Eplan Properties 2023](https://eplan.help/en-us/Infoportal/Content/Plattform/2023/Content/htm/properties_o_main.htm).

## Cách tạo ranh giới truy cập thật

1. Giữ **bản gốc Eplan** ở thư mục/kho mà Agent không có quyền đọc. Không xóa trực tiếp các file con `.eod/.eox` hoặc `ProjectInfo.xml` trong `.edb`, vì đó là cấu trúc project.
2. Tạo **bản sao sạch** ngoài bản gốc. Trong Eplan, xóa/đổi các property có thể sửa; sau đó export lại chỉ các trường kỹ thuật cần thiết. Với trường tự động, lọc ở bản export sạch hoặc dùng tài khoản xuất bản danh tính chung nếu cần giữ project gốc dạng native.
3. Rà lại **mọi** export, tài liệu đính kèm và text tự do trước khi đưa vào workspace Agent. Ghi rõ snapshot nào đã sạch. Chỉ sau đó đổi marker đầu tài liệu này thành `PRIVACY_STATUS: SANITIZED` và ghi tên snapshot đã duyệt.
4. Có thể dùng công cụ tự động hóa khử dữ liệu: [`Scripts/sanitize_eplan.py`](../Scripts/sanitize_eplan.py) đi kèm cấu hình tái sử dụng [`Scripts/sanitize_config.json`](../Scripts/sanitize_config.json) để xử lý hàng loạt EPJ, AML, EDC, EPDZ, XML mà không làm ảnh hưởng bản gốc.

`AGENTS.md` và `SKILL.md` là hướng dẫn hành vi, **không phải cơ chế bảo mật**. Nếu file gốc vẫn nằm trong workspace Agent có quyền đọc, Agent vẫn có khả năng truy cập về mặt kỹ thuật. Muốn chặn chắc chắn phải tách file khỏi workspace hoặc dùng quyền truy cập hệ thống.
