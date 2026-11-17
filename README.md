# TTC Project — nghiên cứu dữ liệu Eplan

Thư mục này dùng để tra cứu bản vẽ từ **dữ liệu Eplan**, đặc biệt là liên kết thiết bị, dây, part và vị trí trên layout. Các kết luận trong `Content/` dựa trên `TTC_Sample_Project_V1`; không dùng PDF làm chứng cứ.

## Bố cục thư mục

| Thư mục | Trạng thái Git | Vai trò & Nội dung |
|---|:---:|---|
| [`Content/`](Content/) | Tracked | Quy ước đọc dữ liệu, ca nghiên cứu, phân tích cáp/layout và ranh giới bảo mật. |
| [`Export_ProjectData_Sanitized/`](Export_ProjectData_Sanitized/) | Tracked | **Bộ dữ liệu xuất bản sạch (Đã khử thông tin riêng)**: Dùng để tra cứu, kiểm chứng và nạp cho Agent. |
| ├── `Page/` | | `Project.epj`, `Project.aml`, `Project_External_Document.aml` (Sơ đồ nguyên lý, cấu trúc trang, metadata). |
| ├── `External_editing/` | | `Device.edc`, `Blackbox.edc`, `Connection.edc`, `Cable.edc`, `Cable_v2.edc`, `Wiring.epdz` (Thuộc tính, kết nối dây, cáp và lõi). |
| └── `PLC/` | | `Bill_of_materials.XML`, `PLC_data.aml`, `Assignment_lists.SDF` (BOM, PLC I/O). |
| [`Scripts/`](Scripts/) | Tracked | Bộ công cụ tự động hóa làm sạch dữ liệu export Eplan theo Schema (`sanitize_eplan.py`, `sanitize_config.json`). |
| [`Part/`](Part/) | Tracked | Dữ liệu part rời do người dùng export (`ME-M-0001.xml`, `ME-M-0001_V2.xml`). |
| [`Skills/eplan-source-analysis/`](Skills/eplan-source-analysis/) | Tracked | Skill tra cứu Eplan có thể tái sử dụng cho các dự án khác. |
| [`Skills/eplan-troubleshooting/`](Skills/eplan-troubleshooting/) | Tracked | Skill chẩn đoán và xử lý sự cố (Troubleshooting) kết hợp hiện trạng hiện trường và mạch Eplan. |
| [`Tests/`](Tests/) | Tracked | Hồ sơ kiểm chứng kỹ thuật và kế hoạch kiểm thử (EDT-005, EDT-009). |
| [`AGENTS.md`](AGENTS.md) | Tracked | Điểm vào cho Agent và quy tắc cập nhật kiến thức sau mỗi phát hiện. |
| `Export_ProjectData/` | Ignored | Thư mục export Eplan gốc của dự án (Lưu cục bộ, không commit lên Git vì chứa thông tin riêng). |
| `Source_Eplan/` | Ignored | Project Eplan gốc native (`.edb`, `.elk`) nếu có (Lưu cục bộ, không commit lên Git). |

## Bắt đầu

1. Đọc [quy tắc chứng cứ](Content/01_EVIDENCE_AND_SOURCES.md) trước khi kết luận.
2. Dùng [bản đồ trường dữ liệu](Content/02_PROPERTY_MAP.md) để chọn đúng thuộc tính.
3. Xem [ca kiểm chứng CYL1 và 6K1](Content/03_CASE_CYL1_6K1.md), nhất là phần layout.
4. Khi cần xác nhận vùng bao trên Panel Layout, dùng [yêu cầu export](Content/04_LAYOUT_EXPORT.md).
5. Dùng [roadmap](Content/05_ROADMAP.md) để chọn việc còn thiếu và [nhật ký học được](Content/06_LEARNING_LOG.md) để tránh lặp lại các nhầm lẫn đã xử lý.
6. Xem [ranh giới dữ liệu riêng](Content/07_PRIVACY_BOUNDARY.md) để hiểu cách phân tách dữ liệu sạch và dữ liệu nhạy cảm.
7. Khi chỉ chia sẻ file export, dùng [bộ dữ liệu export cho Agent](Content/08_EXPORT_ONLY_PACKAGE.md) để biết những trường còn cần bổ sung.
8. Xem [đánh giá bộ export kết hợp](Content/09_REPORT_ONLY_AUDIT.md) để biết ba EDC mới bổ sung gì và những câu hỏi nào còn thiếu trường.
9. Khi cấu hình Eplan External editing, dùng [hướng dẫn scheme và snapshot](Content/10_EXTERNAL_EDITING_SCHEMES.md) và [elements cho scheme Cable](Content/12_CABLE_EXTERNAL_EDITING_ELEMENTS.md).
10. Khi kiểm tra cáp và trạng thái lõi dùng/dư, dùng [báo cáo trích xuất Wiring.epdz](Content/11_WIRING_EPDZ_EXTRACTION.md).
11. Khi làm sạch dữ liệu cho dự án mới, sử dụng công cụ tự động tại [`Scripts/sanitize_eplan.py`](Scripts/sanitize_eplan.py).
12. Xem [tổng quan cốt lõi dự án](Content/00_PROJECT_OVERVIEW.md) để nắm nhanh toàn bộ cấu trúc.
13. Khi tra cứu tuyến cáp theo Location, dùng [quy tắc tuyến cáp theo Location (EDT-005)](Content/13_CABLE_ROUTE_LOCATION_RULES.md).
14. Xem hồ sơ kiểm thử cáp và lõi tại [EDT-005](Tests/EDT-005_CABLE_ROUTE_AND_CORE_VALIDATION.md) và kế hoạch kiểm chứng Object ID tại [EDT-009](Tests/EDT-009_OBJECT_ID_STABILITY.md).
15. Xem bộ kiểm thử chẩn đoán sự cố Evidence & Safety Gate tại [EDT-010](Tests/EDT-010_TROUBLESHOOTING_V2_1_EVIDENCE_GATE.md) và đề xuất học tập tại [LL-006 & LL-007](Content/LL-006_LL-007_TROUBLESHOOTING_V2_1_PROPOSAL.md).

Các skill tại [eplan-source-analysis](Skills/eplan-source-analysis/SKILL.md) và [eplan-troubleshooting](Skills/eplan-troubleshooting/SKILL.md) hướng dẫn cách áp dụng các tài liệu này cho câu hỏi tra cứu dữ liệu và xử lý sự cố.
