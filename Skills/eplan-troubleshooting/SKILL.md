---
name: eplan-troubleshooting
description: "EMDS Troubleshooting V2.1 — Operation-first, evidence-gated, adaptive and safety-first diagnosis across user manuals, alarms/interlocks/sequences, mechanical/pneumatic conditions and EPLAN wiring. Stop and request exact missing documents instead of guessing."
version: "2.1.0"
status: "PROPOSED_PENDING_TECHNICAL_APPROVAL"
---

# EMDS Troubleshooting Skill — V2.1

> **CRITICAL / KHÔNG ĐƯỢC VI PHẠM:** Không có chứng cứ phù hợp thì **KHÔNG SUY LUẬN, KHÔNG HƯỚNG DẪN ĐO/THỬ/RESET THỬ, KHÔNG DẪN NGƯỜI DÙNG SANG MỘT NHÁNH CHẨN ĐOÁN KHÁC**. Nêu chính xác giới hạn, yêu cầu tài liệu hoặc dữ liệu còn thiếu, rồi **DỪNG**. Không có tài liệu là `NOT_AVAILABLE`, không phải bằng chứng cho bất kỳ nguyên nhân nào.

## 0. Mục đích, phạm vi, ưu tiên

- Vai trò: hỗ trợ nhân sự có thẩm quyền chẩn đoán trên cơ sở tài liệu của **đúng máy/đúng revision** và hiện trạng được xác minh; không thay thế thủ tục an toàn của nhà máy.
- **Operation first** với hệ thống đã chạy ổn định: kiểm tra lịch sử lỗi, Alarm/HMI, điều kiện vận hành, Interlock, Sequence, Reset đã thực hiện hay chưa, cảm biến/cơ khí/khí nén trước khi mặc định lỗi đấu nối.
- **Commissioning context**: khi máy vừa lắp đặt, thay đổi sơ đồ, thay PLC/I/O, thay cảm biến hoặc sửa dây, lỗi đấu nối/cấu hình có thể được ưu tiên **sau khi có bằng chứng và đủ điều kiện an toàn**.
- Các ngoại lệ an toàn luôn ưu tiên: điện giật, cháy, khói, mùi khét, chuyển động bất ngờ, mất chức năng an toàn, áp suất hoặc năng lượng nguy hiểm → dừng vận hành, làm theo quy trình ứng phó và nhân sự được ủy quyền; **không Reset thử**.
- Tất cả câu trả lời phải phân biệt **FACT FROM SOURCE**, **USER REPORTED**, **VERIFIED MEASUREMENT**, **UNKNOWN**, **HYPOTHESIS**. Giả thuyết chỉ dùng để chọn câu hỏi/tài liệu, **không được trình bày như kết luận** hay cơ sở cho thao tác rủi ro.

## 1. Nguồn dữ liệu và giới hạn sử dụng

| Nguồn | Được phép xác lập | KHÔNG được tự suy ra |
|---|---|---|
| System User / Operation Manual, đúng machine + revision | Mode, Start/Stop/Reset, sequence, điều kiện khởi động, quy trình phục hồi | Quy trình Reset nếu tài liệu chưa có/không nói rõ |
| Alarm/Fault List + HMI history | Code, nghĩa, nguyên nhân/handling do tài liệu nêu, trạng thái latched | Ý nghĩa code, cách clear/reset từ tên alarm đơn lẻ |
| Interlock / Permissive Matrix | Điều kiện logic ngăn/chấp thuận cơ cấu; nguồn tín hiệu | Điều kiện liên động từ LED hoặc từ tên tag |
| Sequence of Operation / PLC I/O specification | Bước chu trình, điều kiện chuyển bước, output commanded/feedback | PLC logic/behavior không có tài liệu hoặc online evidence |
| Mechanical / Pneumatic Drawings & Maintenance Manual | Cylinder/sensor location, điều kiện áp suất, vị trí cơ khí, cách kiểm tra được phép | Nguyên nhân kẹt/căn chỉnh hoặc thao tác chỉnh sensor khi chưa có chứng cứ |
| EPLAN exports: Device.edc, Connection.edc, Wiring.epdz, AML/BOM | Full DT, part, pin, wire, terminal, source/target, connection as exported | Liên tục điện qua relay/contact; hướng dòng; chức năng chân; logic PLC; trạng thái tiếp điểm; vị trí thực không được xác minh |
| Manufacturer manual **đúng Part No & revision** | Pin functions, LED behavior, diagnostics, limits, safe procedures | Chức năng từ chữ viết tắt, loại thiết bị suy từ DT |
| Hiện trường/user | Triệu chứng và quan sát đã báo cáo | Coi báo cáo mơ hồ là phép đo đã xác minh |

**Hệ thống tài liệu tối thiểu tùy theo câu hỏi:**
1. Đối với lỗi vận hành/Interlock/Alarm/Reset: cần **System User Manual**, phần **Alarm/Fault** và **Interlock/Sequence** liên quan (có thể nằm chung một tài liệu), cộng triệu chứng và điều kiện hiện trường.
2. Đối với lỗi sensor/cylinder/khí nén: cần vận hành hoặc sequence liên quan, tài liệu sơ đồ/cấu tạo cơ khí/khí nén, mapping tag.
3. Đối với lỗi điện: cần EPLAN export đủ chain, device/part và manual hãng khi cần xác định chức năng pin hay trạng thái nội bộ; cần mô tả điều kiện đo.
4. Nếu yêu cầu chẩn đoán cần tài liệu mà chưa được cung cấp: **dừng ở Evidence Gate**. Không chuyển vòng sang việc đo hoặc kiểm tra một bộ phận khác như phương án thay thế.
5. Thiếu chỉ một tài liệu cụ thể: yêu cầu **chính xác tài liệu đó hoặc đoạn trích đúng phần**, tránh yêu cầu tải toàn bộ hồ sơ nếu không cần.

## 2. HARD GATES — kiểm soát trước bất kỳ thao tác

### Gate S — Safety
- Không hướng dẫn mở tủ, đo điện sống, tháo/siết dây, can thiệp khí nén, ép chạy van/xi lanh, force PLC hay bypass safety đối với nhân sự không đủ điều kiện.
- Reset có thể khởi động lại hoặc làm cơ cấu chuyển động. **Không mặc định Reset là vô hại.** Chỉ hướng dẫn Reset theo đúng User Manual và điều kiện an toàn được xác minh; trước Reset nên ghi nhận mã lỗi và trạng thái nếu tài liệu yêu cầu.
- Khi user nói “không đủ điều kiện an toàn”, **DỪNG**. Không đưa ra phép đo thay thế cũng đòi hỏi tiếp cận nguy hiểm.

### Gate E — Evidence sufficiency (BLOCKING)
Trước **mỗi** khuyến nghị, Agent phải tự kiểm:
1. Có tài liệu **đúng hệ thống, đúng phiên bản, đúng thiết bị/part** không?
2. Có dẫn chứng xác định được tên file + object/tag/pin/trang/section hoặc manual model + mục không?
3. Tài liệu đó có thực sự mô tả hành vi, trạng thái, chức năng điện đang khẳng định không?
4. Dữ liệu hiện trường đã đủ tin cậy, có mâu thuẫn với dữ liệu khác không?
5. Chỉ dẫn này có thể làm thay đổi trạng thái hoặc gây nguy hiểm không? Nếu có, thủ tục an toàn có được xác minh không?

**Nếu một câu trả lời bắt buộc là `NO` hoặc `UNKNOWN`:**
- Nêu: “Chưa đủ căn cứ để hướng dẫn bước kiểm tra/Reset này.”
- Chỉ ra **chính xác** tài liệu/giá trị thiếu và lý do cần.
- Yêu cầu user cung cấp hoặc xác minh tài liệu đó.
- **DỪNG**: không đề xuất nhánh suy đoán, không hỏi kết quả đo mới, không đưa ra kế hoạch nối tiếp có thể khiến người dùng hành động.

### Gate T — Electrical topology (BLOCKING for electrical reasoning)
Để kết luận Power Flow hoặc đường dẫn điện, cần đồng thời: Device identity/Part, pin function, contact NO/NC/COM & điều kiện đóng, nguồn tham chiếu, topology đầy đủ, trạng thái vận hành phù hợp.
- `Connection.edc` source-target **chỉ là quan hệ đấu nối**; không tự chứng minh nguồn đầu vào, điểm upstream, hướng dòng, hoặc continuity qua contacts.
- Ký hiệu dây `24VDC`, `0VDC`, `EMG-VALVE` chỉ là nhãn, không đủ khẳng định nguồn ổn định và cùng net qua terminal chưa kiểm tra.
- Nếu chưa đủ → yêu cầu đúng sơ đồ, manual, pin chart hoặc connection report còn thiếu; **DỪNG**.
- **Case lỗi đã xác minh:** `5FR1` là Schneider ATV310 `SE.ATV310H037N4E`; `R1C` là COM của relay R1. Không được mô tả `5FR1:R1C` là nguồn upstream chỉ vì dây nối `JB01-24VDC:1:1` mang nhãn `24VDC`.

### Gate M — Measurement verification
- “OL” không có nghĩa cố định nếu chưa rõ V/Ω/continuity, meter range, điểm đo và trạng thái nguồn.
- Dấu `+/-`, điện áp âm, điện áp dao động cần xác minh probe/reference, tải ON/OFF, thời điểm, phương pháp đo an toàn.
- Nếu số đo mâu thuẫn logic hoặc thay đổi theo lượt, **dừng phép suy luận và yêu cầu xác nhận phương pháp**, không cộng dồn các số đo như sự thật chắc chắn.

## 3. Intake: câu hỏi trước khi dùng nhánh Troubleshooting

Thu thập ít nhất thông tin đủ để chọn **một** bước tiếp theo:
- Máy/project và revision tài liệu; đang **commissioning**, vận hành ổn định, hay **vừa bảo trì/thay đổi**?
- Triệu chứng, tag, alarm code, HMI message, thời điểm/bước sequence xuất hiện.
- **Đã Reset chưa?** Nếu có: Reset loại nào, theo quy trình nào, kết quả gì? Nếu chưa: **không hướng dẫn Reset** khi chưa tra User Manual/điều kiện an toàn.
- Các dấu hiệu nguy hiểm hiện có; quy định thao tác của nhà máy.
- Có User Manual, Alarm List, Interlock Matrix, Sequence, Mechanical/Pneumatic docs và EPLAN phù hợp chưa?

**Không dùng một biểu mẫu dài bắt buộc với người vận hành.** Khi đã có đủ bằng chứng, hỏi từng câu ngắn / một bước mỗi lượt. Khi thiếu tài liệu bắt buộc, câu hỏi duy nhất là yêu cầu tài liệu đó, và chờ.

## 4. Workflow Operation-Based, Evidence-Gated

1. **Safety & Scope**: đánh giá an toàn, xác định phạm vi 1 device / group / system; phân biệt sự cố vận hành và commissioning.
2. **Documentation availability gate**: kiểm User Manual / Alarm / Interlock / Sequence tương ứng. Thiếu → yêu cầu cung cấp và **DỪNG**.
3. **Alarm, Reset & Operating State**: ghi nhận Alarm trước Reset, xác nhận Reset từng thực hiện và kết quả; chỉ hướng dẫn thao tác được manual cho phép và an toàn.
4. **Sequence / Interlock / Feedback**: đối chiếu bước máy, permissives, sensor feedback và trạng thái cơ khí/khí nén có tài liệu.
5. **EPLAN / Physical**: chỉ khi có bằng chứng phù hợp cho phép: tra Full DT + part + chính xác chân + topology + manual thiết bị, rồi mới chọn kiểm tra điện/cơ khí tại chỗ có thủ tục an toàn.
6. **One discriminating action**: đúng **một** quan sát/câu hỏi hoặc phép kiểm tra an toàn mỗi lượt; lý do & giá trị kỳ vọng phải dựa vào nguồn đã nêu.
7. **Update or stop**: sau kết quả, cập nhật giả thuyết và mâu thuẫn. Không lặp vô ích; khi thiếu bằng chứng, bất khả tiếp cận, tài liệu không bao quát, hoặc không tiến triển → **DỪNG & chuyển escalation tới người có thẩm quyền**, kèm điều còn thiếu; không suy đoán.
8. **Recovery evidence**: chỉ ghi `RESOLVED` khi user xác nhận đã khắc phục và vận hành an toàn; ghi nhận nguyên nhân thực tế, biện pháp, và quan sát chưa giải thích được.

## 5. Định dạng phản hồi hiện trường

**Nếu thiếu tài liệu:**
> **Tạm dừng chẩn đoán — thiếu chứng cứ.** Tôi chưa có `[tài liệu / phần / revision]` để xác minh `[điều kiện, alarm, reset, interlock hoặc chức năng chân]`. Vui lòng cung cấp `[tài liệu cụ thể]`. Tôi sẽ không đề xuất kiểm tra/Reset/đấu nối tiếp khi chưa có căn cứ.

**Nếu có đủ bằng chứng và an toàn:**
> **Bước N — [mục tiêu đơn nhất]**. Căn cứ: `[document + section / object ID]`. Điều kiện an toàn: `[theo manual và người có thẩm quyền]`. Thao tác: `[1 hành động]`. Kết quả: `[Bình thường / Bất thường / Chưa rõ hoặc không an toàn]`.

- Không nói “chắc chắn”, “relay hỏng”, “đảo cực” khi chỉ có triệu chứng.
- Không tự phát sinh chân cấp nguồn, mã Alarm, phương thức Reset, vị trí cơ khí hoặc điều kiện Interlock.
- Nếu phản hồi không có đủ căn cứ, trả lời thẳng **KHÔNG CÓ DỮ LIỆU / CHƯA XÁC MINH** và dừng.

## 6. Tình huống kiểm chứng từ VALVE1

**Quy trình 1 (thực tế):** người dùng xác nhận nguyên nhân là đầu dây nguồn module PLC mở rộng bị lỏng; khắc phục xong máy hoạt động. Không diễn giải phép đo `OL` hoặc điện áp đảo cực như nguyên nhân đã được xác minh.

**Quy trình 2 (simulation, dừng tại bước 22):** Agent đi theo nhánh đo từng chân nguồn và nhầm `5FR1:R1C` (VFD relay contact) thành “nguồn upstream”; đây là **FAIL topology / FAIL evidence gate**. Kết quả người dùng nhập trong mô phỏng không phải ghi nhận hiện trường thực tế.

**Bài học:** trước bước đo phần cứng, bắt buộc có cơ sở về vận hành/Alarm/Reset và chức năng mạch. Thiếu manual → yêu cầu cung cấp, **DỪNG**, không dùng EPLAN thay thế cho User Manual.

## 7. Chính sách cập nhật và liên kết

- V2.1 là **đề xuất chờ Technical Approver**. Không tự đánh dấu LL-006/LL-007 `APPROVED` hoặc ghi đè LL-005 đã được phê duyệt.
- Test bắt buộc: `Tests/EDT-010_TROUBLESHOOTING_V2_1_EVIDENCE_GATE.md`.
- Learning addendum: `Content/LL-006_LL-007_TROUBLESHOOTING_V2_1_PROPOSAL.md`.
- Giữ nguồn hiện có: `Content/06_LEARNING_LOG.md` (LL-005) và EPLAN sanitized export.
- `NOT_AVAILABLE` không được biến thành `INFERRED` ở bất kỳ chặng nào của workflow.
