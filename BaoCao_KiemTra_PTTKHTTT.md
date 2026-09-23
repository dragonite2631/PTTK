# BÁO CÁO PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG THÔNG TIN
## ĐỀ TÀI: HỆ THỐNG ĐẶT VÉ THAM GIA SỰ KIỆN TRỰC TUYẾN
**Học viện Công nghệ Bưu chính Viễn thông (PTIT)**  
**Lớp học phần:** N12 | **Giảng viên hướng dẫn:** TS. Nguyễn Đức Hiển (Email: `ndhien@hotmail.com`)  
**Tệp nộp bài Word:** `N12 Nhóm 01.docx` (kèm tệp hoàn chỉnh: `N12 Nhóm 01 - HoanChinh.docx`)

---

## 1. MÃ SỐ NHÓM, TÊN ĐỀ TÀI, HỌ TÊN CÁC THÀNH VIÊN – CHỨC NĂNG

* **Tên đề tài:** Xây dựng Hệ thống đặt vé tham gia sự kiện trực tuyến (*Online Event Ticket Booking System*).
* **Mã số nhóm:** Nhóm 01 (Lớp tín chỉ: N12) *(Sinh viên có thể tùy biến sang mã số nhóm thực tế)*.
* **Mục tiêu hệ thống:** Hệ thống cung cấp giải pháp bán vé sự kiện đa quy mô (Liveshow, Concert, Kịch, Thể thao, Hội thảo), giải quyết triệt để bài toán thắt nút cổ chai (Bottleneck) khi mở bán vé giờ cao điểm thông qua cơ chế **Phòng chờ ảo (Virtual Waiting Queue)**, hiển thị **Sơ đồ khán đài theo thời gian thực (Real-time Seat Map)**, cơ chế **Giữ ghế tạm thời (Countdown Timer)**, thanh toán trực tuyến an toàn và phát hành **Vé điện tử kèm mã QR Code động**.

### Bảng phân công thành viên và chức năng phụ trách

| STT | Họ và tên | Mã sinh viên | Vai trò | Phân hệ (Module) & Chức năng phụ trách chính |
|:---:|:---|:---:|:---:|:---|
| **1** | **Nguyễn Văn A** | B21DCCN001 | Nhóm trưởng | **Module 1: Quản lý tài khoản người dùng**<br>• Đăng ký, đăng nhập tài khoản (phân quyền Role-based)<br>• Đổi mật khẩu, lấy lại mật khẩu qua mã xác thực Email OTP<br>• Chỉnh sửa thông tin hồ sơ cá nhân<br>• Cấu hình tùy chọn nhận thông báo và email |
| **2** | **Trần Thị B** | B21DCCN002 | Thành viên | **Module 2: Tìm kiếm & Xem sự kiện**<br>• Xem danh sách sự kiện nổi bật, thịnh hành (Trending/Hot)<br>• Tìm kiếm và lọc đa tiêu chí (ngày diễn, địa điểm, thể loại, khoảng giá)<br>• Xem trang chi tiết sự kiện, dàn nghệ sĩ/khách mời biểu diễn<br>• Lưu danh sách sự kiện yêu thích (Wishlist) & chia sẻ sự kiện |
| **3** | **Lê Văn C** | B21DCCN003 | Thành viên | **Module 3: Xếp hàng và chọn chỗ**<br>• Xếp hàng đợi ảo (Virtual Queue) khi lưu lượng truy cập lớn<br>• Hiển thị sơ đồ khán đài và trạng thái từng ghế thời gian thực<br>• Chọn vị trí ghế ngồi (VIP, Standard, Fan Zone, vé đứng)<br>• Khóa giữ ghế tạm thời (10–15 phút có bộ đếm ngược) |
| **4** | **Phạm Thị D** | B21DCCN004 | Thành viên | **Module 4: Tính tiền và Xuất vé**<br>• Tạo đơn hàng mua vé, áp dụng mã voucher giảm giá<br>• Thanh toán trực tuyến qua cổng VNPAY, Ví MoMo, Thẻ ATM/Visa<br>• Xử lý giao dịch và sinh mã vé điện tử QR Code động chống giả mạo<br>• Gửi vé qua Email và lưu trữ vào danh mục "Vé của tôi" |
| **5** | **Hoàng Văn E** | B21DCCN005 | Thành viên | **Chức năng 5: Xem thống kê doanh thu sự kiện**<br>• Tiếp nhận yêu cầu tra cứu từ Ban tổ chức<br>• Tính toán các chỉ số KPIs (Gross/Net Revenue, Occupancy Rate)<br>• Phân tích tỷ trọng đóng góp theo từng phân khu khán đài<br>• Kết xuất báo cáo thống kê trực quan (dashboard & file) |

---

## 2. BIỂU ĐỒ USE CASE CHO HỆ THỐNG VÀ CHO CÁC CHỨC NĂNG

### 2.1. Biểu đồ Use Case tổng thể toàn hệ thống

Biểu đồ bao quát toàn bộ 5 phân hệ chức năng tương tác với các tác nhân trong và ngoài hệ thống:
* **Tác nhân chính (Actors):**
  * `Khách hàng (Customer)`: Tìm kiếm sự kiện, xếp hàng, chọn ghế, thanh toán và nhận vé điện tử.
  * `Ban tổ chức (Organizer)`: Thiết kế sơ đồ ghế, đăng sự kiện, cấu hình giá vé, quản lý check-in và xem báo cáo doanh thu.
  * `Quản trị viên (Administrator)`: Quản lý người dùng, duyệt sự kiện và giám sát vận hành hệ thống.
* **Tác nhân hệ thống ngoài (External Systems):**
  * `Cổng thanh toán (Payment Gateway)`: VNPAY / MoMo xử lý giao dịch tài chính trực tuyến.
  * `Dịch vụ Email/SMS (Notification Service)`: Gửi OTP xác thực, thông báo mở bán và tệp vé điện tử QR.

```mermaid
flowchart LR
    Customer((Khách hàng))
    Organizer((Ban tổ chức))
    Admin((Quản trị viên))
    PaymentGW["Cổng thanh toán"]
    MailService["Dịch vụ Email/SMS"]

    subgraph System ["HỆ THỐNG ĐẶT VÉ THAM GIA SỰ KIỆN TRỰC TUYẾN"]
        UC1["1. Đăng ký, Đăng nhập & QL Tài khoản"]
        UC2["2. Tìm kiếm, Lọc & Xem sự kiện"]
        UC3["3. Xếp hàng đợi ảo & Giữ ghế"]
        UC4["4. Thanh toán & Nhận vé QR Code"]
        UC5["5. Thiết kế sơ đồ, Quản lý sự kiện & Thống kê"]
    end

    Customer --> UC1
    Customer --> UC2
    Customer --> UC3
    Customer --> UC4

    Organizer --> UC1
    Organizer --> UC5

    Admin --> UC1
    Admin --> UC5

    UC4 --> PaymentGW
    UC1 --> MailService
    UC4 --> MailService
```

---

### 2.2. Biểu đồ Use Case Phân hệ 1: Quản lý tài khoản người dùng

```mermaid
flowchart LR
    User((Người dùng))
    MailService["Dịch vụ Email/SMS"]

    subgraph Mod1 ["Phân hệ 1: Quản lý tài khoản"]
        UC_Reg["Đăng ký tài khoản"]
        UC_OTP["Gửi mã OTP xác nhận"]
        UC_Login["Đăng nhập"]
        UC_Lock["Khóa tạm thời\n(sai quá 5 lần)"]
        UC_Pwd["Đổi mật khẩu"]
        UC_Forgot["Quên / Lấy lại mật khẩu"]
        UC_ResetMail["Gửi link reset mật khẩu"]
        UC_Profile["Chỉnh sửa thông tin cá nhân"]
        UC_NotiSetting["Cài đặt nhận thông báo"]
    end

    User --> UC_Reg
    User --> UC_Login
    User --> UC_Pwd
    User --> UC_Forgot
    User --> UC_Profile
    User --> UC_NotiSetting

    UC_Reg -.->|<<include>>| UC_OTP
    UC_Lock -.->|<<extend>>| UC_Login
    UC_Forgot -.->|<<include>>| UC_ResetMail

    UC_OTP --> MailService
    UC_ResetMail --> MailService
```

**Đặc tả tóm tắt Use Case Phân hệ 1:**
* **Đăng ký tài khoản:** Khách hàng điền thông tin -> Hệ thống validate dữ liệu -> Gửi mã OTP xác thực email -> Hoàn tất kích hoạt tài khoản.
* **Đăng nhập:** Người dùng nhập username/email và mật khẩu -> Hệ thống băm kiểm tra (BCrypt) -> Cấp JWT Token. Nếu nhập sai 5 lần liên tiếp, kích hoạt Use Case mở rộng khóa tài khoản trong 15 phút.
* **Quên mật khẩu:** Người dùng nhập email -> Nhận mã bảo mật qua email -> Nhập mật khẩu mới.

---

### 2.3. Biểu đồ Use Case Phân hệ 2: Tìm kiếm & Xem sự kiện

```mermaid
flowchart LR
    Customer((Khách hàng))

    subgraph Mod2 ["Phân hệ 2: Tìm kiếm & Xem sự kiện"]
        UC_Hot["Xem sự kiện nổi bật"]
        UC_Search["Tìm kiếm sự kiện theo từ khóa"]
        UC_Filter["Lọc sự kiện (Ngày, Địa điểm,\nThể loại, Khoảng giá)"]
        UC_Detail["Xem chi tiết sự kiện & Nghệ sĩ"]
        UC_Fav["Lưu sự kiện yêu thích"]
        UC_Alert["Nhận thông báo khi mở bán"]
        UC_Share["Chia sẻ thông tin sự kiện"]
    end

    Customer --> UC_Hot
    Customer --> UC_Search
    Customer --> UC_Filter
    Customer --> UC_Detail
    Customer --> UC_Fav
    Customer --> UC_Share

    UC_Alert -.->|<<extend>>| UC_Fav
```

**Đặc tả tóm tắt Use Case Phân hệ 2:**
* **Tìm kiếm & Lọc sự kiện:** Người dùng tìm kiếm toàn văn theo tên nghệ sĩ, sự kiện; áp dụng bộ lọc đa chiều (theo thành phố, thời gian diễn ra cuối tuần này, thể loại nhạc kịch/Concert, giá vé từ thấp đến cao).
* **Xem chi tiết sự kiện:** Hiển thị poster, mô tả kịch bản, lịch diễn các suất (Showtimes), dàn nghệ sĩ khách mời, sơ đồ khán đài và chính sách vé.
* **Lưu sự kiện yêu thích:** Khách hàng đánh dấu lưu sự kiện; hệ thống tự động gửi thông báo đẩy (Push/Email) nhắc nhở trước thời điểm mở bán vé chính thức 30 phút.

---

### 2.4. Biểu đồ Use Case Phân hệ 3: Xếp hàng và chọn chỗ

```mermaid
flowchart LR
    Customer((Khách hàng))
    Timer["Bộ đếm thời gian (Timer)"]

    subgraph Mod3 ["Phân hệ 3: Xếp hàng và chọn chỗ"]
        UC_Queue["Tham gia hàng đợi ảo (Queue)"]
        UC_Status["Theo dõi số thứ tự & Thời gian chờ"]
        UC_Map["Xem sơ đồ sân khấu & Ghế trống"]
        UC_Select["Chọn vị trí ghế ngồi theo khu vực"]
        UC_Hold["Giữ ghế tạm thời (Khóa 10-15 phút)"]
        UC_Release["Giải phóng ghế khi hết hạn"]
        UC_Cancel["Hủy chọn ghế / Thoát hàng đợi"]
    end

    Customer --> UC_Queue
    Customer --> UC_Status
    Customer --> UC_Map
    Customer --> UC_Select
    Customer --> UC_Hold
    Customer --> UC_Cancel

    UC_Release -.->|<<extend>>| UC_Hold
    UC_Hold --> Timer
    Timer --> UC_Release
```

**Đặc tả tóm tắt Use Case Phân hệ 3:**
* **Tham gia hàng đợi ảo (Virtual Waiting Room):** Khi sự kiện có số lượng truy cập đồng thời lớn hơn ngưỡng chịu tải, người dùng được xếp vào hàng đợi FIFO. Màn hình hiển thị số thứ tự và thời gian ước tính. Khi tới lượt, hệ thống cấp `QueueToken` cho phép chuyển vào giao diện chọn ghế.
* **Xem sơ đồ & Giữ ghế tạm thời:** Tải sơ đồ ghế dạng SVG thời gian thực qua WebSocket. Ghế được phân loại theo màu sắc: Trắng (trống), Đỏ (đã bán), Vàng (đang chọn). Khi bấm chọn, ghế chuyển sang trạng thái "Tạm khóa" với đồng hồ đếm ngược 10 phút. Nếu hết 10 phút chưa thanh toán, hệ thống tự động giải phóng ghế trả lại trạng thái trống.

---

### 2.5. Biểu đồ Use Case Phân hệ 4: Tính tiền và Xuất vé

```mermaid
flowchart LR
    Customer((Khách hàng))
    PaymentGW["Cổng thanh toán (VNPAY/MoMo)"]
    Mailer["Dịch vụ Email"]

    subgraph Mod4 ["Phân hệ 4: Tính tiền và Xuất vé"]
        UC_Order["Tạo hóa đơn mua vé"]
        UC_Coupon["Nhập mã giảm giá (Voucher)"]
        UC_CheckCoupon["Kiểm tra hợp lệ mã voucher"]
        UC_Method["Chọn phương thức thanh toán"]
        UC_Pay["Thực hiện thanh toán trực tuyến"]
        UC_Verify["Xác thực OTP & Kết quả GD"]
        UC_Issue["Xuất vé điện tử mã QR Code động"]
        UC_MyTickets["Lưu trữ vào mục 'Vé của tôi'"]
    end

    Customer --> UC_Order
    Customer --> UC_Coupon
    Customer --> UC_Method
    Customer --> UC_Pay
    Customer --> UC_Issue
    Customer --> UC_MyTickets

    UC_Coupon -.->|<<include>>| UC_CheckCoupon
    UC_Pay -.->|<<include>>| UC_Verify

    UC_Verify --> PaymentGW
    UC_Issue --> Mailer
```

**Đặc tả tóm tắt Use Case Phân hệ 4:**
* **Tạo đơn hàng & Nhập voucher:** Hệ thống tổng hợp các ghế đang giữ, tính tạm tính. Người dùng nhập mã giảm giá -> Hệ thống kiểm tra điều kiện (hạn dùng, đơn tối thiểu, số lượng còn) -> Áp dụng giảm giá và tính tổng tiền thanh toán cuối.
* **Thanh toán trực tuyến:** Người dùng chọn VNPAY-QR, Thẻ ATM/Visa hoặc Ví MoMo -> Chuyển hướng sang cổng thanh toán -> Xác thực OTP ngân hàng -> Webhook trả về kết quả thành công -> Cập nhật trạng thái đơn hàng thành `PAID`.
* **Xuất vé điện tử:** Hệ thống sinh mã vé và chuỗi mã hóa QR Code độc nhất chứa chữ ký điện tử -> Gửi vé định dạng PDF/QR qua Email và lưu trữ vào danh mục "Vé của tôi".

---

### 2.6. Biểu đồ Use Case Chức năng 5: Xem thống kê doanh thu sự kiện

```mermaid
flowchart TB
    Organizer((Ban tổ chức))
    Admin((Quản trị viên))

    subgraph Subsystem ["CHỨC NĂNG: XEM THỐNG KÊ DOANH THU SỰ KIỆN"]
        UC_Main(["Xem thống kê doanh thu sự kiện"])
        UC_Select(["Chọn sự kiện cần thống kê"])
        UC_Compute(["Tổng hợp & Tính toán KPIs\n(Doanh thu & Tỷ lệ lấp đầy)"])
        UC_Filter(["Lọc theo suất diễn & khoảng ngày"])
        UC_ZoneDetail(["Xem chi tiết phân bổ\ndoanh thu theo phân khu"])
        UC_Export(["Xuất báo cáo doanh thu\n(Excel / PDF)"])
    end

    Organizer --> UC_Main
    Admin --> UC_Main

    UC_Main -.->|<<include>>| UC_Select
    UC_Main -.->|<<include>>| UC_Compute

    UC_Filter -.->|<<extend>>| UC_Main
    UC_ZoneDetail -.->|<<extend>>| UC_Main
    UC_Export -.->|<<extend>>| UC_Main
```

* **Ý nghĩa ca sử dụng:** Chức năng 5 tập trung duy nhất vào nghiệp vụ đơn lẻ: **Xem thống kê doanh thu sự kiện** (View Event Revenue Statistics) dành cho Ban tổ chức và Quản trị viên.
* **Quan hệ `<<include>>` (Bắt buộc):**
  * `Chọn sự kiện cần thống kê`: Xác định đối tượng sự kiện cần kết xuất báo cáo tài chính.
  * `Tổng hợp & Tính toán KPIs`: Bước tính toán tự động các chỉ số doanh thu gộp, doanh thu thuần, tỷ lệ lấp đầy và giá vé bình quân.
* **Quan hệ `<<extend>>` (Tùy chọn mở rộng):**
  * `Lọc theo suất diễn & khoảng ngày`: Mở rộng khi cần thống kê thu hẹp.
  * `Xem chi tiết phân bổ doanh thu theo phân khu`: Mở rộng khi cần phân tích sâu tỷ trọng từng hạng vé.
  * `Xuất báo cáo doanh thu (Excel / PDF)`: Mở rộng khi cần lưu tệp ngoại tuyến về máy.

---

## 3. KỊCH BẢN PHÂN TÍCH CHO CÁC CHỨC NĂNG (SCENARIO)

Dưới đây là kịch bản phân tích chi tiết (Scenario) được xây dựng theo format chuẩn của môn học dành riêng cho **Chức năng 5: Xem thống kê doanh thu sự kiện** (*View Event Revenue Statistics*):

### Scenario cho chức năng: Xem thống kê doanh thu sự kiện

| Mục kịch bản | Nội dung chi tiết |
|:---|:---|
| **Tên use case** | `XemThongKeDoanhThuSuKien` (`ViewEventRevenueStatistics`) |
| **Tác nhân chính** | Ban tổ chức sự kiện (`Organizer`), Quản trị viên (`Admin`) |
| **Tiền điều kiện** | Khi người dùng muốn xem báo cáo thống kê doanh thu phải đăng nhập thành công vào hệ thống với vai trò Ban tổ chức hoặc Quản trị viên.<br>Sự kiện đã được tạo, cấu hình phân khu giá vé và đã mở bán vé (phát sinh dữ liệu đơn hàng). |
| **Đảm bảo tối thiểu** | Hệ thống hiển thị thông báo sự kiện chưa có dữ liệu hoặc lỗi kết nối, giữ nguyên giao diện để người dùng chọn lại sự kiện khác. |
| **Đảm bảo thành công** | Hệ thống tổng hợp, tính toán đầy đủ và hiển thị chính xác các chỉ số tài chính (Tổng doanh thu gộp, Doanh thu thuần sau thuế và phí, Tỷ lệ lấp đầy khán đài, Giá vé bình quân, Đánh giá hiệu suất) cùng bảng biểu chi tiết và biểu đồ phân bổ doanh thu theo từng phân khu. |
| **Kích hoạt** | Người dùng chọn chức năng 'Xem thống kê doanh thu sự kiện' trên thanh menu/bảng điều khiển hệ thống. |
| **Chuỗi sự kiện chính:** | 1. Người dùng chọn chức năng 'Xem thống kê doanh thu sự kiện' từ menu điều hướng của hệ thống.<br>2. Hệ thống hiển thị Form thống kê: yêu cầu người dùng chọn sự kiện từ danh sách sự kiện đang quản lý (`eventSelector`) và tùy chọn khoảng thời gian lọc (`datePicker`).<br>3. Người dùng chọn sự kiện cần xem từ danh sách, chọn khoảng thời gian tra cứu và nhấn nút 'Tra cứu'.<br>4. Hệ thống kiểm tra dữ liệu sự kiện, nạp danh sách các phân khu vé (`ZonePricing`), các suất diễn (`Showtime`) và các hóa đơn vé đã thanh toán thành công.<br>5. Hệ thống thực hiện chuỗi phương thức tính toán tài chính nội tại:<br>&nbsp;&nbsp;&nbsp;• Tính tổng sức chứa phát hành: `calculateTotalCapacity()`<br>&nbsp;&nbsp;&nbsp;• Tính tổng số vé đã bán thành công: `calculateTotalTicketsSold()`<br>&nbsp;&nbsp;&nbsp;• Tính tổng doanh thu bán vé gộp: `calculateGrossRevenue()`<br>&nbsp;&nbsp;&nbsp;• Khấu trừ 10% VAT và 5% phí sàn để tính doanh thu thuần: `calculateNetRevenue()`<br>&nbsp;&nbsp;&nbsp;• Tính tỷ lệ lấp đầy khán đài: `calculateOccupancyRate()`<br>&nbsp;&nbsp;&nbsp;• Tính giá vé bình quân mỗi vé bán ra: `calculateAverageTicketPrice()`<br>&nbsp;&nbsp;&nbsp;• Tính tỷ trọng đóng góp doanh thu của từng phân khu: `calculateZoneContribution(zoneId)`<br>&nbsp;&nbsp;&nbsp;• Đánh giá xếp hạng hiệu quả mở bán: `evaluatePerformance()`<br>6. Hệ thống hiển thị toàn bộ các thẻ KPI chỉ số tài chính, bảng chi tiết từng phân khu vé và vẽ biểu đồ tỷ trọng phân bổ doanh thu trực quan. |
| **Ngoại lệ:** | **4.a. Sự kiện được chọn chưa có giao dịch bán vé nào phát sinh trong khoảng thời gian tra cứu**<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.a.1. Hệ thống hiển thị thông báo: 'Sự kiện chưa phát sinh giao dịch bán vé'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.a.2. Hiển thị các chỉ số ở mức mặc định (0 VNĐ, 0%) và cho phép người dùng chọn lại sự kiện khác.<br>**4.b. Người dùng nhập khoảng thời gian lọc không hợp lệ (Ngày bắt đầu > Ngày kết thúc)**<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.b.1. Hệ thống hiển thị thông báo lỗi: 'Khoảng thời gian tra cứu không hợp lệ'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.b.2. Đặt lại khoảng thời gian mặc định là toàn bộ thời gian mở bán của sự kiện.<br>**4.c. Lỗi kết nối máy chủ cơ sở dữ liệu hoặc hệ thống tính toán**<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.c.1. Hệ thống hiển thị thông báo: 'Lỗi kết xuất dữ liệu thống kê, vui lòng thử lại sau'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.c.2. Giữ nguyên giao diện ban đầu. |

---

## 4. KỊCH BẢN VÀ THIẾT KẾ GIAO DIỆN CHO CÁC CHỨC NĂNG

Thiết kế giao diện cho **Chức năng 5: Xem thống kê doanh thu sự kiện** (`RevenueReportView`) được tối ưu hóa nhằm cung cấp trải nghiệm phân tích tài chính trực quan, rõ ràng và tức thì cho Ban tổ chức.

### 4.1. Bảng đặc tả các thành phần điều khiển trên giao diện (UI Controls Specification)

| Mã điều khiển | Tên thành phần | Kiểu điều khiển (Type) | Ý nghĩa nghiệp vụ & Ràng buộc dữ liệu |
|:---|:---|:---|:---|
| `cb_event` | Chọn sự kiện | ComboBox (Dropdown) | Danh sách các sự kiện do ban tổ chức quản lý. Ràng buộc: bắt buộc chọn 1 sự kiện. |
| `dp_from_date`| Từ ngày | DatePicker / TextInput | Ngày bắt đầu lọc số liệu (DD/MM/YYYY). Mặc định: ngày mở bán vé đầu tiên. |
| `dp_to_date` | Đến ngày | DatePicker / TextInput | Ngày kết thúc lọc số liệu (DD/MM/YYYY). Ràng buộc: phải $\ge$ `dp_from_date`. |
| `btn_search` | Tra cứu | Button (Primary Blue) | Kích hoạt gửi yêu cầu tra cứu và tính toán số liệu thống kê. |
| `btn_excel` | Xuất Excel | Button (Success Green) | Kết xuất toàn bộ bảng số liệu phân tích ra tệp bảng tính `.xlsx`. |
| `btn_pdf` | In PDF | Button (Danger Red) | Tạo tài liệu báo cáo định dạng `.pdf` chuẩn hóa để in ấn hoặc ký duyệt. |
| `card_gross` | Tổng doanh thu gộp | KPI Card (Blue) | Hiển thị tổng số tiền bán vé thu được trước thuế phí (`Gross Revenue`). |
| `card_net` | Doanh thu thuần | KPI Card (Green) | Hiển thị số tiền thực nhận sau khi khấu trừ 10% VAT và 5% phí nền tảng (`Net Revenue`). |
| `card_occupancy`| Tỷ lệ lấp đầy | KPI Card (Amber) | Hiển thị phần trăm số ghế đã bán trên tổng sức chứa và xếp hạng (`EXCELLENT`). |
| `card_avg_price`| Giá vé bình quân | KPI Card (Purple) | Hiển thị giá bán trung bình trên mỗi vé thành công (`Average Ticket Price`). |
| `chart_zone` | Biểu đồ phân bổ phân khu | Donut Chart | Biểu đồ tròn trực quan tỷ trọng đóng góp doanh thu của từng phân khu vé. |
| `tbl_breakdown`| Bảng chi tiết phân khu | Data Table | Liệt kê chi tiết từng phân khu: Đơn giá, Chỉ tiêu, Đã bán, Tỷ lệ lấp đầy, Doanh thu gộp, Tỷ trọng. |

### 4.2. Kịch bản tương tác người dùng - hệ thống (UI Interaction Scenario)

| Bước | Hành động của người dùng (User Action) | Phản hồi của hệ thống (System Response) |
|:---:|:---|:---|
| **1** | Người dùng truy cập vào mục 'Thống kê doanh thu' từ menu hệ thống. | Hệ thống tải giao diện `RevenueReportView`, nạp danh sách các sự kiện vào `cb_event`, đặt khoảng ngày mặc định là 30 ngày gần nhất. |
| **2** | Người dùng nhấp vào `cb_event` và chọn sự kiện "Born Pink World Tour Hanoi 2026". | Hệ thống ghi nhận mã sự kiện `eventId`, tự động cập nhật ngày mở bán và ngày kết thúc sự kiện vào 2 ô DatePicker. |
| **3** | Người dùng nhấp nút 'Tra cứu' (`btn_search`). | Giao diện hiển thị biểu tượng tải dữ liệu (loading spinner). Controller nạp Entity `RevenueReport`, kích hoạt chuỗi tính toán và trả về `RevenueSummaryDto`. |
| **4** | Hệ thống nhận kết quả tính toán thành công. | Giao diện cập nhật tức thì 4 thẻ KPI, kết xuất biểu đồ Donut tỷ trọng doanh thu bên trái và điền đầy đủ dữ liệu vào bảng chi tiết phân khu bên phải. |
| **5** | Người dùng rê chuột vào các phần của biểu đồ Donut. | Hệ thống hiển thị tooltip chi tiết: Tên phân khu, doanh thu thu được và tỷ lệ phần trăm đóng góp. |
| **6** | Người dùng nhấp nút 'Xuất Excel' hoặc 'In PDF'. | Hệ thống gọi phương thức `exportExcel()` / `exportPdf()`, hiển thị hộp thoại tải tệp xuống máy tính của người dùng. |

### 4.3. Bản vẽ thiết kế giao diện trực quan (UI Mockup Wireframe)

Toàn bộ bố cục màn hình được phân chia khoa học thành 4 vùng chức năng (Thanh điều hướng bộ lọc $\rightarrow$ Khung thẻ KPI $\rightarrow$ Khung biểu đồ Donut $\rightarrow$ Bảng phân tích chi tiết):

*(Tham khảo tệp ảnh thiết kế độ phân giải cao đính kèm: `PTTK/diagrams/ui_m5_view_revenue.png`)*

---

## 5. BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH CHO HỆ THỐNG VÀ CHO CÁC CHỨC NĂNG

### Nguyên lý lớp phân tích (Analysis Entity Classes)
1. Thể hiện các **khái niệm nghiệp vụ cốt lõi** trong miền bài toán (Domain Model).
2. Mỗi lớp gồm 2 ngăn: **Tên thực thể** và **Danh sách thuộc tính nghiệp vụ thuần túy**.
3. Không phụ thuộc vào kiểu dữ liệu lập trình cụ thể (`int`, `varchar2`, `boolean`...), không có các hàm kỹ thuật `getter/setter`.
4. Thể hiện rõ các mối quan hệ ngữ nghĩa: Kế thừa (Generalization), Kết hợp (Association), Kết tập mạnh (Composition), Kết tập yếu (Aggregation) cùng bản số (Multiplicity).

### 3.1. Biểu đồ lớp thực thể phân tích tổng thể hệ thống

```mermaid
classDiagram
    class User {
        userId
        fullName
        email
        phoneNumber
        password
        role
    }
    class Customer {
        rewardPoints
        membershipTier
    }
    class Organizer {
        organizationName
        taxCode
        businessLicense
        description
    }
    class Venue {
        venueId
        venueName
        detailedAddress
        maxCapacity
    }
    class SeatMap {
        seatMapId
        seatMapName
        stageType
        totalSeats
    }
    class SeatZone {
        zoneId
        zoneName
        colorHex
        zoneType
        seatCount
    }
    class Seat {
        seatId
        rowLabel
        seatNumber
        coordinateX
        coordinateY
    }
    class Event {
        eventId
        title
        category
        description
        posterUrl
        status
    }
    class Showtime {
        showtimeId
        showDate
        startTime
        endTime
    }
    class ZonePricing {
        pricingId
        unitPrice
        maxQuota
    }
    class VirtualQueue {
        queueId
        queueNumber
        joinedAt
        status
    }
    class SeatHold {
        holdId
        heldAt
        expiresAt
        status
    }
    class Order {
        orderId
        orderDate
        totalAmount
        discountAmount
        status
    }

    User <|-- Customer
    User <|-- Organizer
    Organizer "1" --> "*" Event : creates
    Venue "1" --> "*" Event : hosts at
    Venue "1" --> "*" SeatMap : has
    SeatMap "1" *-- "*" SeatZone : contains
    SeatZone "1" *-- "*" Seat : contains
    Event "1" *-- "*" Showtime : has
    Showtime "1" --> "*" ZonePricing : applies
    SeatZone "1" --> "*" ZonePricing : prices
    Customer "1" --> "*" VirtualQueue : joins
    VirtualQueue "1" --> "*" SeatHold : transitions
    SeatHold "*" --> "1..*" Seat : locks
    Customer "1" --> "*" Order : pays for
```

---

### 3.2. Biểu đồ lớp phân tích theo từng phân hệ

#### Phân hệ 1: Quản lý tài khoản người dùng
* Các thực thể: `User`, `Customer`, `Organizer`, `UserSession`, `Notification`.
* Quan hệ: Kế thừa từ `User`; Khách hàng sở hữu nhiều `UserSession`; Người dùng nhận nhiều `Notification`.

#### Phân hệ 2: Tìm kiếm & Xem sự kiện
* Các thực thể: `Event`, `Category`, `Venue`, `Showtime`, `Artist`, `FavoriteEvent`.
* Quan hệ: Sự kiện thuộc một Thể loại (`Category`), tổ chức tại một Địa điểm (`Venue`), bao hàm nhiều Suất diễn (`Showtime`); Nghệ sĩ (`Artist`) biểu diễn tại nhiều Suất diễn; Khách hàng lưu sự kiện vào danh sách Yêu thích (`FavoriteEvent`).

#### Phân hệ 3: Xếp hàng và chọn chỗ
* Các thực thể: `SeatMap`, `SeatZone`, `Seat`, `Customer`, `VirtualQueue`, `SeatHold`.
* Quan hệ: Cấu trúc phân cấp chứa `SeatMap` -> `SeatZone` -> `Seat`; Khách hàng vào `VirtualQueue`; Khi đến lượt tạo bản ghi `SeatHold` liên kết với danh sách các `Seat` đã chọn.

#### Phân hệ 4: Tính tiền và Xuất vé
* Các thực thể: `Order`, `Ticket`, `Voucher`, `PaymentTransaction`, `Customer`, `Seat`.
* Quan hệ: `Order` do `Customer` lập, áp dụng 0..1 `Voucher`, thanh toán qua 1 `PaymentTransaction`, và bao hàm 1..* `Ticket`. Mỗi `Ticket` được gán cố định cho 1 `Seat`.

#### Chức năng 5: Xem thống kê doanh thu sự kiện
* Các thực thể: `Organizer`, `Event`, `Showtime`, `ZonePricing`, `RevenueReport`, `SeatZone`.
* Quan hệ: Ban tổ chức (`Organizer`) yêu cầu báo cáo doanh thu cho Sự kiện (`Event`); Thực thể `RevenueReport` tổng hợp các phân khu vé (`ZonePricing`) và suất diễn (`Showtime`), trực tiếp đóng gói toàn bộ phương thức tính toán tài chính.

---

### 3.3. Biểu đồ lớp phân tích Chức năng 5: Xem thống kê doanh thu sự kiện

Để giải quyết triệt để yêu cầu: *"Nếu là class thì cần có các phương thức thực hiện tính toán, nếu không chỉ là nhóm dữ liệu không được coi là class"*, biểu đồ lớp phân tích dưới đây thể hiện toàn diện các phương thức tính toán tài chính của các thực thể tham gia ca sử dụng này:

```mermaid
classDiagram
    class Organizer {
        <<analysis>>
        userId
        companyName
        taxId
        email
        +selectEvent()
        +viewRevenueReport()
    }

    class Event {
        <<analysis>>
        eventId
        title
        category
        status
        +getTotalCapacity()
        +getShowtimes()
    }

    class RevenueReport {
        <<analysis>>
        id
        eventId
        calculatedAt
        taxRate
        platformFeeRate
        totalTicketsSold
        grossRevenue
        netRevenue
        occupancyRate
        averageTicketPrice
        +calculateTotalCapacity()
        +calculateTotalTicketsSold()
        +calculateGrossRevenue()
        +calculateNetRevenue()
        +calculateOccupancyRate()
        +calculateAverageTicketPrice()
        +calculateZoneContribution(zoneId)
        +evaluatePerformance()
    }

    class ZonePricing {
        <<analysis>>
        id
        zoneName
        price
        maxQuota
        soldCount
        +calculateZoneGross()
        +calculateRemainingSeats()
        +getSoldRate()
        +isSoldOut()
    }

    class Showtime {
        <<analysis>>
        id
        showDate
        startTime
        endTime
        +calculateShowtimeRevenue()
        +getSoldTicketsCount()
    }

    class SeatZone {
        <<analysis>>
        id
        zoneName
        colorHex
        seatCount
        +countTotalSeats()
    }

    Organizer "1" --> "*" Event : manages
    Organizer "1" --> "*" RevenueReport : requests
    Event "1" --> "*" ZonePricing : configures
    RevenueReport "1" --> "*" ZonePricing : aggregates
    RevenueReport "1" --> "*" Showtime : summarizes
    ZonePricing "*" --> "1" SeatZone : maps to
    Showtime "1" --> "*" ZonePricing : prices via
```

---

## 6. BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ CHO HỆ THỐNG VÀ CHO CÁC CHỨC NĂNG

### Nguyên lý lớp thiết kế (Design Entity Classes)
1. Thể hiện **mô hình hướng đối tượng chi tiết** sẵn sàng ánh xạ ORM (JPA/Hibernate) và sinh mã nguồn.
2. Stereotype `<<entity>>` cho các thực thể dữ liệu.
3. Cấu trúc chuẩn 3 ngăn: **Tên lớp**, **Thuộc tính với phạm vi (`-` private), tên biến và kiểu dữ liệu cụ thể, khóa chính [PK]**, **Phương thức với phạm vi (`+` public), tham số và kiểu trả về**.
4. Các phương thức nghiệp vụ nội tại được mô hình hóa rõ ràng.

### 4.1. Biểu đồ lớp thực thể thiết kế tổng thể hệ thống

```mermaid
classDiagram
    class User {
        <<entity>>
        -id: Long
        -username: String
        -passwordHash: String
        -email: String
        -phone: String
        -role: UserRole
        +login() boolean
        +changePassword() void
        +updateProfile() void
    }
    class Customer {
        <<entity>>
        -points: int
        +addFavorite() void
        +getOrderHistory() List
    }
    class Organizer {
        <<entity>>
        -taxCode: String
        -businessLicense: String
        +createEvent() void
        +verifyLicense() boolean
    }
    class Venue {
        <<entity>>
        -id: Long
        -name: String
        -address: String
        -maxCapacity: int
        +isAvailable() boolean
    }
    class SeatMap {
        <<entity>>
        -id: Long
        -name: String
        -stageType: String
        -totalSeats: int
        +validateLayout() boolean
    }
    class SeatZone {
        <<entity>>
        -id: Long
        -zoneName: String
        -colorHex: String
        -seatCount: int
        +getAvailableCount() int
    }
    class Seat {
        <<entity>>
        -id: Long
        -rowLabel: String
        -seatNo: int
        -isLocked: boolean
        +lock() void
        +isAvailable() boolean
    }
    class Event {
        <<entity>>
        -id: Long
        -title: String
        -category: String
        -status: EventStatus
        +publish() void
        +cancel() void
    }
    class Showtime {
        <<entity>>
        -id: Long
        -showDate: LocalDate
        -startTime: LocalTime
        +isUpcoming() boolean
    }
    class VirtualQueue {
        <<entity>>
        -id: Long
        -queueNo: int
        -sessionToken: String
        -status: QueueStatus
        +isMyTurn() boolean
        +expire() void
    }
    class SeatHold {
        <<entity>>
        -id: Long
        -holdToken: String
        -expiresAt: LocalDateTime
        +isExpired() boolean
        +cancel() void
    }
    class Order {
        <<entity>>
        -id: Long
        -orderNo: String
        -totalAmount: double
        -status: OrderStatus
        +calculateTotal() double
        +complete() void
    }
    class Ticket {
        <<entity>>
        -id: Long
        -ticketCode: String
        -qrCode: String
        -isCheckedIn: boolean
        +generateQR() String
        +checkIn() boolean
    }

    User <|-- Customer
    User <|-- Organizer
    Organizer "1" --> "*" Event : creates
    Venue "1" --> "*" Event : hosts at
    Venue "1" --> "*" SeatMap : has
    SeatMap "1" *-- "*" SeatZone : contains
    SeatZone "1" *-- "*" Seat : contains
    Event "1" *-- "*" Showtime : has
    VirtualQueue "1" --> "*" SeatHold : transitions
    SeatHold "*" --> "1..*" Seat : locks
    Order "1" *-- "1..*" Ticket : contains
    Ticket "1" --> "1" Seat : maps to
```

---

### 4.2. Từ điển dữ liệu và Lớp thiết kế chi tiết theo 5 phân hệ

#### Phân hệ 1: Quản lý tài khoản (Classes: User, Customer, Organizer, UserSession, Notification)
| Lớp thiết kế | Thuộc tính chi tiết (Kiểu dữ liệu & Ràng buộc) | Phương thức nghiệp vụ (Operations) |
|:---|:---|:---|
| **User** | `- id: Long [PK, Auto]`<br>`- username: String [Unique]`<br>`- passwordHash: String [BCrypt]`<br>`- email: String [Unique]`<br>`- phone: String`<br>`- role: UserRole [Enum]` | `+ authenticate(pwd: String): boolean`<br>`+ changePassword(newPwd: String): void`<br>`+ updateInfo(dto: UserDto): void`<br>`+ isAccountNonLocked(): boolean` |
| **Customer** | `- rewardPoints: int [Default 0]`<br>`- memberTier: MemberTier [Enum]` | `+ addRewardPoints(pts: int): void`<br>`+ getOrderHistory(): List<Order>`<br>`+ canRedeemPoints(pts: int): boolean` |
| **Organizer** | `- orgName: String [Not Null]`<br>`- taxId: String [Unique]`<br>`- businessLicense: String` | `+ verifyLicense(): boolean`<br>`+ getManagedEvents(): List<Event>`<br>`+ updateOrgProfile(info: OrgDto): void` |
| **UserSession** | `- id: Long [PK]`<br>`- jwtToken: String [Not Null]`<br>`- createdAt: LocalDateTime`<br>`- expiresAt: LocalDateTime` | `+ isExpired(): boolean`<br>`+ refreshToken(): String`<br>`+ revoke(): void` |
| **Notification**| `- id: Long [PK]`<br>`- title: String`<br>`- message: String`<br>`- isRead: boolean [Default false]` | `+ markAsRead(): void`<br>`+ sendEmailNotification(): boolean` |

---

#### Phân hệ 2: Tìm kiếm & Xem sự kiện (Classes: Event, Showtime, Category, Venue, Artist, FavoriteEvent)
| Lớp thiết kế | Thuộc tính chi tiết (Kiểu dữ liệu & Ràng buộc) | Phương thức nghiệp vụ (Operations) |
|:---|:---|:---|
| **Event** | `- id: Long [PK]`<br>`- title: String [Not Null]`<br>`- description: String`<br>`- bannerUrl: String`<br>`- status: EventStatus [Enum]` | `+ publish(): void`<br>`+ cancel(): void`<br>`+ isUpcoming(): boolean`<br>`+ getActiveShowtimes(): List<Showtime>` |
| **Showtime** | `- id: Long [PK]`<br>`- showDate: LocalDate [Not Null]`<br>`- startTime: LocalTime [Not Null]`<br>`- endTime: LocalTime` | `+ isAvailableForBooking(): boolean`<br>`+ getAvailableSeats(): int`<br>`+ isOngoing(): boolean` |
| **Category** | `- id: Long [PK]`<br>`- name: String [Unique]`<br>`- code: String [Unique]` | `+ getEvents(): List<Event>`<br>`+ countEvents(): int` |
| **Venue** | `- id: Long [PK]`<br>`- name: String [Not Null]`<br>`- address: String`<br>`- capacity: int [> 0]` | `+ checkCapacity(): boolean`<br>`+ getAssignedSeatMap(): SeatMap` |
| **Artist** | `- id: Long [PK]`<br>`- stageName: String [Not Null]`<br>`- bio: String`<br>`- avatarUrl: String` | `+ getParticipatingEvents(): List<Event>` |
| **FavoriteEvent** | `- id: Long [PK]`<br>`- customerId: Long [FK]`<br>`- savedDate: LocalDateTime` | `+ notifySaleOpening(): void`<br>`+ remove(): void` |

---

#### Phân hệ 3: Xếp hàng và chọn chỗ (Classes: SeatMap, SeatZone, Seat, VirtualQueue, SeatHold)
| Lớp thiết kế | Thuộc tính chi tiết (Kiểu dữ liệu & Ràng buộc) | Phương thức nghiệp vụ (Operations) |
|:---|:---|:---|
| **SeatMap** | `- id: Long [PK]`<br>`- mapName: String [Not Null]`<br>`- totalSeats: int [> 0]`<br>`- layoutSvg: String [SVG Data]` | `+ validateLayout(): boolean`<br>`+ getZones(): List<SeatZone>`<br>`+ getTotalCapacity(): int` |
| **SeatZone** | `- id: Long [PK]`<br>`- zoneName: String [VIP, CAT 1...]`<br>`- colorHex: String [#HEX]`<br>`- zoneType: ZoneType [SEATED, STANDING]` | `+ getSeats(): List<Seat>`<br>`+ countVacantSeats(): int`<br>`+ isStandingZone(): boolean` |
| **Seat** | `- id: Long [PK]`<br>`- rowLabel: String [A, B, C...]`<br>`- seatNumber: int [1, 2, 3...]`<br>`- isLocked: boolean [Default false]` | `+ lockSeat(token: String): boolean`<br>`+ unlockSeat(): void`<br>`+ isAvailable(): boolean`<br>`+ getSeatCode(): String` |
| **VirtualQueue**| `- id: Long [PK]`<br>`- queueNumber: int [Auto]`<br>`- accessToken: String [UUID]`<br>`- status: QueueStatus [WAITING, SERVING, EXPIRED]` | `+ isTurn(): boolean`<br>`+ generateToken(): String`<br>`+ expireToken(): void` |
| **SeatHold** | `- id: Long [PK]`<br>`- holdToken: String [UUID, Unique]`<br>`- startTime: LocalDateTime`<br>`- expiresAt: LocalDateTime` | `+ isExpired(): boolean`<br>`+ getRemainingSeconds(): long`<br>`+ confirmHold(): void`<br>`+ releaseHold(): void` |

---

#### Phân hệ 4: Tính tiền và Xuất vé (Classes: Order, Voucher, PaymentTransaction, Ticket)
| Lớp thiết kế | Thuộc tính chi tiết (Kiểu dữ liệu & Ràng buộc) | Phương thức nghiệp vụ (Operations) |
|:---|:---|:---|
| **Order** | `- id: Long [PK]`<br>`- orderCode: String [ORD-XXXXX]`<br>`- subTotal: double [>= 0]`<br>`- discount: double [>= 0]`<br>`- finalTotal: double [>= 0]`<br>`- status: OrderStatus [PENDING, PAID, CANCELLED]` | `+ calculateFinalTotal(): double`<br>`+ applyVoucher(v: Voucher): boolean`<br>`+ markAsPaid(): void`<br>`+ cancelOrder(): void` |
| **Voucher** | `- id: Long [PK]`<br>`- code: String [Unique]`<br>`- percentOff: double [0.0 - 100.0]`<br>`- maxDiscount: double`<br>`- validUntil: LocalDate` | `+ isValid(amount: double): boolean`<br>`+ calculateDiscount(amount: double): double`<br>`+ decrementQuota(): void` |
| **PaymentTransaction** | `- id: Long [PK]`<br>`- transRef: String [Bank Ref]`<br>`- method: PaymentMethod [VNPAY, MOMO, VISA]`<br>`- transAmount: double`<br>`- status: TransStatus [SUCCESS, FAILED]` | `+ processPayment(): boolean`<br>`+ verifyWebhook(payload: String): boolean`<br>`+ getGatewayUrl(): String` |
| **Ticket** | `- id: Long [PK]`<br>`- ticketCode: String [TCK-XXXXX]`<br>`- qrCodeHash: String [HMAC-SHA256]`<br>`- price: double`<br>`- isUsed: boolean [Default false]`<br>`- checkinTime: LocalDateTime` | `+ generateEncryptedQR(): String`<br>`+ checkIn(): boolean`<br>`+ isCheckedIn(): boolean`<br>`+ cancelTicket(): void` |

---

---

### 4.3. Thiết kế chi tiết Chức năng 5: Xem thống kê doanh thu sự kiện (View Event Revenue Statistics)

* **Lý do lựa chọn:** Đây là chức năng đơn lẻ (Single Atomic Function - Read/Calculate Analytics) cốt lõi của Module 5. Chức năng yêu cầu các lớp thực thể phải đóng gói đầy đủ **các phương thức thực hiện tính toán tài chính nghiệp vụ**, đảm bảo không biến lớp thành cấu trúc dữ liệu thụ động (*Anemic Domain Model*).

#### a. Đặc tả ca sử dụng chi tiết (Use Case Specification)
| Thuộc tính | Nội dung chi tiết |
|:---|:---|
| **Tên chức năng** | **Xem thống kê doanh thu sự kiện (View Event Revenue Statistics)** |
| **Tác nhân** | Ban tổ chức sự kiện (`Organizer`), Quản trị viên (`Admin`) |
| **Tiền điều kiện** | 1. Ban tổ chức đã đăng nhập vào hệ thống.<br>2. Sự kiện đã mở bán và phát sinh giao dịch đặt vé. |
| **Hậu điều kiện** | Hiển thị bảng tổng kết các chỉ số tài chính (KPIs) và biểu đồ phân bổ doanh thu theo phân khu. |
| **Luồng sự kiện chính** | 1. Ban tổ chức chọn sự kiện cần xem báo cáo.<br>2. Giao diện `RevenueReportView` gửi yêu cầu đến `RevenueReportController`.<br>3. Controller khởi tạo đối tượng `RevenueReport` nạp các phân khu `ZonePricing`.<br>4. `RevenueReport` gọi chuỗi phương thức tính toán: `calculateGrossRevenue()`, `calculateNetRevenue()`, `calculateOccupancyRate()`, `evaluatePerformance()`.<br>5. Controller chuyển đổi dữ liệu kết quả thành `RevenueSummaryDto` trả về View.<br>6. View hiển thị các thẻ KPI và biểu đồ doanh thu trực quan. |

#### b. Biểu đồ tuần tự (Sequence Diagram)
```mermaid
sequenceDiagram
    autonumber
    actor Org as Ban tổ chức
    participant V as :RevenueReportView
    participant C as :RevenueReportController
    participant R as report:RevenueReport
    participant Z as p:ZonePricing

    Org->>V: onSelectEvent(eventId)
    V->>C: handleViewReport(eventId)
    C->>R: <<create>> (eventId, taxRate, feeRate)
    
    rect rgb(240, 248, 255)
        note over R,Z: Quá trình tính toán nội tại trong Entity
        C->>R: calculateGrossRevenue()
        loop Duyệt từng phân khu ZonePricing
            R->>Z: calculateZoneGross()
            Z-->>R: zoneGrossAmount
        end
        C->>R: calculateNetRevenue()
        C->>R: calculateOccupancyRate()
        C->>R: evaluatePerformance()
        R-->>C: PerformanceStatus (EXCELLENT/GOOD...)
    end

    C->>C: formatReportData()
    C-->>V: return RevenueSummaryDto
    V-->>Org: renderKPIs & showZoneCharts()
```

#### c. Biểu đồ lớp thiết kế chi tiết (Mô hình BCE)
```mermaid
classDiagram
    class RevenueReportView {
        <<boundary>>
        -eventSelector: ComboBox
        -kpiPanel: Panel
        -zoneChart: ChartView
        +onSelectEvent(eventId: Long) void
        +displayKPIs(dto: RevenueSummaryDto) void
        +renderZoneChart(data: List) void
        +showError(msg: String) void
    }

    class RevenueReportController {
        <<control>>
        -reportService: ReportService
        -eventRepo: EventRepository
        +handleViewReport(eventId: Long) RevenueSummaryDto
        +calculateZoneAnalytics(eventId: Long) List
        +formatReportData(report: RevenueReport) Dto
    }

    class RevenueReport {
        <<entity>>
        -id: Long
        -eventId: Long
        -calculatedAt: LocalDateTime
        -taxRate: double
        -platformFeeRate: double
        -totalTicketsSold: int
        -grossRevenue: double
        -netRevenue: double
        -occupancyRate: double
        -averageTicketPrice: double
        +calculateTotalCapacity() int
        +calculateTotalTicketsSold() int
        +calculateGrossRevenue() double
        +calculateNetRevenue() double
        +calculateOccupancyRate() double
        +calculateAverageTicketPrice() double
        +calculateZoneContribution(zoneId: Long) double
        +evaluatePerformance() PerformanceStatus
    }

    class ZonePricing {
        <<entity>>
        -id: Long
        -zoneName: String
        -price: double
        -maxQuota: int
        -soldCount: int
        +calculateZoneGross() double
        +calculateRemainingSeats() int
        +getSoldRate() double
        +isSoldOut() boolean
    }

    class Showtime {
        <<entity>>
        -id: Long
        -showDate: LocalDate
        -startTime: LocalTime
        -endTime: LocalTime
        +calculateShowtimeRevenue() double
        +getSoldTicketsCount() int
    }

    class Event {
        <<entity>>
        -id: Long
        -title: String
        -category: String
        -status: EventStatus
        +getTotalCapacity() int
        +getShowtimes() List
    }

    class RevenueSummaryDto {
        <<dto>>
        -grossRevenue: double
        -netRevenue: double
        -occupancyRate: double
        -averagePrice: double
        -status: PerformanceStatus
        -zoneBreakdowns: List
        +getGrossRevenue() double
        +getNetRevenue() double
        +getOccupancyRate() double
    }

    class PerformanceStatus {
        <<enumeration>>
        EXCELLENT
        GOOD
        AVERAGE
        POOR
    }

    RevenueReportView ..> RevenueReportController : triggers
    RevenueReportController ..> RevenueReport : invokes
    RevenueReportController ..> RevenueSummaryDto : creates DTO
    RevenueSummaryDto <.. RevenueReportView : displays
    RevenueReport "1" --> "*" ZonePricing : aggregates
    RevenueReport "1" --> "*" Showtime : summarizes
    Event "1" --> "*" Showtime : has
    RevenueReport ..> PerformanceStatus : evaluates to
```

#### d. Bảng chi tiết các phương thức thực hiện tính toán (Computational Methods)
| Tên phương thức | Lớp sở hữu | Kiểu trả về | Công thức & Thuật toán tính toán |
|:---|:---|:---:|:---|
| `calculateTotalCapacity()` | `RevenueReport` | `int` | $\text{TotalCapacity} = \sum \text{zone.seatCount}$ (Tổng số ghế phát hành của tất cả các khu vực). |
| `calculateTotalTicketsSold()` | `RevenueReport` | `int` | $\text{TotalSold} = \sum \text{zone.soldCount}$ (Tổng số vé đã bán thành công). |
| `calculateGrossRevenue()` | `RevenueReport` | `double` | $\text{GrossRevenue} = \sum (\text{zone.soldCount} \times \text{zone.price})$ (Doanh thu bán vé gộp). |
| `calculateNetRevenue()` | `RevenueReport` | `double` | $\text{NetRevenue} = \text{GrossRevenue} \times (1 - \text{taxRate} - \text{platformFeeRate})$ (Doanh thu thuần sau thuế và phí sàn). |
| `calculateOccupancyRate()` | `RevenueReport` | `double` | $\text{OccupancyRate} = \frac{\text{TotalSold}}{\text{TotalCapacity}} \times 100\%$ (Tỷ lệ lấp đầy sân khấu). |
| `calculateAverageTicketPrice()` | `RevenueReport` | `double` | $\text{AvgPrice} = \frac{\text{GrossRevenue}}{\text{TotalSold}}$ (Giá vé bình quân thực tế). |
| `calculateZoneContribution(zoneId)` | `RevenueReport` | `double` | $\text{Contribution} = \frac{\text{ZoneGross}}{\text{GrossRevenue}} \times 100\%$ (Tỷ trọng doanh thu theo từng phân khu). |
| `evaluatePerformance()` | `RevenueReport` | `Enum` | Phân loại hiệu quả tài chính:<br>• $\ge 85\%$: `EXCELLENT` (Cháy vé)<br>• $70\% - 84\%$: `GOOD` (Đạt chỉ tiêu)<br>• $50\% - 69\%$: `AVERAGE` (Hòa vốn)<br>• $< 50\%$: `POOR` (Cần giải cứu) |
| `calculateZoneGross()` | `ZonePricing` | `double` | $\text{ZoneGross} = \text{price} \times \text{soldCount}$ (Doanh thu riêng của phân khu). |
| `getSoldRate()` | `ZonePricing` | `double` | $\text{SoldRate} = \frac{\text{soldCount}}{\text{maxQuota}} \times 100\%$ (Tỷ lệ bán của phân khu). |

#### e. Các ghi chú kiến trúc và thiết kế giải thích chi tiết sơ đồ (Architectural & Design Notes)

1. **Khái niệm DTO (Data Transfer Object) và lý do áp dụng trong kiến trúc:**
   * **Bản chất DTO:** `RevenueSummaryDto` và `ZoneRevenueDto` là các đối tượng truyền tải dữ liệu thuần túy (POJO) giữa tầng Điều khiển (`RevenueReportController`) và tầng Giao diện (`RevenueReportView`).
   * **Lý do thiết kế:**
     * *Tính đóng gói & Bảo mật (Security & Encapsulation):* DTO giúp che giấu cấu trúc bảng cơ sở dữ liệu và các trường nhạy cảm của Entity, không để lộ xuống tầng Presentation.
     * *Làm phẳng dữ liệu & Tối ưu hiệu năng (Performance & Flattening):* Thay vì truyền các đối tượng Entity phức tạp có quan hệ liên kết vòng, Controller gọi các hàm tính toán của Entity, đóng gói toàn bộ kết quả (`grossRevenue`, `netRevenue`, `occupancyRate`, `performanceStatus`) vào một đối tượng DTO phẳng, nhẹ. Giao diện người dùng (UI) chỉ việc đọc các giá trị này để hiển thị lên thẻ KPI và vẽ biểu đồ mà không cần tính toán lại.
     * *Khắc phục lỗi Lazy Loading trong ORM:* Trong JPA/Hibernate, việc truy cập các thuộc tính liên kết lười (Lazy) ngoài phạm vi Session/Transaction dễ dẫn đến ngoại lệ `LazyInitializationException`. DTO được khởi tạo bên trong ranh giới Service/Controller giải quyết triệt để lỗi này.

2. **Phân tách vai trò theo mẫu thiết kế BCE (Boundary - Control - Entity):**
   * `<<boundary>>` (`RevenueReportView`): Lớp giao diện người dùng, chịu trách nhiệm nhận sự kiện tương tác (chọn sự kiện từ ComboBox) và kết xuất dữ liệu DTO lên màn hình (KPI cards, biểu đồ tròn phân khu).
   * `<<control>>` (`RevenueReportController`): Đóng vai trò điều phối luồng xử lý (Orchestrator). Controller **không trực tiếp chứa các công thức toán học tính tiền**, mà điều hướng: nhận yêu cầu từ View $\rightarrow$ nạp Entity $\rightarrow$ kích hoạt các hàm tính toán của Entity $\rightarrow$ đóng gói kết quả vào DTO $\rightarrow$ gửi trả View.
   * `<<entity>>` (`RevenueReport`, `ZonePricing`, `Showtime`, `Event`): Lớp thực thể nghiệp vụ chứa dữ liệu và trực tiếp đóng gói các thuật toán tính toán (*Rich Domain Model*).
   * `<<enumeration>>` (`PerformanceStatus`): Kiểu liệt kê định nghĩa tập hợp các giá trị đánh giá chuẩn mực (`EXCELLENT`, `GOOD`, `AVERAGE`, `POOR`).
   * `<<dto>>` (`RevenueSummaryDto`): Đối tượng mang dữ liệu kết quả giữa Control và Boundary.

3. **Giải quyết quan hệ N-N giữa Showtime và SeatZone thông qua lớp liên kết ZonePricing:**
   * Mối quan hệ giữa Suất diễn (`Showtime`) và Phân khu ghế (`SeatZone`) về bản chất là quan hệ nhiều - nhiều ($*..*$). Tuy nhiên, tại mỗi suất diễn cụ thể, một phân khu sẽ có đơn giá vé riêng (`price`), chỉ tiêu phát hành riêng (`maxQuota`) và số vé đã bán thực tế riêng (`soldCount`).
   * Do đó, lớp `ZonePricing` đóng vai trò là **Lớp liên kết nghiệp vụ (Association Class)**, phân rã quan hệ $*..*$ thành 2 quan hệ $1..*$:
     $$\text{Showtime } (1) \longrightarrow (*) \text{ ZonePricing } (*) \longleftarrow (1) \text{ SeatZone}$$
   * Thiết kế này loại bỏ hoàn toàn sự dư thừa liên kết (*Redundant Association*) và phản ánh chính xác nghiệp vụ bán vé theo từng đêm diễn.

4. **Nguyên lý đóng gói hành vi tính toán (Information Expert - GRASP):**
   * Theo nguyên lý *Information Expert*, trách nhiệm tính toán phải được gán cho lớp sở hữu đầy đủ thông tin nhất để thực hiện tính toán đó. Do `RevenueReport` chứa tập hợp các phân khu `ZonePricing` và thuế phí, việc đặt các phương thức `calculateGrossRevenue()`, `calculateNetRevenue()`, `calculateOccupancyRate()` trực tiếp trong `RevenueReport` đảm bảo lớp có cả **Trạng thái (State)** và **Hành vi (Behavior)**, đáp ứng tiêu chuẩn khắt khe của môn học, tránh mô hình *Anemic Domain Model*.

---

## 7. HƯỚNG DẪN NỘP BÀI VÀ THAY ĐỔI THÔNG TIN NHÓM

1. **Tệp tài liệu nộp Thầy Hiển:**
   * Tệp Word chính thức đã nhúng đầy đủ 22 sơ đồ & mockup: **`PTTK/N13 Nhóm 01.docx`** (hoặc `PTTK/N12 Nhóm 01 - HoanChinh.docx`).
   * Thư mục chứa toàn bộ ảnh sơ đồ chất lượng cao (300 DPI): `PTTK/diagrams/`.
2. **Email nhận bài:** `ndhien@hotmail.com`
3. **Tiêu đề email & tên tệp:** `N13<Nhóm Mã số>.docx` hoặc `N12<Nhóm Mã số>.docx` (Ví dụ: `N13 Nhóm 01.docx`).
4. **Cách thay đổi mã nhóm hoặc họ tên thành viên trong 1 câu lệnh:**
   * Mở tệp `generate_word_report.py`, chỉnh sửa thông tin trong mảng `members_data` và `meta_data`.
   * Chạy lệnh `python generate_word_report.py` để sinh lại tệp Word ngay lập tức.
