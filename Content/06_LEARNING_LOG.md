# Nhật ký học được từ truy vấn Eplan

Mỗi mục cần nêu **phát hiện → chứng cứ → cách áp dụng → giới hạn**. Ghi theo ngày cập nhật tài liệu; không dùng ngày này để khẳng định thời điểm tạo dữ liệu Eplan.

## 2026-11-16 — Dây và tên ống lồng

- **Phát hiện:** Theo quy ước của người dùng, tên ống lồng là `Connection designation` của `Conductor/Wire`; màu/số là `Color/Number`; tiết diện là `Cross-section/Diameter`.
- **Chứng cứ:** [Project.epj](../Export_ProjectData/Page/Project.epj#L240795), [Project.epj](../Export_ProjectData/Page/Project.epj#L241054).
- **Áp dụng:** Báo từng đoạn dây theo source/target. CYL1 có `Q24.0/CYL1` phía PLC và `CYL1` phía van 6K1; màu/số lần lượt `22` và `RD`.
- **Giới hạn:** Tên ống lồng là thuộc tính connection, không phải model hoặc DT của thiết bị.

## 2026-11-16 — Cùng DT, nhiều placement

- **Phát hiện:** CYL1 có Black box ở `07/1.5` và `07/1.8`; chỉ bản ghi `07/1.5` có part `MISUMI.ME-P-0001` trong snapshot BOM.
- **Chứng cứ:** [Bill_of_materials.XML](../Export_ProjectData/PLC/Bill_of_materials.XML#L426), [Blackbox.edc](../Export_ProjectData/External_editing/Blackbox.edc#L3766).
- **Áp dụng:** Khóa theo object ID và full page placement, không chỉ DT hoặc ô `07/1.8`.
- **Giới hạn:** Ô placement không phải tọa độ X/Y.

## 2026-11-16 — Vùng Equipment Overview

- **Phát hiện:** `1U1` là Mounting panel, Function text `Equipment Overview`; 10 đối tượng có liên kết trực tiếp `Mounting panel (identifying) = =ST101+-1U1`.
- **Chứng cứ:** [Bill_of_materials.XML](../Export_ProjectData/PLC/Bill_of_materials.XML#L534), [Project.aml](../Export_ProjectData/Page/Project.aml#L10276).
- **Áp dụng:** Dùng property `20465` để trả lời quan hệ panel trực tiếp. Người dùng xác nhận suy luận CYL1 ở vùng Equipment Overview là đúng về bố cục.
- **Giới hạn:** Black box CYL1 tại `07/1.8` chưa có property `20465` trong export; cần X/Y và biên hoặc parent ID để chứng minh bằng dữ liệu.

## 2026-11-16 — Export mới và metadata part

- **Phát hiện:** AML mới thêm part `OEM.ME-M-COMPO2` cho `1U1`, order number `Component 2`, hãng `OEM`, số lượng `1`, variant `1`; part class có hai External document `Rev1`/`Rev2`.
- **Chứng cứ:** [Project_External_Document.aml](../Export_ProjectData/Page/Project_External_Document.aml#L18), [part class](../Export_ProjectData/Page/Project_External_Document.aml#L18727).
- **Áp dụng:** Khi export mới khác BOM cũ, ghi rõ snapshot và ưu tiên bản cập nhật cho thuộc tính được hỏi.
- **Giới hạn:** Đường dẫn External document là metadata; không đọc PDF khi đang đánh giá dữ liệu Eplan.

## 2026-11-16 — Agent dùng export, không cần project native cho câu hỏi đã kiểm chứng

- **Phát hiện:** `.elk` là file project chuẩn để Eplan mở; `.edb` là thư mục dữ liệu liên quan. Agent có thể tra cứu từ export đủ trường mà không cần hai mục này. EPJ mặc định có thể không xuất connections.
- **Chứng cứ:** [Eplan Projects: Principle](https://eplan.help/en-us/Infoportal/Content/Plattform/2024/Content/htm/projects_k_prinzip.htm), [Eplan API export](https://eplan.help/en-us/Infoportal/Content/api/2026/export.html), [ca TTC](03_CASE_CYL1_6K1.md).
- **Áp dụng:** Dùng [gói export](08_EXPORT_ONLY_PACKAGE.md) theo câu hỏi; bật `EXPORTCONNECTIONS=1` khi xuất EPJ bằng API hoặc xuất connection riêng.
- **Giới hạn:** Export thiếu X/Y, biên hoặc parent vẫn chưa đủ xác nhận quan hệ bao của Black box trên layout. Không đưa source native chưa khử thông tin riêng vào workspace Agent.

## 2026-11-16 — Report EDC Device, Connection, Cable

- **Phát hiện:** `Connection.edc` có 141 Source–Target và đủ ba trường dây đã yêu cầu trong các ca CYL1. `Device.edc` có 640 bản ghi nhưng chỉ part index `[1]`; `Cable.edc` có 13 placement của 6 DT cáp, chưa liên kết lõi với connection.
- **Chứng cứ:** [đánh giá report](09_REPORT_ONLY_AUDIT.md) và ba file EDC mới trong `Export_ProjectData/External_editing/`.
- **Áp dụng:** Dùng `Connection.edc` để tra dây; dùng AML/BOM cho hãng/order/trang; yêu cầu report layout và liên kết cáp–lõi khi câu hỏi cần.
- **Giới hạn:** `Blackbox.edc` cũ có 639 object ID đều trùng `Device.edc`; tên file không xác nhận filter. Header EDC còn đường dẫn `SourceProject`, cần khử trước khi cấp cho Agent.

## 2026-11-16 — Đánh giá report phải xét toàn bộ bộ export

- **Phát hiện:** Ba EDC mới bổ sung cho EPJ, AML, BOM và PLC đã có; đánh giá chúng riêng lẻ dẫn tới kết luận thiếu quá mức.
- **Chứng cứ:** [kiểm kê kết hợp](09_REPORT_ONLY_AUDIT.md): 10 liên kết panel trong AML, part `1U1` trong AML mới, 141 connection trong EDC, hai placement CYL1 trong BOM.
- **Áp dụng:** Trả lời mức đủ theo **câu hỏi cụ thể và toàn bộ bộ export**; chỉ nêu thiếu trường khi cả bộ export chưa cung cấp được chứng cứ đó.
- **Giới hạn:** Các export khác snapshot có thể mâu thuẫn; quan hệ Black box–vùng và liên kết cáp–lõi vẫn chưa được chứng minh trực tiếp trong report hiện tại.

## 2026-11-16 — File Wiring.epdz: Cấu trúc 7z, SQLite manifest.db và trạng thái lõi cáp dùng/dư trực tiếp

- **Phát hiện:** File `Wiring.epdz` là kho nén 7-Zip chứa cơ sở dữ liệu SQLite `manifest.db` (16 bảng) cùng các bản vẽ vector SVG. Bảng `property` chứa đầy đủ cả `Cable definition` (loại cáp, part, order, tổng lõi `20042`) và từng `Conductor / wire` (`20026`). Trạng thái lõi cáp được xác định trực tiếp qua trường vị trí placement `19007`: lõi có ô placement là lõi đã dùng trên sơ đồ; lõi có placement trống là lõi dự phòng/dư.
- **Chứng cứ:** [Wiring.epdz](../Export_ProjectData/External_editing/Wiring.epdz) (`manifest.db`), trích xuất ra 6 cáp: `4W1` (6 lõi: 5 dùng, 1 dư GN), `4W2` (10 lõi: 8 dùng, 2 dư 9-10), `5W1` (3 lõi: 3 dùng, 0 dư), `5W2` (10 lõi: 6 dùng, 4 dư 3-8-9-10), `5W3` (30 lõi: 30 dùng, 0 dư), `9W1` (2 lõi: 1 dùng, 1 dư BK).
- **Áp dụng:** Dùng `Wiring.epdz` làm nguồn trực tiếp để kiểm kê số lõi cáp, nhận diện chính xác lõi dự phòng và đối chiếu 151 merged connections mà không cần suy luận từ topology hay phụ thuộc vào các scheme External Editing thiếu trường.
- **Giới hạn:** Cần công cụ giải nén 7z và đọc SQLite để truy xuất dữ liệu từ `.epdz`.

## 2026-11-16 — Cable_v2.edc: Source/Target và số lõi đã có, chiều dài vẫn trống

- **Phát hiện:** `Cable_v2.edc` bổ sung `Source` (`20376`), `Target` (`20377`), Source/Target with plug designation (`20383`/`20385`), số lõi (`20042`), tiết diện lõi (`20043`), chiều dài (`20041`) và `Designation in graphic` (`20067`). Source và Target giờ có giá trị rõ ràng (ví dụ `4W1`: Source `=ST101+JB01-INPUT` → Target `=ST101+CT01-4S1`).
- **Chứng cứ:** [Cable_v2.edc](../Export_ProjectData/External_editing/Cable_v2.edc) — 13 bản ghi, 6 DT cáp, snapshot 2026-11-16 21:42.
- **Áp dụng:** Dùng `Cable_v2.edc` thay thế `Cable.edc` cũ cho câu hỏi về Source/Target và số lõi. Trường `P20376`/`P20377` đã xác nhận được hai đầu cáp trực tiếp từ report. Trường `P20383`/`P20385` cho thêm plug designation khi cần.
- **Giới hạn:** Toàn bộ trường chiều dài (`20041`, `20046`, `20257`, `20078`, `20079`) vẫn rỗng — cần gán giá trị trong Eplan trước. Order number (`20919`) và Manufacturer (`20921`) chưa có trong scheme. Liên kết lõi–connection vẫn cần scheme Connection riêng.

## 2026-11-16 — Scheme External editing theo object type

- **Phát hiện:** Một scheme Eplan External editing gắn với một object type; Device, Connection, Cable nên xuất thành các file riêng rồi xử lý chung như một snapshot.
- **Chứng cứ:** [Eplan Settings: External editing](https://eplan.help/en-us/Infoportal/Content/Plattform/2027/Content/htm/macrosgui_d_pxfeinstellungenexport.htm), [hướng dẫn scheme TTC](10_EXTERNAL_EDITING_SCHEMES.md).
- **Áp dụng:** Nếu muốn một lần vận hành, tự động chạy nhiều scheme liên tiếp; không ghép các XML EDC thô. Bổ sung các trường thiếu vào từng scheme, nhất là page/placement, part metadata, cable association.
- **Giới hạn:** Cột mới không khôi phục thuộc tính chưa được gán trong project. Layout X/Y và vùng bao có thể cần export placement/API riêng.

## 2026-11-16 — Rà soát lộ dữ liệu khách hàng và người dùng trong file export

- **Phát hiện:** Dù các property chuẩn `Customer / End customer` (`10100`–`10147`) để trống, thông tin khách hàng thực tế (**Akzonobel**) và các đơn vị đối tác/nhà thầu (**TTC**, **QT**, **Real Group**) vẫn bị để lộ qua tên khung bản vẽ (`Khung_A3_TTC_Akzonobel_2025`, `Khung_A3_QT_Akzonobel_2023`), form tiêu đề (`FormTtitle_Page_TTC_Akzonobel_2025`), nguồn gốc dự án của trang (`P11067`), mã Job number (`2603-ANBH-FIL103-LID-ELEC`), và ảnh logo nhúng (`Icon_Real Group v1 - Copy.png`). Thông tin cá nhân/người dùng gồm họ tên đầy đủ (`Tran The Tuyen`), username (`TRANQ`, `TRANT`), mã dongle license (`CHAOS363`), cùng đường dẫn ổ đĩa tuyệt đối máy thiết kế trong header file EDC và database part XML.
- **Chứng cứ:** [Project.epj](../Export_ProjectData/Page/Project.epj), [Project.aml](../Export_ProjectData/Page/Project.aml), [EDC files](../Export_ProjectData/External_editing/), [Wiring.epdz](../Export_ProjectData/External_editing/Wiring.epdz), [Part/ME-M-0001.xml](../Part/ME-M-0001.xml).
- **Áp dụng:** Khi quy trình khử dữ liệu riêng (sanitizing) được thực hiện, bắt buộc phải rà soát cả các trường tự do, khung bản vẽ (plot frame), header XML/EDC/AML, đường dẫn tài liệu đính kèm và tài nguyên đa phương tiện (ảnh logo), thay vì chỉ kiểm tra các thuộc tính Eplan mặc định.
- **Giới hạn:** Nếu chỉ xuất file dạng văn bản mà không đổi plot frame / tiêu đề trang trong chính Eplan trước khi export, các siêu dữ liệu nhúng này vẫn sẽ tái sinh.

## 2026-11-17 — EDT-005/F04: Cable Route theo Location (APPROVED)

- **Quyết định đã phê duyệt:** Báo tuyến cáp ở cấp `Source Location → Target Location`. Giữ `P20376/P20377` (Source/Target Device gốc) và các field có plug để truy vết; Core Source/Target Device/Pin là một cấp khác.
- **Chứng cứ:** `Export_ProjectData_Sanitized/External_editing/Cable_v2.edc`, commit `e459be0b6e588bb7795bf76211b84b8dfba97160`, ví dụ `5W1`: raw `=CPT-103+A-5FR1` → `=ST101+FD-5M1`, route `=CPT-103+A` → `=ST101+FD` (derived/approved display).
- **Áp dụng:** Không tách chuỗi bằng dấu `-` đơn giản (ví dụ Location `+DDC-103`); ưu tiên structure identifier/validated location index. Gom cable theo Full DT, giữ nhiều placement riêng.
- **Giới hạn:** Quy tắc trình bày route được APPROVED, nhưng việc tự động lấy Location và nối tới từng Core chưa được xác nhận toàn diện; xem [EDT-005](../Tests/EDT-005_CABLE_ROUTE_AND_CORE_VALIDATION.md).
- **Chưa chốt:** EDT-009 về độ ổn định Object ID; chờ export mới. Các số Used/Spare từ `Wiring.epdz` đang chờ re-test độc lập.

## 2026-11-17 — Phương pháp kiểm chứng tương thích cảm biến (NPN/PNP) và ngõ vào PLC

- **Phát hiện:** Tín hiệu cảm biến mang cùng Function text với địa chỉ PLC (ví dụ `7S5` và `I24.4` đều có text `SEN1-I`) không đồng nghĩa cảm biến đấu thẳng vào PLC. Khả năng đấu trực tiếp phụ thuộc vào hai yếu tố phần cứng: (1) Chuẩn ngõ ra của cảm biến (NPN vs PNP) và (2) Cực tính của chân Common (`1M/2M`) trên module Digital Input của PLC.
- **Chứng cứ:**
  - Cảm biến `=ST101+FD-7S5`: `P_FUNC_TECHNICAL_CHARACTERISTIC = NPN`, `AUTI.BRQM3M-PDTA` ([Bill_of_materials.XML](../Export_ProjectData_Sanitized/PLC/Bill_of_materials.XML)).
  - Chuỗi kết nối ([Connection.edc](../Export_ProjectData_Sanitized/External_editing/Connection.edc)): Pin 2 của `7S5` kéo về chân 6 của rơ-le trung gian `=ST101+JB01-7K1` (Omron `G6B-1114P-FD-US`). Cuộn hút 7K1 cấp `24VDC` ở chân 1. Tiếp điểm NO (chân 4 nối `24VDC`, chân 3 ra dây `SEN1-I`) chuyển tín hiệu sang dạng đóng nguồn dương.
  - Module PLC `=ET101+DDC-103-2K1` (Siemens SM 1223 `6ES7223-1PL32-0XB0`): Chân Common `X10:2/X10:3` (`1M`) đấu cố định vào `0VDC` ([Connection.edc](../Export_ProjectData_Sanitized/External_editing/Connection.edc)), nghĩa là nhóm DI này chỉ nhận mức kích dương `+24VDC` (Sink/PNP).
- **Áp dụng:** Áp dụng phương pháp **"Dò chuỗi 3 điểm"** (Three-Point Verification) khi trả lời câu hỏi tương thích cảm biến - PLC:
  1. Kiểm tra chuẩn ngõ ra cảm biến (`P_FUNC_TECHNICAL_CHARACTERISTIC` và part description: NPN hay PNP).
  2. Lần theo chuỗi dây từ chân output (`Connection.edc` `P31019 -> P31020`): Nếu có rơ-le đệm hoặc bộ chuyển đổi opto, xác định mạch cuộn hút và tiếp điểm.
  3. Kiểm tra điện áp đấu vào chân Common (`1M/2M`) của khối DI tương ứng trên PLC để biết PLC đang nhận Sink (+24V) hay Source (0V).
- **Giới hạn:** Cần có file export Connection đầy đủ cả nguồn cấp cho Common PLC và chân cuộn hút rơ-le; nếu thiếu export connection của trạm trung gian, chỉ có thể kết luận ở mức "chưa xác nhận".

## 2026-11-17 — LL-004: Quy trình 4 bước tra cứu và phân tích nguyên lý thiết bị (APPROVED)

- **Quyết định đã phê duyệt:** Phê duyệt quy trình 4 bước chuẩn hóa khi tra cứu, phân tích nguyên lý hoạt động, trạng thái đèn LED và hành vi mạch của thiết bị, ngăn chặn việc suy luận chủ quan hoặc bịa đặt (hallucination).
- **Bối cảnh thực tế:** Ca phân tích thiết bị `=ET101+DDC-103-15K4` (Rơ-le an toàn Phoenix Contact `PSR-MS35-1NO-24DC-SC` - mã `2904953`) khi người dùng hỏi về bản chất, tài liệu đính kèm (Manual/PDF) trong export, và trạng thái đèn LED ở chế độ Bình thường vs. Chế độ An toàn (Safety Tripped).
- **Bản chất vấn đề & Ranh giới dữ liệu:**
  - File export Eplan (`Bill_of_materials.XML`, `Device.edc`, `Project.epj`, `Project_External_Document.aml`) cung cấp khóa định danh, mã part, sơ đồ chân đấu nối, thông số tóm tắt, và hyperlink tài liệu hãng (`P22149` / `P22280`). File export **không chứa toàn văn User Manual hay bảng mã đèn LED nội bộ**.
  - Không được suy đoán nguyên lý hoạt động chỉ dựa vào ký tự DT (như chữ `K` có thể là contactor, relay trung gian, hoặc safety relay).
  - Không nhầm lẫn giữa **nguyên lý chung của linh kiện rời** với **hành vi thực tế trong mạch của tủ**.
- **Quy tắc 4 bước (Chuẩn hóa):**
  1. **Bước 1 — Định danh chính xác & Bóc tách Part No (Zero Guesswork):** Lấy Full DT (`P20006`), Part Number (`P20100` / `P22001` / `P_ARTICLEREF_PARTNO`), Order Number (`P20919` / `P22003`), Manufacturer (`P20921` / `P22007`).
  2. **Bước 2 — Quét trường tài liệu & Hyperlink trong Eplan:**
     - Quét `P22149` trong [Project.epj](../Export_ProjectData_Sanitized/Page/Project.epj): Tìm link Datasheet trực tuyến chính thức của hãng (`http://www.phoenixcontact.com/pi/products/2904953`).
     - Quét `P22280` / `P22279` trong [Project_External_Document.aml](../Export_ProjectData_Sanitized/Page/Project_External_Document.aml): Kiểm tra tài liệu PDF/DOC đính kèm offline (nếu có).
     - Đọc phần mô tả gốc của hãng trong `P22009` / `P_ARTICLE_NOTE` để nắm thông số cốt lõi.
  3. **Bước 3 — Xác minh cấu hình đấu nối thực tế trong tủ (Project Wiring Context):**
     - Tra cứu [Connection.edc](../Export_ProjectData_Sanitized/External_editing/Connection.edc) / [Wiring.epdz](../Export_ProjectData_Sanitized/External_editing/Wiring.epdz): Xác định nguồn nuôi (`A1/A2`), cấu hình ngõ vào an toàn (`S11/S12/S22`), chế độ kích hoạt/Start (`S34`: Manual Monitored Start hay Auto Start), ngõ ra an toàn (`13-14` cấp cho tải nào).
  4. **Bước 4 — Tra cứu tài liệu kỹ thuật chuẩn của hãng và kết hợp với mạch thực tế:**
     - Sử dụng datasheet/manual chính hãng theo đúng Part No ở Bước 1 & Bước 2 để lấy thông tin chi tiết mà Eplan không lưu (bảng trạng thái LED, mã lỗi, chu trình reset).
     - Phân định rõ ràng: Thông tin nào từ file export Eplan, thông tin nào tra cứu từ tài liệu hãng.
     - Phân tách rõ các trạng thái vận hành: Bình thường (Normal/Running: LED `PWR` và `K1/K2` đều sáng ON) vs. An toàn kích hoạt (Safety Tripped: LED `PWR` sáng, `K1/K2` tắt OFF) vs. Chờ Reset (Awaiting Reset: `PWR` sáng, `K1/K2` tắt chờ nhấn nút S34).


