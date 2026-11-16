# Hướng dẫn Elements cho scheme External Editing — Cable (Eplan)

> [!NOTE]
> Tài liệu này tổng hợp các thuộc tính cần thiết khi người dùng hoặc Agent cấu hình scheme **External Editing** cho đối tượng **Cable / Conduit** trong Eplan Platform.
> Tham chiếu ID thuộc tính Eplan: [Eplan Properties](https://eplan.help/en-us/Infoportal/Content/Plattform/2025/Content/htm/properties_o_main.htm).

---

## 1. So sánh hiện trạng `Cable.edc` và `Cable_v2.edc`

| Thuộc tính | Property ID | Có trong `Cable.edc` (v1)? | Có trong `Cable_v2.edc`? | Ý nghĩa & Đánh giá |
|---|---|:---:|:---:|---|
| Object ID (`A1`) | `60001` | ✅ | ✅ | Khóa nội bộ duy nhất trong Eplan, bắt buộc giữ. |
| Function definition / group | `61383`, `61382` | ✅ | ✅ | Phân loại function. |
| DT (full) / DT (displayed) | `20006`, `20010` | ✅ | ✅ | Mã định danh thiết bị logic của cáp. |
| Function text | `20011` | ✅ | ✅ | Chức năng mô tả cáp. |
| Part number / Quantity | `20100`, `20102` | ✅ | ✅ | Part index 1 của cáp. |
| Cable / Conduit: Type | `20040` | ✅ | ✅ | Kiểu/quy cách cáp (`6x0.5 mm²`, `CVV-3x2.5`...). |
| Voltage | `20044` | ✅ | ✅ | Điện áp danh định. |
| Number of connections | `20042` | ❌ | ✅ | **Tổng số lõi của cáp**. |
| Cross-section / diameter | `20043`, `20070` | ❌ | ✅ | Tiết diện dây lõi (có/không có đơn vị). |
| Cables: Source / Source (plug) | `20376`, `20383` | ❌ | ✅ | Điểm đầu cáp (tự động từ lõi đầu tiên). |
| Cables: Target / Target (plug) | `20377`, `20385` | ❌ | ✅ | Điểm cuối cáp (tự động từ lõi đầu tiên). |
| Designation in graphic | `20067` | ❌ | ✅ | Chuỗi quy chuẩn kỹ thuật hiển thị trên bản vẽ. |
| Cable length | `20041`, `20046` | ❌ | ⚠️ (Trống) | Chiều dài cáp (trống nếu người thiết kế không nhập). |

---

## 2. Danh mục Elements đề xuất cấu hình cho Scheme Cable

Khi tạo hoặc sửa scheme External Editing cho Cable (**Options → Settings → User → Interfaces → External editing**), nên đưa các trường sau vào scheme:

### Nhóm 1: Nhận dạng & Định vị
* `A1` (`60001`): Object ID (Read-only = 1)
* `P20006`: `DT (full)` (Read-only = 1)
* `P20010`: `DT (displayed)`
* `M20011`: `Function text`
* `P19023`: `Page name (full)` — Giúp Agent và kỹ sư biết cáp nằm ở trang nào
* `P19007`: `Placement` — Vị trí ô sơ đồ

### Nhóm 2: Thông số kỹ thuật lõi
* `P20040`: `Cable / Conduit: Type`
* `P20042`: `Cable / Conduit: Number of connections` (Tổng số lõi)
* `P20043`: `Cable / Conduit: Cross-section / diameter` (Tiết diện lõi)
* `P20071`: `Cable / Conduit: Number of connections, cross-section / diameter with unit` (Auto summary)
* `P20044`: `Cables: Voltage`
* `M20067`: `Cable / Conduit: Designation in graphic`

### Nhóm 3: Đầu nối (Source / Target)
* `P20376`: `Cables: Source`
* `P20383`: `Cables: Source (with plug designation)`
* `P20377`: `Cables: Target`
* `P20385`: `Cables: Target (with plug designation)`

### Nhóm 4: Vật tư / Part (Nếu có quản lý BOM)
* `P20100` (Index 1): `Part number`
* `P20919` (Index 1): `Order number`
* `P20921` (Index 1): `Manufacturer`
* `P20102` (Index 1): `Number of units / quantity`

---

## 3. Lưu ý quan trọng về Lõi Cáp (Conductors) & Kết nối

1. **Scheme Cable không xuất danh sách từng lõi:** 
   Trong Eplan, đối tượng Cable chỉ đại diện cho bó cáp tổng thể. Từng lõi cáp là các đối tượng `Conductor / wire`.
2. **Cách tra cứu từng lõi:**
   - Hoặc xuất thêm scheme **Connection** kèm thuộc tính `Connection: Association` (`31142`) để biết kết nối nào thuộc về cáp nào.
   - Hoặc đọc trực tiếp từ **`Project.aml`** (các node `Connection` lồng trong `InternalElement` của cáp) hoặc **`Wiring.epdz`** (các bản ghi `Conductor / wire` mang DT của cáp).
