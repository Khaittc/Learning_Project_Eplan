# Hướng dẫn cho Agent làm việc trong TTC_Project

- Kiểm tra [trạng thái dữ liệu riêng](Content/07_PRIVACY_BOUNDARY.md) trước tiên. Khi marker là `PRIVACY_STATUS: UNSANITIZED`, không mở, parse, tìm kiếm hoặc trích xuất `Source_Eplan/` và `Export_ProjectData/` để làm nhiệm vụ thông thường. Chỉ đọc tài liệu trong `Content/` và chờ bản dữ liệu sạch; ngoại lệ chỉ khi người dùng yêu cầu kiểm kê dữ liệu riêng một cách rõ ràng.
- Bắt đầu từ [README.md](README.md) và [skill tra cứu Eplan](Skills/eplan-source-analysis/SKILL.md).
- Khi người dùng đánh giá khả năng đọc **source Eplan**, chỉ dùng `.edb` và các file export làm chứng cứ; không đọc PDF để bổ sung đáp án, trừ khi người dùng đổi phạm vi.
- Trước khi kết luận, phân biệt: thuộc tính/liên kết trực tiếp, suy luận từ bố cục, và thông tin chưa xác nhận. Ghi đúng file export và phiên bản/snapshot đã dùng.
- Nếu phát hiện quy tắc tra cứu có thể dùng lại, cập nhật `Skills/eplan-source-analysis/SKILL.md` hoặc `Content/02_PROPERTY_MAP.md`. Nếu là phát hiện riêng của TTC, cập nhật ca trong `Content/` và [nhật ký học được](Content/06_LEARNING_LOG.md). Nếu thay đổi năng lực còn thiếu, cập nhật [roadmap](Content/05_ROADMAP.md).
- Không sửa hoặc di chuyển source Eplan và file export chỉ để làm đẹp bố cục tài liệu.
- Khi nhận kết quả từ Technical Tester: `PROPOSED/PENDING APPROVAL` chỉ được ghi ở test backlog, không nâng thành quy tắc kỹ thuật trong Skill/Property Map. Chỉ `APPROVED` từ project owner mới được cập nhật thành quy tắc chuẩn. Giữ riêng `test execution status` (`PASS/PARTIAL/FAIL/UNVERIFIED`) và `review status` (`PENDING/APPROVED/REJECTED`), đồng thời ghi commit/snapshot của chứng cứ.
