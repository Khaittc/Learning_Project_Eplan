# TTC Project — nghiên cứu dữ liệu Eplan

Thư mục này dùng để tra cứu bản vẽ từ **dữ liệu Eplan**, đặc biệt là liên kết thiết bị, dây, part và vị trí trên layout. Các kết luận trong `Content/` dựa trên `TTC_Sample_Project_V1`; không dùng PDF làm chứng cứ.

## Bố cục

| Thư mục | Vai trò |
|---|---|
| `Source_Eplan/` | Project Eplan gốc (`.edb`, `.elk`); giữ nguyên để đối chiếu. |
| `Export_ProjectData/Page/` | Export trang `Project.epj` và AutomationML `Project.aml`. |
| `Export_ProjectData/External_editing/` | Export thuộc tính function, hiện có `Blackbox.edc`. |
| `Export_ProjectData/PLC/` | BOM, PLC và assignment list. |
| `Part/` | Dữ liệu part rời do người dùng export. |
| `Content/` | Quy ước đọc dữ liệu, ca nghiên cứu và yêu cầu export tiếp theo. |
| `Skills/eplan-source-analysis/` | Skill tra cứu Eplan có thể dùng lại. |
| `AGENTS.md` | Điểm vào cho Agent và quy tắc cập nhật kiến thức sau mỗi phát hiện. |

## Bắt đầu

1. Đọc [quy tắc chứng cứ](Content/01_EVIDENCE_AND_SOURCES.md) trước khi kết luận.
2. Dùng [bản đồ trường dữ liệu](Content/02_PROPERTY_MAP.md) để chọn đúng thuộc tính.
3. Xem [ca kiểm chứng CYL1 và 6K1](Content/03_CASE_CYL1_6K1.md), nhất là phần layout.
4. Khi cần xác nhận vùng bao trên Panel Layout, dùng [yêu cầu export](Content/04_LAYOUT_EXPORT.md).
5. Dùng [roadmap](Content/05_ROADMAP.md) để chọn việc còn thiếu và [nhật ký học được](Content/06_LEARNING_LOG.md) để tránh lặp lại các nhầm lẫn đã xử lý.
6. Khi chỉ chia sẻ file export, dùng [bộ dữ liệu export cho Agent](Content/08_EXPORT_ONLY_PACKAGE.md) để biết những trường còn cần bổ sung.
7. Xem [đánh giá bộ export kết hợp](Content/09_REPORT_ONLY_AUDIT.md) để biết ba EDC mới bổ sung gì và những câu hỏi nào còn thiếu trường.
8. Khi cấu hình Eplan External editing, dùng [hướng dẫn scheme và snapshot](Content/10_EXTERNAL_EDITING_SCHEMES.md) và [elements cho scheme Cable](Content/12_CABLE_EXTERNAL_EDITING_ELEMENTS.md).
9. Khi kiểm tra cáp và trạng thái lõi dùng/dư, dùng [báo cáo trích xuất Wiring.epdz](Content/11_WIRING_EPDZ_EXTRACTION.md).
10. Xem [tổng quan cốt lõi dự án](Content/00_PROJECT_OVERVIEW.md) để nắm nhanh toàn bộ cấu trúc.

**Trước khi cấp dữ liệu cho Agent:** xem [trạng thái dữ liệu riêng](Content/07_PRIVACY_BOUNDARY.md). Snapshot source/export hiện tại chưa được khử thông tin riêng.

Skill tại [SKILL.md](Skills/eplan-source-analysis/SKILL.md) hướng dẫn cách áp dụng các tài liệu này cho câu hỏi mới.
