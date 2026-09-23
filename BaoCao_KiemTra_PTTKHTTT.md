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
| **5** | **Hoàng Văn E** | B21DCCN005 | Thành viên | **Module 5: Quản lý và thống kê dành cho ban tổ chức**<br>• Công cụ vẽ & tạo sơ đồ các khu vực ghế ngồi cho sân khấu<br>• Đăng bài tạo sự kiện mới, quản lý lịch diễn và cấu hình giá vé<br>• Quản lý đợt mở bán vé (Early Bird, Regular) và mã khuyến mãi<br>• Quản lý danh sách check-in và xem báo cáo tổng kết doanh thu |

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

### 2.6. Biểu đồ Use Case Phân hệ 5: Quản lý và thống kê dành cho ban tổ chức

```mermaid
flowchart LR
    Organizer((Ban tổ chức))
    Admin((Quản trị viên))

    subgraph Mod5 ["Phân hệ 5: Quản lý & Thống kê BTC"]
        UC_Layout["Thiết kế & Tạo sơ đồ ghế sân khấu"]
        UC_NewEvent["Đăng bài tạo sự kiện mới"]
        UC_Pricing["Quản lý suất diễn & Cấu hình giá vé"]
        UC_Promo["Thiết lập đợt mở bán & Mã khuyến mãi"]
        UC_Checkin["Quản lý danh sách khách & Soát vé QR"]
        UC_Report["Xem báo cáo thống kê doanh thu"]
        UC_Export["Xuất báo cáo (Excel/PDF)"]
    end

    Organizer --> UC_Layout
    Organizer --> UC_NewEvent
    Organizer --> UC_Pricing
    Organizer --> UC_Promo
    Organizer --> UC_Checkin
    Organizer --> UC_Report

    Admin --> UC_NewEvent
    Admin --> UC_Report

    UC_Export -.->|<<extend>>| UC_Report
```

**Đặc tả tóm tắt Use Case Phân hệ 5:**
* **Thiết kế sơ đồ ghế:** Công cụ Canvas trực quan cho phép BTC dựng khán đài, chia khu vực VIP, CAT 1, CAT 2, vẽ hàng ghế, số ghế và định cấu hình vé ngồi hoặc vé đứng.
* **Tạo sự kiện & Định giá vé:** Nhập mô tả, poster, nghệ sĩ, địa điểm; tạo các suất diễn và gán bảng giá vé cho từng khu vực ghế.
* **Soát vé & Báo cáo:** Ứng dụng quét mã QR tại cửa vào sự kiện xác thực vé hợp lệ trong 1 giây, ngăn chặn vé giả và vé sử dụng lại. Dashboard hiển thị số vé bán, tỷ lệ lấp đầy sân khấu và tổng doanh thu thu được.

---

## 3. BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH CHO HỆ THỐNG VÀ CHO CÁC CHỨC NĂNG

### Nguyên lý lớp phân tích (Analysis Entity Classes)
1. Thể hiện các **khái niệm nghiệp vụ cốt lõi** trong miền bài toán (Domain Model).
2. Mỗi lớp gồm 2 ngăn: **Tên thực thể** và **Danh sách thuộc tính nghiệp vụ thuần túy**.
3. Không phụ thuộc vào kiểu dữ liệu lập trình cụ thể (`int`, `varchar2`, `boolean`...), không có các hàm kỹ thuật `getter/setter`.
4. Thể hiện rõ các mối quan hệ ngữ nghĩa: Kế thừa (Generalization), Kết hợp (Association), Kết tập mạnh (Composition), Kết tập yếu (Aggregation) cùng bản số (Multiplicity).

### 3.1. Biểu đồ lớp thực thể phân tích tổng thể hệ thống

```mermaid
classDiagram
    class NguoiDung {
        maNguoiDung
        hoTen
        email
        soDienThoai
        matKhau
        vaiTro
    }
    class KhachHang {
        diemTichLuy
        hangThanhVien
    }
    class BanToChuc {
        tenToChuc
        maSoThue
        giayPhep
        thongTinMoTa
    }
    class DiaDiem {
        maDiaDiem
        tenDiaDiem
        diaChiChiTiet
        sucChuaToiDa
    }
    class SoDoGhe {
        maSoDo
        tenSoDo
        kieuSanKhau
        tongSoGhe
    }
    class KhuVucGhe {
        maKhuVuc
        tenKhuVuc
        mauSac
        loaiKhuVuc
        soLuongGhe
    }
    class Ghe {
        maGhe
        hangGhe
        soThuTu
        toaDoX
        toaDoY
    }
    class SuKien {
        maSuKien
        tenSuKien
        theLoai
        moTa
        hinhAnh
        trangThai
    }
    class SuatDien {
        maSuatDien
        ngayDien
        thoiGianBatDau
        thoiGianKetThuc
    }
    class GiaVeKhuVuc {
        maGiaVe
        donGia
        soLuongToiDa
    }
    class HangDoiAo {
        maHangDoi
        soThuTu
        thoiGianVao
        trangThaiCho
    }
    class GiuGheTamThoi {
        maGiuGhe
        thoiGianBatDau
        thoiGianHetHan
        trangThai
    }
    class HoaDon {
        maHoaDon
        ngayTao
        tongTien
        soTienGiam
        trangThai
    }

    NguoiDung <|-- KhachHang
    NguoiDung <|-- BanToChuc
    BanToChuc "1" --> "*" SuKien : quản lý
    DiaDiem "1" --> "*" SuKien : tổ chức tại
    DiaDiem "1" --> "*" SoDoGhe : chứa
    SoDoGhe "1" *-- "*" KhuVucGhe : gồm
    KhuVucGhe "1" *-- "*" Ghe : gồm
    SuKien "1" *-- "*" SuatDien : có
    SuatDien "1" --> "*" GiaVeKhuVuc : áp dụng
    KhuVucGhe "1" --> "*" GiaVeKhuVuc : định giá
    KhachHang "1" --> "*" HangDoiAo : tham gia
    HangDoiAo "1" --> "*" GiuGheTamThoi : chuyển tiếp
    GiuGheTamThoi "*" --> "1..*" Ghe : khóa tạm
    KhachHang "1" --> "*" HoaDon : thanh toán
```

---

### 3.2. Biểu đồ lớp phân tích theo từng phân hệ

#### Phân hệ 1: Quản lý tài khoản người dùng
* Các thực thể: `NguoiDung`, `KhachHang`, `BanToChuc`, `PhienDangNhap`, `ThongBao`.
* Quan hệ: Kế thừa từ `NguoiDung`; Khách hàng sở hữu nhiều `PhienDangNhap`; Người dùng nhận nhiều `ThongBao`.

#### Phân hệ 2: Tìm kiếm & Xem sự kiện
* Các thực thể: `SuKien`, `TheLoai`, `DiaDiem`, `SuatDien`, `NgheSi`, `SuKienYeuThich`.
* Quan hệ: Sự kiện thuộc một Thể loại, tổ chức tại một Địa điểm, bao hàm nhiều Suất diễn; Nghệ sĩ biểu diễn tại nhiều Suất diễn; Khách hàng lưu sự kiện vào danh sách Yêu thích.

#### Phân hệ 3: Xếp hàng và chọn chỗ
* Các thực thể: `SoDoGhe`, `KhuVucGhe`, `Ghe`, `KhachHang`, `HangDoiAo`, `GiuGheTamThoi`.
* Quan hệ: Cấu trúc phân cấp chứa `SoDoGhe` -> `KhuVucGhe` -> `Ghe`; Khách hàng vào `HangDoiAo`; Khi đến lượt tạo bản ghi `GiuGheTamThoi` liên kết với danh sách các `Ghe` đã chọn.

#### Phân hệ 4: Tính tiền và Xuất vé
* Các thực thể: `HoaDon`, `Ve`, `MaGiamGia`, `GiaoDichThanhToan`, `KhachHang`, `Ghe`.
* Quan hệ: `HoaDon` do `KhachHang` lập, áp dụng 0..1 `MaGiamGia`, thanh toán qua 1 `GiaoDichThanhToan`, và bao hàm 1..* `Ve`. Mỗi `Ve` được gán cố định cho 1 `Ghe`.

#### Phân hệ 5: Quản lý và thống kê dành cho BTC
* Các thực thể: `BanToChuc`, `SuKien`, `SuatDien`, `SoDoGhe`, `KhuVucGhe`, `GiaVeKhuVuc`, `BaoCaoDoanhThu`.
* Quan hệ: Ban tổ chức quản lý Sự kiện; Sự kiện liên kết Sơ đồ ghế và Suất diễn; Suất diễn định giá qua `GiaVeKhuVuc` và kết xuất `BaoCaoDoanhThu`.

---

## 4. BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ CHO HỆ THỐNG VÀ CHO CÁC CHỨC NĂNG

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

#### Phân hệ 5: Quản lý và thống kê dành cho ban tổ chức (Classes: Organizer, ZonePricing, RevenueReport)
| Lớp thiết kế | Thuộc tính chi tiết (Kiểu dữ liệu & Ràng buộc) | Phương thức nghiệp vụ (Operations) |
|:---|:---|:---|
| **Organizer** | `- id: Long [PK]`<br>`- companyName: String`<br>`- taxId: String`<br>`- email: String` | `+ createEvent(dto: EventDto): Event`<br>`+ updatePricing(pricingDto): void`<br>`+ viewReports(eventId: Long): RevenueReport` |
| **ZonePricing** | `- id: Long [PK]`<br>`- price: double [>= 0]`<br>`- maxQuota: int`<br>`- soldCount: int` | `+ isSoldOut(): boolean`<br>`+ recordSale(qty: int): void`<br>`+ getRemainingQuota(): int` |
| **RevenueReport**| `- id: Long [PK]`<br>`- totalTicketsSold: int`<br>`- grossRevenue: double`<br>`- occupancyRate: double [0.0 - 100.0%]`<br>`- generatedAt: LocalDateTime` | `+ exportExcel(): byte[]`<br>`+ exportPdf(): byte[]`<br>`+ calculateRevenueByZone(): Map` |

---

## 5. HƯỚNG DẪN NỘP BÀI VÀ THAY ĐỔI THÔNG TIN NHÓM

1. **Tệp tài liệu nộp Thầy Hiển:**
   * Tệp Word đã hoàn chỉnh sẵn sàng để gửi: **`PTTK/N12 Nhóm 01 - HoanChinh.docx`** (hoặc bạn có thể đóng ứng dụng Microsoft Word đang mở và đổi tên thành `N12 Nhóm 01.docx`).
   * Thư mục chứa toàn bộ 18 ảnh sơ đồ chất lượng cao (300 DPI): `PTTK/diagrams/`.
2. **Email nhận bài:** `ndhien@hotmail.com`
3. **Tiêu đề email & tên tệp:** `N12<Nhóm Mã số>.docx` (Ví dụ: `N12 Nhóm 01.docx`).
4. **Cách thay đổi mã nhóm hoặc họ tên thành viên trong 1 câu lệnh:**
   * Mở tệp `generate_word_report.py`, chỉnh sửa thông tin trong mảng `members_data` và `meta_data`.
   * Chạy lệnh `python generate_word_report.py` để sinh lại tệp Word ngay lập tức.
