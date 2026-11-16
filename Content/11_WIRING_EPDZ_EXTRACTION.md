# Báo cáo trích xuất dữ liệu Cáp & Kết nối từ Wiring.epdz

Nguồn trích xuất trực tiếp: `Export_ProjectData/External_editing/Wiring.epdz` (cơ sở dữ liệu SQLite `manifest.db`).

---

## 1. Cấu trúc kỹ thuật file `Wiring.epdz`
- **Định dạng file:** Kho lưu trữ nén chuẩn **7-Zip (7z)** (Header: `37 7A BC AF 27 1C`).
- **Nội dung bên trong:**
  - `manifest.db` (~848 KB): Cơ sở dữ liệu SQLite 3 gồm 16 bảng (`property`, `package`, `function_package`, `mergedconnection_package`, `page_package`, v.v.).
  - `packages/pages/items/pagesvg/`: Bản vẽ vector SVG hiển thị trực quan các trang sơ đồ nguyên lý.

---

## 2. Bảng kiểm kê Cáp & Lõi (Cables & Cores)

| Cáp (DT full) | Chức năng (Function text) | Loại cáp (Type) | Part Number / Order Number | Tổng lõi thiết kế (`20042`) | **Đã đấu nối** (Có placement) | **Dự phòng / Dư** (Chưa gán) |
|---|---|---|---|:---:|:---:|:---:|
| `=ST101+-4W1` | From Control Box To LID-103 | `6x0.5 mm²` | `TT.6x0.5-C` / `6x0.5-C` | **6** | **5** | **1** (`GN`) |
| `=ST101+-4W2` | From LID-103 To JB-FL103 | `10x0.5 mm²` | `TT.10x0.5-N` / `TT.10x0.5` | **10** | **8** | **2** (`9`, `10`) |
| `=ST101+-5W1` | MOTOR | `CVV-3X2.5 mm2 – 0.6/1kV` | `CADIVI.CVV-3x2.5` / `CVV-3x2.5` | **3** | **3** | **0** |
| `=ST101+-5W2` | From CPT-103 to LID-103 | `10x0.5mm²` | `San.10x0.5` / `San.10x0.5` | **10** | **6** | **4** (`3`, `8`, `9`, `10`) |
| `=ST101+-5W3` | From JB-LID to FILL-103 | `30x0.5 mm²` | `TT.30x0.5-N` / `TT.30x0.5` | **30** | **30** | **0** |
| `=ST101+-9W1` | LS-DOOR | `CY-2x0.5mm²` | `LION.CY-2x0.5` / `CY-2x0.5` | **2** | **1** | **1** (`BK`) |

> [!NOTE]
> Khác với việc suy luận mạng nối, cơ chế nhận diện lõi dư trong `Wiring.epdz` dựa trên đối tượng **`Conductor / wire`** (`20026`): Lõi nào có giá trị vị trí trang/ô (`19007`) nghĩa là đã được đặt trên sơ đồ nguyên lý; lõi nào có `19007` trống là lõi dự phòng chưa được sử dụng.

---

## 3. Chi tiết từng Cáp và trạng thái các lõi (Conductor / Wire)

### 3.1. Cáp `=ST101+-4W1` (Tổng: 6 lõi | Đã dùng: 5 | Dư: 1)
* **Vị trí Cable Definition:** `==FILL-103=ST101#EL&11/4.1`
* **Mã Part / Order:** `TT.6x0.5-C` / `6x0.5-C`
* **Danh sách lõi:**
  * `BK` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.5`)
  * `BU` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.3`)
  * `RD` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.5`)
  * `WH` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.4`)
  * `YE` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.2`)
  * `GN` — **DƯ / DỰ PHÒNG** (Chưa gán trên sơ đồ)

---

### 3.2. Cáp `=ST101+-4W2` (Tổng: 10 lõi | Đã dùng: 8 | Dư: 2)
* **Vị trí Cable Definition:** `==FILL-103=ST101#EL&11/4.2`, `==FILL-103=ST101#EL&11/5.3`, `==FILL-103=ST101#EL&11/9.6`
* **Mã Part / Order:** `TT.10x0.5-N` / `TT.10x0.5`
* **Danh sách lõi:**
  * `1` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.5`)
  * `2` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.4`)
  * `3` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/5.3`)
  * `4` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/9.6`)
  * `5` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.6`)
  * `6` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.3`)
  * `7` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.9`)
  * `8` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/4.7`)
  * `9` — **DƯ / DỰ PHÒNG** (Chưa gán trên sơ đồ)
  * `10` — **DƯ / DỰ PHÒNG** (Chưa gán trên sơ đồ)

---

### 3.3. Cáp `=ST101+-5W1` (Tổng: 3 lõi | Đã dùng: 3 | Dư: 0)
* **Vị trí Cable Definition:** `==FILL-103=ST101#EL&11/5.1`
* **Mã Part / Order:** `CADIVI.CVV-3x2.5` / `CVV-3x2.5`
* **Danh sách lõi:**
  * `RD` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/5.1`)
  * `YE` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/5.1`)
  * `BU` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/5.2`)

---

### 3.4. Cáp `=ST101+-5W2` (Tổng: 10 lõi | Đã dùng: 6 | Dư: 4)
* **Vị trí Cable Definition:** `==FILL-103=ST101#EL&11/5.3`
* **Mã Part / Order:** `San.10x0.5` / `San.10x0.5`
* **Danh sách lõi:**
  * `1` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/5.4`)
  * `2` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/5.5`)
  * `4` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/5.7`)
  * `5` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/5.8`)
  * `6` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/5.3`)
  * `7` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/5.4`)
  * `3` — **DƯ / DỰ PHÒNG** (Chưa gán trên sơ đồ)
  * `8` — **DƯ / DỰ PHÒNG** (Chưa gán trên sơ đồ)
  * `9` — **DƯ / DỰ PHÒNG** (Chưa gán trên sơ đồ)
  * `10` — **DƯ / DỰ PHÒNG** (Chưa gán trên sơ đồ)

---

### 3.5. Cáp `=ST101+-5W3` (Tổng: 30 lõi | Đã dùng: 30 | Dư: 0)
* **Vị trí Cable Definition:** `==FILL-103=ST101#EL&11/5.3`, `==FILL-103=ST101#EL&11/6.0`, `==FILL-103=ST101#EL&11/7.0`, `==FILL-103=ST101#EL&11/8.1`, `==FILL-103=ST101#EL&11/9.1`
* **Mã Part / Order:** `TT.30x0.5-N` / `TT.30x0.5`
* **Danh sách lõi:**
  * Cả 30 lõi (từ `1` đến `30`) đều đã được đặt trên các trang sơ đồ `11/5`, `11/6`, `11/7`, `11/8`, `11/9`. Không còn lõi dự phòng.

---

### 3.6. Cáp `=ST101+-9W1` (Tổng: 2 lõi | Đã dùng: 1 | Dư: 1)
* **Vị trí Cable Definition:** `==FILL-103=ST101#EL&11/9.4`
* **Mã Part / Order:** `LION.CY-2x0.5` / `CY-2x0.5`
* **Danh sách lõi:**
  * `RD` — Đã dùng (vị trí: `==FILL-103=ST101#EL&11/9.5` và `11/9.6`)
  * `BK` — **DƯ / DỰ PHÒNG** (Chưa gán trên sơ đồ)

---

## 4. Thống kê Kết nối dây (Merged Connections)

* **Tổng số đoạn kết nối:** 151 đối tượng `mergedconnection`.
* **Cấu trúc trường thuộc tính lưu trữ:**
  * `connectionoid`: Mã định danh đối tượng connection trong Eplan.
  * `31011` (`Connection designation`): Tên ống lồng / nhãn dây.
  * `31004` (`Connection color / number`): Màu hoặc số dây.
  * `31007` (`Cross-section with unit`): Tiết diện dây kèm đơn vị (ví dụ `0,5 mm²`, `2.5 mm²`).
  * `31019` (`Source`) & `31020` (`Target`): Điểm gốc và điểm đích đấu nối chi tiết đến từng chân pin/terminal.
  * `33003` (`Potential`): Điện thế nguồn (`24VDC`, `0VDC`...).
  * `source.20024` & `destination.20024`: Vị trí lắp đặt mô tả tương ứng của 2 đầu kết nối.
