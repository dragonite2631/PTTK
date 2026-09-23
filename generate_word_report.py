import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIAGRAMS_DIR = os.path.join(BASE_DIR, "diagrams")
DOCX_OUT = os.path.join(BASE_DIR, "N12 Nhóm 01.docx")

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="8" w:space="0" w:color="1E3A8A"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def add_styled_table(doc, headers, data, col_widths=None):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)

    # Header row
    hdr_cells = table.rows[0].cells
    for i, h_text in enumerate(headers):
        hdr_cells[i].text = h_text
        set_cell_background(hdr_cells[i], "1E3A8A")
        set_cell_margins(hdr_cells[i], top=140, bottom=140, left=160, right=160)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.name = "Times New Roman"
            run.font.size = Pt(10.5)
            run.font.bold = True
            run.font.color.rgb = RGBColor(255, 255, 255)

    # Data rows
    for r_idx, row_data in enumerate(data):
        row_cells = table.rows[r_idx + 1].cells
        bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=100, bottom=100, left=140, right=140)
            p = row_cells[c_idx].paragraphs[0]
            if c_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.name = "Times New Roman"
                run.font.size = Pt(10)
                run.font.color.rgb = RGBColor(30, 41, 59)

    # Set column widths
    if col_widths:
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = Inches(width)

    # Spacing after table
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(6)

def add_heading_1(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(16)
    h.paragraph_format.space_after = Pt(6)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 58, 138) # Navy #1E3A8A
    return h

def add_heading_2(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(29, 78, 216) # Royal Blue #1D4ED8
    return h

def add_heading_3(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(8)
    h.paragraph_format.space_after = Pt(3)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.italic = True
    run.font.color.rgb = RGBColor(51, 65, 85) # Slate #334155
    return h

def add_body_p(doc, text, bold_prefix=""):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.25
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(15, 23, 42)
    r_text = p.add_run(text)
    r_text.font.name = "Times New Roman"
    r_text.font.size = Pt(11.5)
    r_text.font.color.rgb = RGBColor(30, 41, 59)
    return p

def add_bullet_p(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.2
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(15, 23, 42)
    r_text = p.add_run(text)
    r_text.font.name = "Times New Roman"
    r_text.font.size = Pt(11)
    r_text.font.color.rgb = RGBColor(30, 41, 59)
    return p

def add_diagram_image(doc, filename, caption_text):
    path = os.path.join(DIAGRAMS_DIR, filename)
    if not os.path.exists(path):
        print(f"Warning: image {path} does not exist!")
        return
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(8)
    p_img.paragraph_format.space_after = Pt(2)
    p_img.paragraph_format.keep_with_next = True
    run_img = p_img.add_run()
    run_img.add_picture(path, width=Inches(6.2))

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(10)
    run_cap = p_cap.add_run(caption_text)
    run_cap.font.name = "Times New Roman"
    run_cap.font.size = Pt(10)
    run_cap.font.italic = True
    run_cap.font.bold = True
    run_cap.font.color.rgb = RGBColor(71, 85, 105)

def build_full_docx():
    doc = docx.Document()

    # Page setup - Margins: Top 2cm, Bottom 2cm, Left 3cm, Right 2cm
    section = doc.sections[0]
    section.top_margin = Inches(0.79)    # 2.0 cm
    section.bottom_margin = Inches(0.79) # 2.0 cm
    section.left_margin = Inches(1.18)   # 3.0 cm
    section.right_margin = Inches(0.79)  # 2.0 cm

    # Document Header block
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(2)
    r = p_inst.add_run("HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG\nKHOA CÔNG NGHỆ THÔNG TIN")
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(30, 41, 59)

    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_after = Pt(14)
    r_line = p_line.add_run("------------------***------------------")
    r_line.font.bold = True
    r_line.font.color.rgb = RGBColor(148, 163, 184)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(6)
    r_t = p_title.add_run("BÀI KIỂM TRA ĐỊNH KỲ\nPHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG THÔNG TIN")
    r_t.font.name = "Times New Roman"
    r_t.font.size = Pt(16)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(190, 18, 60) # Dark Red / Crimson

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(18)
    r_sub = p_sub.add_run("ĐỀ TÀI: XÂY DỰNG HỆ THỐNG ĐẶT VÉ THAM GIA SỰ KIỆN TRỰC TUYẾN")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(13)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(30, 58, 138)

    # Meta table
    meta_headers = ["Thông tin", "Chi tiết"]
    meta_data = [
        ["Lớp học phần", "N12"],
        ["Mã số nhóm", "Nhóm 01 (Sinh viên có thể thay số nhóm tương ứng)"],
        ["Giảng viên giảng dạy", "TS. Nguyễn Đức Hiển"],
        ["Email tiếp nhận bài", "ndhien@hotmail.com"],
        ["Tên file nộp bài", "N12 Nhóm 01.docx"]
    ]
    add_styled_table(doc, meta_headers, meta_data, col_widths=[2.0, 4.2])

    # =========================================================================
    # PHẦN 1
    # =========================================================================
    add_heading_1(doc, "1. MÃ SỐ NHÓM, TÊN ĐỀ TÀI, HỌ TÊN CÁC THÀNH VIÊN – CHỨC NĂNG")
    
    add_body_p(doc, "Xây dựng Hệ thống đặt vé tham gia sự kiện trực tuyến (Online Event Ticket Booking System)", "Tên đề tài: ")
    add_body_p(doc, "Nhóm 01 - Lớp tín chỉ: N12", "Mã số nhóm: ")
    add_body_p(doc, "Hệ thống phục vụ toàn diện nhu cầu bán vé các sự kiện âm nhạc (Concert), thể thao, hội thảo và biểu diễn nghệ thuật. Hệ thống giải quyết bài toán tải lớn khi mở bán thông qua phòng chờ ảo (Virtual Waiting Queue), sơ đồ ghế trực quan theo thời gian thực (Interactive Real-time Seat Map), khóa giữ ghế tạm thời, thanh toán đa kênh và cấp phát vé điện tử QR Code chống gian lận.", "Mô tả tổng quan: ")

    add_body_p(doc, "Dưới đây là bảng phân công nhiệm vụ và trách nhiệm cụ thể của từng thành viên tương ứng với 5 phân hệ (module) chính của bài tập môn học:")

    members_headers = ["STT", "Họ và tên", "Mã sinh viên", "Vai trò", "Chức năng / Module phụ trách"]
    members_data = [
        ["1", "Nguyễn Văn A", "B21DCCN001", "Nhóm trưởng", "Module 1: Quản lý tài khoản người dùng\n- Đăng ký, đăng nhập tài khoản, bảo mật phân quyền\n- Đổi mật khẩu, khôi phục mật khẩu quên qua Email OTP\n- Chỉnh sửa hồ sơ cá nhân, cài đặt thông báo"],
        ["2", "Trần Thị B", "B21DCCN002", "Thành viên", "Module 2: Tìm kiếm & Xem sự kiện\n- Trang chủ hiển thị sự kiện nổi bật, thịnh hành\n- Tìm kiếm, lọc sự kiện đa tiêu chí (ngày, địa điểm, thể loại)\n- Chi tiết sự kiện, dàn nghệ sĩ biểu diễn, lưu yêu thích"],
        ["3", "Lê Văn C", "B21DCCN003", "Thành viên", "Module 3: Xếp hàng và chọn chỗ\n- Hàng đợi ảo thông minh (Virtual Queue) khi lưu lượng cao\n- Hiển thị sơ đồ ghế sân khấu thời gian thực (Real-time Seat Map)\n- Chọn vị trí ghế, khóa ghế tạm thời (Hold Timer 10-15 phút)"],
        ["4", "Phạm Thị D", "B21DCCN004", "Thành viên", "Module 4: Tính tiền và Xuất vé\n- Tạo đơn hàng mua vé, áp dụng mã voucher khuyến mãi\n- Tích hợp cổng thanh toán trực tuyến (VNPAY, Ví MoMo, Thẻ ATM/Visa)\n- Tạo vé điện tử mã QR Code động, gửi vé qua Email"],
        ["5", "Hoàng Văn E", "B21DCCN005", "Thành viên", "Chức năng 5: Xem thống kê doanh thu sự kiện\n- Tiếp nhận yêu cầu tra cứu từ Ban tổ chức\n- Tính toán các chỉ số KPIs (Gross/Net Revenue, Occupancy Rate)\n- Phân tích tỷ trọng đóng góp doanh thu theo từng phân khu khán đài\n- Kết xuất báo cáo thống kê trực quan (dashboard & file)"]
    ]
    add_styled_table(doc, members_headers, members_data, col_widths=[0.5, 1.3, 1.1, 1.0, 2.6])

    # =========================================================================
    # PHẦN 2
    # =========================================================================
    add_heading_1(doc, "2. BIỂU ĐỒ USE CASE CHO HỆ THỐNG VÀ CHO CÁC CHỨC NĂNG")
    
    add_heading_2(doc, "2.1. Biểu đồ Use Case tổng thể toàn hệ thống")
    add_body_p(doc, "Biểu đồ Use Case tổng quát mô tả toàn bộ ranh giới của Hệ thống đặt vé tham gia sự kiện trực tuyến, bao gồm các tác nhân (Actors) chính và các nhóm chức năng tương ứng:")
    add_bullet_p(doc, "Người dùng tìm kiếm, chọn ghế, thanh toán vé và quản lý vé cá nhân.", "Khách hàng (Customer): ")
    add_bullet_p(doc, "Đơn vị tổ chức thiết kế sơ đồ ghế, đăng sự kiện, cấu hình giá vé và theo dõi doanh thu.", "Ban tổ chức (Organizer): ")
    add_bullet_p(doc, "Kiểm duyệt sự kiện, quản lý tài khoản người dùng và giám sát hệ thống.", "Quản trị viên (Administrator): ")
    add_bullet_p(doc, "Hệ thống thanh toán trực tuyến xử lý giao dịch tiền tệ (VNPAY, MoMo, Visa/Mastercard).", "Cổng thanh toán (Payment Gateway - External): ")
    add_bullet_p(doc, "Dịch vụ bên ngoài gửi mã xác thực OTP, email hóa đơn và vé điện tử đính kèm QR Code.", "Dịch vụ Email / SMS (Notification Service - External): ")

    add_diagram_image(doc, "uc_tong_the.png", "Hình 2.1: Biểu đồ Use Case tổng thể Hệ thống Đặt vé tham gia sự kiện")

    # Module 1
    add_heading_2(doc, "2.2. Biểu đồ Use Case Phân hệ 1: Quản lý tài khoản người dùng")
    add_body_p(doc, "Phân hệ đảm nhiệm việc xác thực và định danh người dùng trong toàn hệ thống. Hỗ trợ đầy đủ các nghiệp vụ đăng ký, đăng nhập an toàn, cơ chế khôi phục mật khẩu qua mã xác nhận OTP/Token, cập nhật hồ sơ và tùy chỉnh nhận thông báo.")
    add_diagram_image(doc, "uc_module1.png", "Hình 2.2: Biểu đồ Use Case Phân hệ 1 - Quản lý tài khoản người dùng")

    uc1_headers = ["Use Case", "Tác nhân", "Mô tả nghiệp vụ", "Quan hệ Use Case"]
    uc1_data = [
        ["Đăng ký tài khoản", "Khách hàng, Organizer", "Người dùng điền thông tin (họ tên, email, mật khẩu, SĐT) để tạo tài khoản mới.", "<<include>> Gửi mã OTP xác nhận email"],
        ["Đăng nhập", "Người dùng", "Xác thực bằng Email/Username và Mật khẩu. Hỗ trợ ghi nhớ phiên đăng nhập qua JWT.", "<<extend>> Khóa tài khoản tạm thời khi nhập sai quá 5 lần"],
        ["Đổi mật khẩu", "Người dùng đã đăng nhập", "Người dùng cung cấp mật khẩu cũ và nhập mật khẩu mới hợp lệ để cập nhật.", "Không"],
        ["Quên / Lấy lại MK", "Khách hàng, Organizer", "Nhập email đã đăng ký để nhận mã OTP hoặc đường dẫn thiết lập lại mật khẩu mới.", "<<include>> Gửi link reset mật khẩu qua email"],
        ["Chỉnh sửa thông tin", "Người dùng đã đăng nhập", "Cập nhật thông tin cá nhân: họ tên, ảnh đại diện, số điện thoại liên hệ.", "Không"],
        ["Cài đặt thông báo", "Khách hàng", "Bật/tắt các loại thông báo sự kiện, ưu đãi mở bán vé qua Email hoặc Web Push.", "Không"]
    ]
    add_styled_table(doc, uc1_headers, uc1_data, col_widths=[1.5, 1.2, 2.3, 1.5])

    # Module 2
    add_heading_2(doc, "2.3. Biểu đồ Use Case Phân hệ 2: Tìm kiếm & Xem sự kiện")
    add_body_p(doc, "Phân hệ giúp người dùng khám phá và tìm kiếm sự kiện một cách nhanh chóng, trực quan. Người dùng có thể tìm kiếm theo từ khóa, lọc đa tiêu chí (ngày diễn, địa điểm, thể loại nhạc/kịch/thể thao, mức giá), xem chi tiết thông tin sự kiện cùng dàn nghệ sĩ tham gia, và lưu vào danh sách yêu thích.")
    add_diagram_image(doc, "uc_module2.png", "Hình 2.3: Biểu đồ Use Case Phân hệ 2 - Tìm kiếm & Xem sự kiện")

    uc2_headers = ["Use Case", "Tác nhân", "Mô tả nghiệp vụ", "Quan hệ Use Case"]
    uc2_data = [
        ["Xem sự kiện nổi bật", "Khách hàng", "Hiển thị banner các sự kiện 'Hot', sự kiện sắp mở bán vé hoặc đang bán chạy.", "Không"],
        ["Tìm kiếm sự kiện", "Khách hàng", "Tìm kiếm sự kiện theo tên sự kiện, tên ca sĩ, ban nhạc hoặc địa điểm biểu diễn.", "Không"],
        ["Lọc sự kiện", "Khách hàng", "Lọc theo nhiều tiêu chí kết hợp: Khoảng thời gian, Khu vực (Hà Nội, TP.HCM...), Thể loại, Mức giá.", "Không"],
        ["Xem chi tiết sự kiện", "Khách hàng", "Xem mô tả chi tiết, lịch diễn, danh sách nghệ sĩ, sơ đồ sân khấu và bảng giá vé.", "Không"],
        ["Lưu sự kiện yêu thích", "Khách hàng (đăng nhập)", "Thêm sự kiện vào Wishlist để theo dõi trạng thái và nhận thông báo khi mở bán.", "<<extend>> Nhận thông báo khi mở bán vé"],
        ["Chia sẻ sự kiện", "Khách hàng", "Tạo liên kết chia sẻ sự kiện lên các nền tảng mạng xã hội (Facebook, Zalo, X).", "Không"]
    ]
    add_styled_table(doc, uc2_headers, uc2_data, col_widths=[1.5, 1.2, 2.3, 1.5])

    # Module 3
    add_heading_2(doc, "2.4. Biểu đồ Use Case Phân hệ 3: Xếp hàng và chọn chỗ")
    add_body_p(doc, "Phân hệ trọng yếu đảm bảo hệ thống không bị sập (crash) khi có hàng chục nghìn lượt truy cập đồng thời vào giờ mở bán vé. Cơ chế phòng chờ ảo (Virtual Waiting Room) cấp số thứ tự công bằng, khi tới lượt người mua được chuyển vào màn hình chọn ghế trực quan với đồng hồ đếm ngược giữ ghế tạm thời (10-15 phút).")
    add_diagram_image(doc, "uc_module3.png", "Hình 2.4: Biểu đồ Use Case Phân hệ 3 - Xếp hàng và chọn chỗ")

    uc3_headers = ["Use Case", "Tác nhân", "Mô tả nghiệp vụ", "Quan hệ Use Case"]
    uc3_data = [
        ["Vào hàng đợi ảo", "Khách hàng, Queue System", "Khi sự kiện có tải vượt ngưỡng, hệ thống đưa người mua vào hàng đợi với số thứ tự duy nhất.", "Không"],
        ["Theo dõi tiến trình chờ", "Khách hàng", "Hiển thị số người phía trước và thời gian ước tính; tự động cấp Access Token khi tới lượt.", "Không"],
        ["Xem sơ đồ sân khấu", "Khách hàng", "Tải bản đồ ghế trực quan với màu sắc thể hiện trạng thái: Trống, Đang giữ, Đã bán theo thời gian thực.", "Không"],
        ["Chọn vị trí ghế ngồi", "Khách hàng", "Người dùng nhấn chọn ghế trên sơ đồ (theo khu vực: VIP, Standard, Fan Zone...).", "Không"],
        ["Giữ ghế tạm thời", "Khách hàng, Timer Service", "Khóa các ghế đã chọn trong 10-15 phút, hiển thị đồng hồ đếm ngược để người dùng thanh toán.", "<<extend>> Giải phóng ghế khi hết hạn giữ chỗ"],
        ["Hủy chọn / Thoát chờ", "Khách hàng", "Người dùng chủ động hủy các ghế đang giữ hoặc thoát khỏi hàng đợi.", "Không"]
    ]
    add_styled_table(doc, uc3_headers, uc3_data, col_widths=[1.5, 1.2, 2.3, 1.5])

    # Module 4
    add_heading_2(doc, "2.5. Biểu đồ Use Case Phân hệ 4: Tính tiền và Xuất vé")
    add_body_p(doc, "Phân hệ xử lý thanh toán tài chính và cấp phát vé. Sau khi chọn ghế, đơn hàng được khởi tạo, cho phép nhập mã khuyến mãi, chọn cổng thanh toán phù hợp, hoàn tất thanh toán an toàn và sinh mã vé điện tử QR Code động gửi thẳng tới Email khách hàng.")
    add_diagram_image(doc, "uc_module4.png", "Hình 2.5: Biểu đồ Use Case Phân hệ 4 - Tính tiền và Xuất vé")

    uc4_headers = ["Use Case", "Tác nhân", "Mô tả nghiệp vụ", "Quan hệ Use Case"]
    uc4_data = [
        ["Tạo đơn hàng mua vé", "Khách hàng", "Tổng hợp thông tin các ghế đang giữ, tính tiền tạm tính và tạo mã đơn hàng.", "Không"],
        ["Nhập mã giảm giá", "Khách hàng", "Nhập Voucher ưu đãi; hệ thống kiểm tra điều kiện áp dụng và trừ tiền tương ứng.", "<<include>> Kiểm tra hợp lệ mã voucher"],
        ["Chọn kênh thanh toán", "Khách hàng", "Lựa chọn phương thức: Cổng VNPAY-QR, Ví điện tử MoMo, Thẻ ATM/Visa/MasterCard.", "Không"],
        ["Thanh toán trực tuyến", "Khách hàng, Cổng thanh toán", "Chuyển hướng cổng thanh toán, xác thực OTP ngân hàng và xử lý giao dịch thành công.", "<<include>> Xác thực OTP & Kết quả giao dịch"],
        ["Xuất vé điện tử QR", "Hệ thống, Mail Service", "Sinh mã QR Code được mã hóa chữ ký số (chống làm giả) cho từng ghế trong đơn hàng.", "Không"],
        ["Lưu vào 'Vé của tôi'", "Khách hàng", "Vé điện tử được lưu trữ vĩnh viễn trong tài khoản người dùng để phục vụ soát vé (Check-in).", "Không"]
    ]
    add_styled_table(doc, uc4_headers, uc4_data, col_widths=[1.5, 1.2, 2.3, 1.5])

    # Module 5 - Focused Single Feature
    add_heading_2(doc, "2.6. Biểu đồ Use Case Chức năng 5: Xem thống kê doanh thu sự kiện")
    add_body_p(doc, "Trong bài tập môn học, thành viên 5 phụ trách chuyên sâu chức năng nghiệp vụ đơn lẻ 'Xem thống kê doanh thu sự kiện' (View Event Revenue Statistics). Biểu đồ Use Case phân rã chi tiết dưới đây làm rõ các ca sử dụng bao hàm (<<include>>) bắt buộc để thực hiện tính toán tài chính và các ca sử dụng mở rộng (<<extend>>) phục vụ lọc và kết xuất báo cáo:")
    add_diagram_image(doc, "uc_m5_view_revenue_detail.png", "Hình 2.6: Biểu đồ Use Case chi tiết - Chức năng Xem thống kê doanh thu sự kiện")

    uc5_headers = ["Use Case", "Tác nhân", "Mô tả nghiệp vụ", "Quan hệ Use Case"]
    uc5_data = [
        ["Xem thống kê doanh thu sự kiện", "Ban tổ chức, Admin", "Ca sử dụng trung tâm: tiếp nhận yêu cầu, tổng hợp và hiển thị toàn bộ báo cáo doanh thu sự kiện.", "Chức năng chính"],
        ["Chọn sự kiện cần thống kê", "Ban tổ chức, Admin", "Chọn sự kiện cụ thể từ danh sách sự kiện do ban tổ chức quản lý để nạp dữ liệu.", "<<include>> Bắt buộc thực hiện trước khi xem"],
        ["Tính toán chỉ số KPIs", "Hệ thống (RevenueReport)", "Thực hiện chuỗi phương thức tính toán: doanh thu gộp, doanh thu thuần, tỷ lệ lấp đầy, giá vé bình quân.", "<<include>> Bắt buộc để có dữ liệu báo cáo"],
        ["Lọc theo suất diễn & ngày", "Ban tổ chức", "Tùy chọn lọc thu hẹp phạm vi thống kê theo từng suất diễn cụ thể hoặc một khoảng ngày mở bán.", "<<extend>> Mở rộng theo nhu cầu"],
        ["Xem phân bổ theo phân khu", "Ban tổ chức", "Xem biểu đồ và bảng phân tích chi tiết tỷ trọng đóng góp doanh thu của từng phân khu (VIP, Regular, Stand).", "<<extend>> Mở rộng phân tích sâu"],
        ["Xuất báo cáo (Excel / PDF)", "Ban tổ chức, Admin", "Kết xuất toàn bộ dữ liệu thống kê ra tệp bảng tính Excel hoặc tài liệu PDF ngoại tuyến.", "<<extend>> Mở rộng khi cần lưu tệp"]
    ]
    add_styled_table(doc, uc5_headers, uc5_data, col_widths=[1.6, 1.2, 2.3, 1.4])

    # =========================================================================
    # PHẦN 3: KỊCH BẢN PHÂN TÍCH CHO CÁC CHỨC NĂNG
    # =========================================================================
    add_heading_1(doc, "3. KỊCH BẢN PHÂN TÍCH CHO CÁC CHỨC NĂNG (SCENARIO)")
    add_body_p(doc, "Dưới đây là kịch bản phân tích chi tiết (Scenario) được xây dựng theo chuẩn mẫu phân tích yêu cầu phần mềm dành riêng cho chức năng đơn lẻ trọng tâm: Chức năng 5 - Xem thống kê doanh thu sự kiện (View Event Revenue Statistics):")

    sc_headers = ["Mục kịch bản", "Nội dung đặc tả chi tiết"]
    sc_data = [
        ["Tên use case", "XemThongKeDoanhThuSuKien (ViewEventRevenueStatistics)"],
        ["Tác nhân chính", "Ban tổ chức sự kiện (Organizer), Quản trị viên (Admin)"],
        ["Tiền điều kiện", "Khi người dùng muốn xem báo cáo thống kê doanh thu phải đăng nhập thành công vào hệ thống với vai trò Ban tổ chức hoặc Quản trị viên.\nSự kiện đã được khởi tạo, cấu hình phân khu giá vé và đã mở bán vé (phát sinh dữ liệu đơn hàng)."],
        ["Đảm bảo tối thiểu", "Hệ thống hiển thị thông báo sự kiện chưa có dữ liệu hoặc lỗi kết nối, giữ nguyên giao diện để người dùng chọn lại sự kiện khác."],
        ["Đảm bảo thành công", "Hệ thống tổng hợp, tính toán đầy đủ và hiển thị chính xác các chỉ số tài chính (Tổng doanh thu gộp, Doanh thu thuần sau thuế và phí, Tỷ lệ lấp đầy khán đài, Giá vé bình quân, Đánh giá hiệu suất) cùng bảng biểu chi tiết và biểu đồ phân bổ doanh thu theo từng phân khu."],
        ["Kích hoạt", "Người dùng chọn chức năng 'Xem thống kê doanh thu sự kiện' trên thanh menu/bảng điều khiển hệ thống."],
        ["Chuỗi sự kiện chính:", 
         "1. Người dùng chọn chức năng 'Xem thống kê doanh thu sự kiện' từ menu điều hướng của hệ thống.\n"
         "2. Hệ thống hiển thị Form thống kê: yêu cầu người dùng chọn sự kiện từ danh sách sự kiện đang quản lý (eventSelector) và tùy chọn khoảng thời gian lọc (datePicker).\n"
         "3. Người dùng chọn sự kiện cần xem từ danh sách, chọn khoảng thời gian tra cứu và nhấn nút 'Tra cứu'.\n"
         "4. Hệ thống kiểm tra dữ liệu sự kiện, nạp danh sách các phân khu vé (ZonePricing), các suất diễn (Showtime) và các hóa đơn vé đã thanh toán thành công.\n"
         "5. Hệ thống thực hiện chuỗi phương thức tính toán tài chính nội tại:\n"
         "   - Tính tổng sức chứa phát hành: calculateTotalCapacity()\n"
         "   - Tính tổng số vé đã bán thành công: calculateTotalTicketsSold()\n"
         "   - Tính tổng doanh thu bán vé gộp: calculateGrossRevenue()\n"
         "   - Khấu trừ 10% VAT và 5% phí sàn để tính doanh thu thuần: calculateNetRevenue()\n"
         "   - Tính tỷ lệ lấp đầy khán đài: calculateOccupancyRate()\n"
         "   - Tính giá vé bình quân mỗi vé bán ra: calculateAverageTicketPrice()\n"
         "   - Tính tỷ trọng đóng góp doanh thu của từng phân khu: calculateZoneContribution(zoneId)\n"
         "   - Đánh giá xếp hạng hiệu quả mở bán: evaluatePerformance()\n"
         "6. Hệ thống hiển thị toàn bộ các thẻ KPI chỉ số tài chính, bảng chi tiết từng phân khu vé và vẽ biểu đồ tỷ trọng phân bổ doanh thu trực quan."],
        ["Ngoại lệ:", 
         "4.a. Sự kiện được chọn chưa có giao dịch bán vé nào phát sinh trong khoảng thời gian tra cứu\n"
         "     4.a.1. Hệ thống hiển thị thông báo: 'Sự kiện chưa phát sinh giao dịch bán vé'\n"
         "     4.a.2. Hiển thị các chỉ số ở mức mặc định (0 VNĐ, 0%) và cho phép người dùng chọn lại sự kiện khác.\n"
         "4.b. Người dùng nhập khoảng thời gian lọc không hợp lệ (Ngày bắt đầu > Ngày kết thúc)\n"
         "     4.b.1. Hệ thống hiển thị thông báo lỗi: 'Khoảng thời gian tra cứu không hợp lệ'\n"
         "     4.b.2. Đặt lại khoảng thời gian mặc định là toàn bộ thời gian mở bán của sự kiện.\n"
         "4.c. Lỗi kết nối máy chủ cơ sở dữ liệu hoặc hệ thống tính toán\n"
         "     4.c.1. Hệ thống hiển thị thông báo: 'Lỗi kết xuất dữ liệu thống kê, vui lòng thử lại sau'\n"
         "     4.c.2. Giữ nguyên giao diện ban đầu."]
    ]
    add_styled_table(doc, sc_headers, sc_data, col_widths=[2.0, 4.5])

    # =========================================================================
    # PHẦN 4: KỊCH BẢN VÀ THIẾT KẾ GIAO DIỆN CHO CÁC CHỨC NĂNG
    # =========================================================================
    add_heading_1(doc, "4. KỊCH BẢN VÀ THIẾT KẾ GIAO DIỆN CHO CÁC CHỨC NĂNG")
    add_body_p(doc, "Thiết kế giao diện cho Chức năng 5: Xem thống kê doanh thu sự kiện được xây dựng nhằm cung cấp trải nghiệm phân tích tài chính trực quan, rõ ràng và tức thì cho Ban tổ chức.")

    add_heading_2(doc, "4.1. Bảng đặc tả các thành phần giao diện (UI Controls Specification)")
    ui_ctrl_headers = ["Mã thành phần", "Tên thành phần", "Kiểu điều khiển (Type)", "Ý nghĩa & Ràng buộc dữ liệu"]
    ui_ctrl_data = [
        ["cb_event", "Chọn sự kiện", "ComboBox (Dropdown)", "Danh sách các sự kiện do ban tổ chức quản lý. Ràng buộc: bắt buộc chọn 1 sự kiện."],
        ["dp_from_date", "Từ ngày", "DatePicker / TextInput", "Ngày bắt đầu lọc số liệu. Định dạng: DD/MM/YYYY. Mặc định: ngày mở bán vé."],
        ["dp_to_date", "Đến ngày", "DatePicker / TextInput", "Ngày kết thúc lọc số liệu. Định dạng: DD/MM/YYYY. Ràng buộc: >= dp_from_date."],
        ["btn_search", "Tra cứu", "Button (Primary)", "Kích hoạt gửi yêu cầu tra cứu và tính toán số liệu thống kê."],
        ["btn_excel", "Xuất Excel", "Button (Success)", "Kết xuất toàn bộ bảng số liệu phân tích ra tệp bảng tính .xlsx."],
        ["btn_pdf", "In PDF", "Button (Danger)", "Tạo tài liệu báo cáo định dạng .pdf chuẩn hóa để in ấn hoặc ký duyệt."],
        ["card_gross", "Tổng doanh thu gộp", "KPI Card (Blue)", "Hiển thị tổng số tiền bán vé thu được trước thuế phí."],
        ["card_net", "Doanh thu thuần", "KPI Card (Green)", "Hiển thị số tiền thực nhận sau khi khấu trừ 10% VAT và 5% phí nền tảng."],
        ["card_occupancy", "Tỷ lệ lấp đầy", "KPI Card (Amber)", "Hiển thị phần trăm số ghế đã bán trên tổng sức chứa và xếp hạng (EXCELLENT)."],
        ["card_avg_price", "Giá vé bình quân", "KPI Card (Purple)", "Hiển thị giá bán trung bình trên mỗi vé thành công."],
        ["chart_zone", "Biểu đồ phân khu", "Donut / Pie Chart", "Biểu đồ trực quan tỷ trọng đóng góp doanh thu của từng phân khu vé."],
        ["tbl_breakdown", "Bảng chi tiết phân khu", "Data Table", "Liệt kê chi tiết từng phân khu: Đơn giá, Chỉ tiêu, Đã bán, Tỷ lệ lấp đầy, Thành tiền, Tỷ trọng."]
    ]
    add_styled_table(doc, ui_ctrl_headers, ui_ctrl_data, col_widths=[1.3, 1.4, 1.4, 2.4])

    add_heading_2(doc, "4.2. Kịch bản tương tác giao diện chi tiết (UI Storyboard Scenario)")
    add_body_p(doc, "Kịch bản tương tác giao diện mô tả chi tiết từng bước hành động của người dùng trên màn hình RevenueReportView, sự kiện kích hoạt, cách thức hệ thống xử lý nghiệp vụ và phản hồi hiển thị tương ứng:")

    ui_flow_headers = ["Bước", "Hành động của tác nhân (User Action)", "Sự kiện UI (Event)", "Xử lý hệ thống & Phản hồi giao diện (System Response)", "Trạng thái giao diện tiếp theo (Next State)"]
    ui_flow_data = [
        ["1", 
         "Người dùng nhấp chọn mục 'Thống kê doanh thu' trên menu điều khiển.", 
         "OnClick (Menu_ThongKe)", 
         "Hệ thống gọi API lấy danh sách các sự kiện đang hoạt động. Khởi tạo màn hình RevenueReportView, nạp danh sách sự kiện vào ComboBox (cb_event), đặt khoảng ngày tra cứu mặc định là 30 ngày gần nhất.", 
         "Màn hình hiển thị trống (Ready): Bộ lọc sẵn sàng, các thẻ KPI và bảng biểu ở trạng thái chờ."],
        ["2", 
         "Người dùng nhấp vào ComboBox cb_event và chọn sự kiện 'Born Pink World Tour Hanoi 2026'.", 
         "OnSelectionChange (cb_event)", 
         "Hệ thống ghi nhận mã sự kiện eventId, tự động truy vấn khoảng thời gian diễn ra sự kiện trong CSDL và điền sẵn vào 2 ô DatePicker dp_from_date và dp_to_date.", 
         "Đã nạp bộ lọc (Configured): ComboBox hiển thị sự kiện đã chọn, các ô ngày hiển thị khoảng ngày của sự kiện."],
        ["3", 
         "Người dùng điều chỉnh ô ngày và nhấp chuột vào nút 'Tra cứu' (btn_search).", 
         "OnClick (btn_search)", 
         "Giao diện vô hiệu hóa tạm thời bộ lọc (disable cb_event, btn_search) và hiển thị vòng xoay tải dữ liệu (loading spinner). Gửi yêu cầu truy vấn tài chính tới RevenueReportController.", 
         "Đang xử lý (Loading): Biểu tượng xoay hiển thị, người dùng không thể nhấp lại nút tra cứu."],
        ["4", 
         "Hệ thống thực hiện tính toán tài chính thành công và trả về RevenueSummaryDto.", 
         "OnDataLoaded (Success Callback)", 
         "Ẩn biểu tượng xoay tải dữ liệu, kích hoạt lại bộ lọc. Nạp các giá trị số liệu vào 4 thẻ KPI; vẽ biểu đồ tròn Donut tỷ trọng phân khu; điền đầy đủ dữ liệu phân tích chi tiết vào bảng breakdown table.", 
         "Hiển thị báo cáo (Rendered): Toàn bộ số liệu doanh thu, biểu đồ phân khu và bảng phân tích chi tiết được hiển thị sắc nét."],
        ["5", 
         "Người dùng di chuyển con trỏ chuột vào vùng phân khu 'VIP' trên biểu đồ tròn Donut.", 
         "OnMouseHover (chart_zone.VIP)", 
         "Biểu đồ Donut làm nổi bật khu vực VIP bằng hiệu ứng phóng to nhẹ (explode). Hệ thống hiển thị tooltip chi tiết: 'Phân khu: VIP | Doanh thu: 7.000.000.000đ | Tỷ trọng: 45.3%'.", 
         "Tương tác biểu đồ (Hovered): Tooltip chi tiết hiển thị động tại vị trí con trỏ chuột."],
        ["6", 
         "Người dùng nhấp chuột vào nút 'Xuất Excel' (btn_excel).", 
         "OnClick (btn_excel)", 
         "Giao diện gửi yêu cầu kết xuất tệp tới Controller. Hệ thống tạo luồng byte của file Excel, thiết lập MIME-type và hiển thị hộp thoại tải xuống tệp 'Báo_cáo_doanh_thu_BornPink_2026.xlsx'.", 
         "Hiển thị báo cáo (Rendered): Quá trình tải xuống tệp báo cáo hoàn tất trong nền."]
    ]
    add_styled_table(doc, ui_flow_headers, ui_flow_data, col_widths=[0.5, 1.8, 1.1, 2.3, 1.3])

    add_heading_3(doc, "4.2.1. Các kịch bản kiểm lỗi và ràng buộc giao diện (UI Validation Scenarios)")
    add_body_p(doc, "Kịch bản xử lý các ngoại lệ và lỗi nhập liệu trên giao diện nhằm đảm bảo tính toàn vẹn của dữ liệu tra cứu và hướng dẫn người dùng sửa lỗi:")

    ui_err_headers = ["Kịch bản ngoại lệ", "Sự kiện kích hoạt (UI Event)", "Xử lý lỗi & Phản hồi giao diện (System Response)", "Trạng thái giao diện tiếp theo"]
    ui_err_data = [
        ["Người dùng nhập ngày bắt đầu lớn hơn ngày kết thúc (dp_from_date > dp_to_date)",
         "OnClick (btn_search) sau khi sửa ô ngày",
         "Giao diện ngăn chặn gửi yêu cầu tra cứu xuống Controller. Ô viền dp_from_date và dp_to_date chuyển sang màu đỏ cảnh báo. Hệ thống hiển thị hộp thoại pop-up: 'Lỗi: Ngày bắt đầu tra cứu không thể sau ngày kết thúc!'",
         "Cảnh báo lỗi bộ lọc (Error State): Hộp thoại hiển thị nút 'Đóng', người dùng phải sửa lại ngày."],
        ["Sự kiện được chọn chưa phát sinh bất kỳ giao dịch bán vé nào",
         "OnClick (btn_search) đối với sự kiện mới tạo",
         "Controller trả về kết quả rỗng (empty result). Giao diện ẩn biểu đồ tròn và bảng breakdown table, đặt giá trị các thẻ KPI về '0 VNĐ' và '0%'. Hiển thị thông báo màu xám trên màn hình: 'Sự kiện hiện tại chưa phát sinh giao dịch bán vé.'",
         "Báo cáo rỗng (No Data State): Bộ lọc giữ nguyên trạng thái hoạt động để người dùng chọn sự kiện khác."],
        ["Mất kết nối mạng hoặc máy chủ cơ sở dữ liệu gặp sự cố",
         "OnClick (btn_search) khi mất tín hiệu",
         "Hệ thống phát hiện lỗi kết nối (Timeout/Connection Refused). Giao diện ẩn loading spinner, hiển thị thông báo lỗi màu đỏ nổi bật: 'Mất kết nối tới máy chủ. Vui lòng kiểm tra lại đường truyền mạng hoặc liên hệ quản trị viên!'",
         "Lỗi kết nối (Network Error): Giữ nguyên giao diện ban đầu để người dùng thử lại khi mạng ổn định."]
    ]
    add_styled_table(doc, ui_err_headers, ui_err_data, col_widths=[1.5, 1.2, 2.5, 1.3])

    add_heading_2(doc, "4.3. Bản vẽ thiết kế giao diện trực quan (UI Mockup Wireframe)")
    add_body_p(doc, "Dưới đây là bản vẽ thiết kế giao diện hoàn chỉnh (Mockup Wireframe) của Màn hình Thống kê doanh thu sự kiện (RevenueReportView):")
    add_diagram_image(doc, "ui_m5_view_revenue.png", "Hình 4.1: Bản vẽ thiết kế giao diện Màn hình Thống kê doanh thu sự kiện (RevenueReportView)")

    # =========================================================================
    # PHẦN 5: BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH CHO HỆ THỐNG VÀ CHO CÁC CHỨC NĂNG
    # =========================================================================
    add_heading_1(doc, "5. BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH CHO HỆ THỐNG VÀ CHO CÁC CHỨC NĂNG")
    
    add_body_p(doc, "Biểu đồ lớp thực thể phân tích (Analysis Entity Class Diagram) là mô hình hướng khái niệm (Conceptual Model), tập trung thể hiện các thực thể thông tin nghiệp vụ cốt lõi của miền bài toán. Theo chuẩn phân tích:", "Nguyên lý xây dựng: ")
    add_bullet_p(doc, "Chỉ bao gồm Tên thực thể và Danh sách thuộc tính nghiệp vụ thuần túy.", "Cấu trúc lớp phân tích: ")
    add_bullet_p(doc, "Không chứa các chi tiết kỹ thuật lập trình như kiểu dữ liệu cụ thể (int, varchar2...), không chứa các phương thức get/set kỹ thuật.", "Độc lập công nghệ: ")
    add_bullet_p(doc, "Tập trung thể hiện mối quan hệ ngữ nghĩa: Kế thừa (Generalization), Kết hợp (Association), Kết tập/Bao hàm (Composition/Aggregation) kèm bản số (Multiplicity: 1, 1..*, 0..1, *).", "Mối quan hệ: ")

    add_heading_2(doc, "5.1. Biểu đồ lớp thực thể phân tích tổng thể hệ thống")
    add_body_p(doc, "Biểu đồ bao quát toàn bộ các thực thể phân tích nòng cốt của hệ thống (được đồng bộ chuẩn hóa tên tiếng Anh theo mô hình thiết kế) và các mối liên kết nghiệp vụ giữa chúng:")
    add_diagram_image(doc, "analysis_tong_the.png", "Hình 5.1: Biểu đồ lớp thực thể phân tích tổng thể toàn hệ thống")

    ana_headers = ["Tên lớp thực thể (Class)", "Ý nghĩa nghiệp vụ", "Các thuộc tính phân tích (Attributes)"]
    ana_data = [
        ["User", "Thông tin tài khoản chung trong hệ thống", "userId, username, password, fullName, email, phoneNumber, role"],
        ["Customer", "Kế thừa User, đại diện người mua vé", "rewardPoints, memberTier"],
        ["Organizer", "Kế thừa User, đơn vị tổ chức sự kiện", "companyName, taxId, businessLicense, contactInfo"],
        ["Venue", "Nơi diễn ra sự kiện (sân vận động, nhà hát)", "venueId, venueName, address, capacity"],
        ["SeatMap", "Bản thiết kế phân bổ chỗ ngồi của địa điểm", "seatMapId, mapName, stageType, totalSeats"],
        ["SeatZone", "Khu vực khán đài cụ thể (VIP, VVIP, CAT 1)", "zoneId, zoneName, colorHex, zoneType, seatCount"],
        ["Seat", "Vị trí ghế cụ thể trên khán đài", "seatId, rowLabel, seatNumber, coordinateX, coordinateY"],
        ["Event", "Sự kiện được tổ chức (Concert, liveshow, kịch)", "eventId, title, category, description, bannerUrl, status"],
        ["Showtime", "Một buổi biểu diễn cụ thể của sự kiện", "showtimeId, showDate, startTime, endTime"],
        ["ZonePricing", "Định giá vé cho từng khu vực của suất diễn", "pricingId, price, maxQuota, soldCount"],
        ["VirtualQueue", "Bản ghi xếp hàng chờ của khách hàng", "queueId, queueNumber, accessToken, status"],
        ["SeatHold", "Trạng thái khóa giữ ghế trong 10-15 phút", "holdId, holdToken, startTime, expiresAt"],
        ["Order", "Đơn hàng thanh toán vé của khách hàng", "orderId, orderCode, subTotal, discount, finalTotal, status"],
        ["Ticket", "Vé điện tử cấp phát cho từng chỗ ngồi", "ticketId, ticketCode, qrCodeHash, price, isUsed"],
        ["Voucher", "Mã giảm giá khuyến mãi áp dụng cho đơn hàng", "voucherId, code, percentOff, maxDiscount, validUntil"],
        ["PaymentTransaction", "Giao dịch thanh toán trực tuyến qua cổng", "transactionId, transRef, paymentMethod, transAmount, status"]
    ]
    add_styled_table(doc, ana_headers, ana_data, col_widths=[1.5, 2.3, 2.7])

    # Module 1 Analysis
    add_heading_2(doc, "5.2. Biểu đồ lớp thực thể phân tích Phân hệ 1: Quản lý tài khoản")
    add_body_p(doc, "Thể hiện quan hệ kế thừa giữa User với Customer và Organizer, đồng thời liên kết với UserSession (phiên làm việc) và Notification (thông báo gửi tới người dùng).")
    add_diagram_image(doc, "analysis_module1.png", "Hình 5.2: Biểu đồ lớp thực thể phân tích - Phân hệ 1: Quản lý tài khoản")

    # Module 2 Analysis
    add_heading_2(doc, "5.3. Biểu đồ lớp thực thể phân tích Phân hệ 2: Tìm kiếm & Xem sự kiện")
    add_body_p(doc, "Mô hình hóa thực thể Event liên kết với Category, Venue tổ chức, dàn Artist biểu diễn và danh sách FavoriteEvent của khách hàng.")
    add_diagram_image(doc, "analysis_module2.png", "Hình 5.3: Biểu đồ lớp thực thể phân tích - Phân hệ 2: Tìm kiếm & Xem sự kiện")

    # Module 3 Analysis
    add_heading_2(doc, "5.4. Biểu đồ lớp thực thể phân tích Phân hệ 3: Xếp hàng và chọn chỗ")
    add_body_p(doc, "Mô hình hóa cấu trúc phân cấp không gian từ SeatMap -> SeatZone -> Seat, kết hợp với VirtualQueue và thực thể SeatHold khóa giữ các ghế được chọn.")
    add_diagram_image(doc, "analysis_module3.png", "Hình 5.4: Biểu đồ lớp thực thể phân tích - Phân hệ 3: Xếp hàng và chọn chỗ")

    # Module 4 Analysis
    add_heading_2(doc, "5.5. Biểu đồ lớp thực thể phân tích Phân hệ 4: Tính tiền và Xuất vé")
    add_body_p(doc, "Order đóng vai trò trung tâm liên kết với Voucher (0..1), PaymentTransaction (1) và chứa tập hợp các Ticket (1..*), mỗi Ticket tương ứng một Seat duy nhất.")
    add_diagram_image(doc, "analysis_module4.png", "Hình 5.5: Biểu đồ lớp thực thể phân tích - Phân hệ 4: Tính tiền và Xuất vé")

    # Module 5 Analysis - Focused Single Feature
    add_heading_2(doc, "5.6. Biểu đồ lớp thực thể phân tích Chức năng 5: Xem thống kê doanh thu sự kiện")
    add_body_p(doc, "Để đáp ứng nguyên tắc hướng đối tượng cốt lõi (Lớp phải đóng gói trạng thái và hành vi tính toán nghiệp vụ, không chỉ là tập hợp dữ liệu thụ động/Anemic Domain Model), biểu đồ lớp phân tích dưới đây thể hiện chi tiết các thực thể tham gia ca sử dụng đơn lẻ 'Xem thống kê doanh thu sự kiện' cùng các phương thức tính toán tài chính trọng tâm. Toàn bộ tên lớp, thuộc tính và phương thức được chuẩn hóa đồng nhất 100% với pha thiết kế:")
    add_diagram_image(doc, "analysis_m5_view_revenue_detail.png", "Hình 5.6: Biểu đồ lớp thực thể phân tích - Chức năng Xem thống kê doanh thu sự kiện")

    ana_m5_headers = ["Lớp phân tích", "Các thuộc tính phân tích cốt lõi", "Các phương thức thực hiện tính toán (Operations)"]
    ana_m5_data = [
        ["RevenueReport", "id, eventId, calculatedAt, taxRate, platformFeeRate, totalTicketsSold, grossRevenue, netRevenue, occupancyRate, averageTicketPrice", 
         "+ calculateTotalCapacity()\n+ calculateTotalTicketsSold()\n+ calculateGrossRevenue()\n+ calculateNetRevenue()\n+ calculateOccupancyRate()\n+ calculateAverageTicketPrice()\n+ calculateZoneContribution(zoneId)\n+ evaluatePerformance()"],
        ["ZonePricing", "id, zoneName, price, maxQuota, soldCount", 
         "+ calculateZoneGross()\n+ calculateRemainingSeats()\n+ getSoldRate()\n+ isSoldOut()"],
        ["Showtime", "id, showDate, startTime, endTime", 
         "+ calculateShowtimeRevenue()\n+ getSoldTicketsCount()"],
        ["Event", "id, title, category, status", 
         "+ getTotalCapacity()\n+ getShowtimes()"],
        ["SeatZone", "id, zoneName, colorHex, seatCount", 
         "+ countTotalSeats()"],
        ["Organizer", "id, companyName, taxId, email", 
         "+ viewReports(eventId)"]
    ]
    add_styled_table(doc, ana_m5_headers, ana_m5_data, col_widths=[1.5, 2.5, 2.5])

    # =========================================================================
    # PHẦN 6: BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ CHO HỆ THỐNG VÀ CHO CÁC CHỨC NĂNG
    # =========================================================================
    add_heading_1(doc, "6. BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ CHO HỆ THỐNG VÀ CHO CÁC CHỨC NĂNG")
    
    add_body_p(doc, "Biểu đồ lớp thực thể thiết kế (Design Entity Class Diagram) là mô hình mức thiết kế chi tiết (Detailed Object-Oriented Design), sẵn sàng cho việc sinh mã nguồn trong các ngôn ngữ lập trình hiện đại (Java Spring Boot, C# .NET Core, TypeScript) và ánh xạ quan hệ ORM (Hibernate / JPA).", "Nguyên lý xây dựng: ")
    add_bullet_p(doc, "Stereotype <<entity>> định danh các lớp thực thể lưu trữ dữ liệu.", "Stereotype chuẩn: ")
    add_bullet_p(doc, "Đầy đủ 3 ngăn chuẩn UML: Tên lớp, Thuộc tính có phạm vi truy cập (- private) và kiểu dữ liệu cụ thể (Long, String, LocalDateTime, double, boolean...), Phương thức có phạm vi (+ public) và danh sách tham số.", "Cấu trúc 3 ngăn chi tiết: ")
    add_bullet_p(doc, "Xác định rõ các thuộc tính định danh khóa chính (Primary Key - id: Long) và các ràng buộc toàn vẹn.", "Khóa chính và ràng buộc: ")
    add_bullet_p(doc, "Bao gồm các phương thức nghiệp vụ nội tại của đối tượng (ví dụ: isAvailable(), lock(), calculateTotal(), generateQR()).", "Phương thức nghiệp vụ: ")

    add_heading_2(doc, "6.1. Biểu đồ lớp thực thể thiết kế tổng thể hệ thống")
    add_body_p(doc, "Biểu đồ lớp thực thể thiết kế tổng thể thể hiện mối liên kết chặt chẽ giữa tất cả các thực thể nghiệp vụ trong hệ thống:")
    add_diagram_image(doc, "design_tong_the.png", "Hình 6.1: Biểu đồ lớp thực thể thiết kế tổng thể toàn hệ thống")

    # Module 1 Design
    add_heading_2(doc, "6.2. Biểu đồ lớp thực thể thiết kế Phân hệ 1: Quản lý tài khoản")
    add_body_p(doc, "Mô hình thiết kế chi tiết các lớp User, Customer, Organizer, UserSession và Notification:")
    add_diagram_image(doc, "design_module1.png", "Hình 6.2: Biểu đồ lớp thực thể thiết kế - Phân hệ 1: Quản lý tài khoản")

    d1_headers = ["Lớp thiết kế", "Thuộc tính chi tiết (Kiểu dữ liệu & Ràng buộc)", "Phương thức nghiệp vụ (Operations)"]
    d1_data = [
        ["User\n(Base Entity)", "- id: Long [PK, Not Null]\n- username: String [Unique]\n- passwordHash: String [BCrypt]\n- email: String [Unique]\n- phone: String\n- role: UserRole [Enum: CUSTOMER, ORGANIZER, ADMIN]", "+ authenticate(pwd: String): boolean\n+ changePassword(newPwd: String): void\n+ updateInfo(dto: UserDto): void\n+ isAccountNonLocked(): boolean"],
        ["Customer\n(extends User)", "- rewardPoints: int [Default: 0]\n- memberTier: MemberTier [BRONZE, SILVER, GOLD, VIP]", "+ addRewardPoints(pts: int): void\n+ getOrderHistory(): List<Order>\n+ canRedeemPoints(pts: int): boolean"],
        ["Organizer\n(extends User)", "- orgName: String [Not Null]\n- taxId: String [Unique]\n- businessLicense: String", "+ verifyLicense(): boolean\n+ getManagedEvents(): List<Event>\n+ updateOrgProfile(info: OrgDto): void"],
        ["UserSession", "- id: Long [PK]\n- jwtToken: String [Not Null]\n- createdAt: LocalDateTime\n- expiresAt: LocalDateTime", "+ isExpired(): boolean\n+ refreshToken(): String\n+ revoke(): void"],
        ["Notification", "- id: Long [PK]\n- title: String\n- message: String\n- isRead: boolean [Default: false]\n- sentAt: LocalDateTime", "+ markAsRead(): void\n+ sendEmailNotification(): boolean"]
    ]
    add_styled_table(doc, d1_headers, d1_data, col_widths=[1.5, 2.5, 2.5])

    # Module 2 Design
    add_heading_2(doc, "6.3. Biểu đồ lớp thực thể thiết kế Phân hệ 2: Tìm kiếm & Xem sự kiện")
    add_body_p(doc, "Mô hình thiết kế chi tiết các lớp Event, Showtime, Category, Venue, Artist và FavoriteEvent:")
    add_diagram_image(doc, "design_module2.png", "Hình 6.3: Biểu đồ lớp thực thể thiết kế - Phân hệ 2: Tìm kiếm & Xem sự kiện")

    d2_headers = ["Lớp thiết kế", "Thuộc tính chi tiết (Kiểu dữ liệu & Ràng buộc)", "Phương thức nghiệp vụ (Operations)"]
    d2_data = [
        ["Event", "- id: Long [PK]\n- title: String [Not Null]\n- description: String [Text]\n- bannerUrl: String\n- status: EventStatus [DRAFT, PUBLISHED, SOLD_OUT, ENDED]", "+ publish(): void\n+ cancel(): void\n+ isUpcoming(): boolean\n+ getActiveShowtimes(): List<Showtime>"],
        ["Showtime", "- id: Long [PK]\n- showDate: LocalDate [Not Null]\n- startTime: LocalTime [Not Null]\n- endTime: LocalTime", "+ isAvailableForBooking(): boolean\n+ getAvailableSeats(): int\n+ isOngoing(): boolean"],
        ["Category", "- id: Long [PK]\n- name: String [Unique, Not Null]\n- code: String [Unique]", "+ getEvents(): List<Event>\n+ countEvents(): int"],
        ["Venue", "- id: Long [PK]\n- name: String [Not Null]\n- address: String [Not Null]\n- capacity: int [> 0]", "+ checkCapacity(): boolean\n+ getAssignedSeatMap(): SeatMap"],
        ["Artist", "- id: Long [PK]\n- stageName: String [Not Null]\n- bio: String\n- avatarUrl: String", "+ getParticipatingEvents(): List<Event>"],
        ["FavoriteEvent", "- id: Long [PK]\n- customerId: Long [FK]\n- savedDate: LocalDateTime", "+ notifySaleOpening(): void\n+ remove(): void"]
    ]
    add_styled_table(doc, d2_headers, d2_data, col_widths=[1.5, 2.5, 2.5])

    # Module 3 Design
    add_heading_2(doc, "6.4. Biểu đồ lớp thực thể thiết kế Phân hệ 3: Xếp hàng và chọn chỗ")
    add_body_p(doc, "Mô hình thiết kế chi tiết các lớp SeatMap, SeatZone, Seat, VirtualQueue và SeatHold:")
    add_diagram_image(doc, "design_module3.png", "Hình 6.4: Biểu đồ lớp thực thể thiết kế - Phân hệ 3: Xếp hàng và chọn chỗ")

    d3_headers = ["Lớp thiết kế", "Thuộc tính chi tiết (Kiểu dữ liệu & Ràng buộc)", "Phương thức nghiệp vụ (Operations)"]
    d3_data = [
        ["SeatMap", "- id: Long [PK]\n- mapName: String [Not Null]\n- totalSeats: int [> 0]\n- layoutSvg: String [SVG Schema]", "+ validateLayout(): boolean\n+ getZones(): List<SeatZone>\n+ getTotalCapacity(): int"],
        ["SeatZone", "- id: Long [PK]\n- zoneName: String [VIP, CAT 1...]\n- colorHex: String [#FF0000]\n- zoneType: ZoneType [SEATED, STANDING]", "+ getSeats(): List<Seat>\n+ countVacantSeats(): int\n+ isStandingZone(): boolean"],
        ["Seat", "- id: Long [PK]\n- rowLabel: String [A, B, C...]\n- seatNumber: int [1, 2, 3...]\n- isLocked: boolean [Default: false]", "+ lockSeat(token: String): boolean\n+ unlockSeat(): void\n+ isAvailable(): boolean\n+ getSeatCode(): String"],
        ["VirtualQueue", "- id: Long [PK]\n- queueNumber: int [Auto-increment]\n- accessToken: String [UUID]\n- status: QueueStatus [WAITING, SERVING, EXPIRED]", "+ isTurn(): boolean\n+ generateToken(): String\n+ expireToken(): void"],
        ["SeatHold", "- id: Long [PK]\n- holdToken: String [UUID, Unique]\n- startTime: LocalDateTime\n- expiresAt: LocalDateTime", "+ isExpired(): boolean\n+ getRemainingSeconds(): long\n+ confirmHold(): void\n+ releaseHold(): void"]
    ]
    add_styled_table(doc, d3_headers, d3_data, col_widths=[1.5, 2.5, 2.5])

    # Module 4 Design
    add_heading_2(doc, "6.5. Biểu đồ lớp thực thể thiết kế Phân hệ 4: Tính tiền và Xuất vé")
    add_body_p(doc, "Mô hình thiết kế chi tiết các lớp Order, Voucher, PaymentTransaction và Ticket:")
    add_diagram_image(doc, "design_module4.png", "Hình 6.5: Biểu đồ lớp thực thể thiết kế - Phân hệ 4: Tính tiền và Xuất vé")

    d4_headers = ["Lớp thiết kế", "Thuộc tính chi tiết (Kiểu dữ liệu & Ràng buộc)", "Phương thức nghiệp vụ (Operations)"]
    d4_data = [
        ["Order", "- id: Long [PK]\n- orderCode: String [ORD-XXXXX]\n- subTotal: double [>= 0]\n- discount: double [>= 0]\n- finalTotal: double [>= 0]\n- status: OrderStatus [PENDING, PAID, CANCELLED]", "+ calculateFinalTotal(): double\n+ applyVoucher(v: Voucher): boolean\n+ markAsPaid(): void\n+ cancelOrder(): void"],
        ["Voucher", "- id: Long [PK]\n- code: String [Unique, Not Null]\n- percentOff: double [0.0 - 100.0]\n- maxDiscount: double\n- validUntil: LocalDate", "+ isValid(amount: double): boolean\n+ calculateDiscount(amount: double): double\n+ decrementQuota(): void"],
        ["PaymentTransaction", "- id: Long [PK]\n- transRef: String [Bank Reference]\n- method: PaymentMethod [VNPAY, MOMO, VISA]\n- transAmount: double\n- status: TransStatus [SUCCESS, FAILED, PENDING]", "+ processPayment(): boolean\n+ verifyWebhook(payload: String): boolean\n+ getGatewayUrl(): String"],
        ["Ticket", "- id: Long [PK]\n- ticketCode: String [TCK-XXXXX]\n- qrCodeHash: String [HMAC-SHA256 Encrypted]\n- price: double\n- isUsed: boolean [Default: false]\n- checkinTime: LocalDateTime", "+ generateEncryptedQR(): String\n+ checkIn(): boolean\n+ isCheckedIn(): boolean\n+ cancelTicket(): void"]
    ]
    add_styled_table(doc, d4_headers, d4_data, col_widths=[1.5, 2.5, 2.5])

    # Module 5 Design - Focused Single Feature
    add_heading_2(doc, "6.6. Biểu đồ lớp thực thể thiết kế Chức năng 5: Xem thống kê doanh thu sự kiện")
    add_body_p(doc, "Chức năng 'Xem thống kê doanh thu sự kiện' (View Event Revenue Statistics) là chức năng đơn lẻ (Single Atomic Function - Read/Calculate Analytics) phụ trách toàn bộ việc tính toán và kết xuất báo cáo tài chính cho sự kiện. Dưới đây là thiết kế chi tiết bao gồm biểu đồ tuần tự tương tác BCE, biểu đồ lớp thiết kế BCE & DTO, bảng từ điển lớp thiết kế, bảng thuật toán chi tiết cho các phương thức tính toán và các ghi chú kiến trúc:")

    add_heading_3(doc, "a. Biểu đồ tuần tự (Sequence Diagram) thể hiện tương tác BCE")
    add_body_p(doc, "Biểu đồ tuần tự thể hiện sự tương tác mạch lạc giữa tác nhân Ban tổ chức, lớp Boundary (Giao diện), lớp Control (Điều phối) và các lớp Entity (Thực thể tính toán):")
    add_diagram_image(doc, "seq_m5_view_revenue.png", "Hình 6.6: Biểu đồ tuần tự ca sử dụng Xem thống kê doanh thu sự kiện")

    add_heading_3(doc, "b. Biểu đồ lớp thiết kế chi tiết theo mô hình BCE & DTO")
    add_body_p(doc, "Mô hình thiết kế 3 lớp (Boundary - Control - Entity) kết hợp tầng DTO làm nổi bật các phương thức tính toán nghiệp vụ trong các lớp thực thể RevenueReport và ZonePricing. Toàn bộ tên biến, kiểu dữ liệu chuẩn và phương thức tương ứng đồng nhất 100% với pha phân tích:")
    add_diagram_image(doc, "design_m5_view_revenue_detail.png", "Hình 6.7: Biểu đồ lớp thiết kế chi tiết (BCE & DTO) chức năng Thống kê doanh thu")

    d5_detail_headers = ["Lớp thiết kế", "Thuộc tính chi tiết (Kiểu dữ liệu & Ràng buộc)", "Phương thức nghiệp vụ & Tính toán"]
    d5_detail_data = [
        ["RevenueReport\n(<<entity>>)", 
         "- id: Long [PK]\n- eventId: Long [FK]\n- calculatedAt: LocalDateTime\n- taxRate: double\n- platformFeeRate: double\n- totalTicketsSold: int\n- grossRevenue: double\n- netRevenue: double\n- occupancyRate: double\n- averageTicketPrice: double",
         "+ calculateTotalCapacity(): int\n+ calculateTotalTicketsSold(): int\n+ calculateGrossRevenue(): double\n+ calculateNetRevenue(): double\n+ calculateOccupancyRate(): double\n+ calculateAverageTicketPrice(): double\n+ calculateZoneContribution(zoneId: Long): double\n+ evaluatePerformance(): PerformanceStatus\n+ exportExcel(): byte[]\n+ exportPdf(): byte[]"],
        ["ZonePricing\n(<<entity>>)", 
         "- id: Long [PK]\n- zoneName: String\n- price: double [>= 0]\n- maxQuota: int\n- soldCount: int",
         "+ calculateZoneGross(): double\n+ calculateRemainingSeats(): int\n+ getSoldRate(): double\n+ isSoldOut(): boolean\n+ recordSale(quantity: int): void"],
        ["Showtime\n(<<entity>>)", 
         "- id: Long [PK]\n- showDate: LocalDate\n- startTime: LocalTime\n- endTime: LocalTime",
         "+ calculateShowtimeRevenue(): double\n+ getSoldTicketsCount(): int\n+ isPublished(): boolean"],
        ["Event\n(<<entity>>)", 
         "- id: Long [PK]\n- title: String\n- category: String\n- status: EventStatus",
         "+ getTotalCapacity(): int\n+ getShowtimes(): List<Showtime>"],
        ["RevenueSummaryDto\n(<<dto>>)", 
         "- grossRevenue: double\n- netRevenue: double\n- occupancyRate: double\n- averagePrice: double\n- status: PerformanceStatus\n- zoneBreakdowns: List<ZoneRevenueDto>",
         "+ getGrossRevenue(): double\n+ getNetRevenue(): double\n+ getOccupancyRate(): double"],
        ["RevenueReportController\n(<<control>>)", 
         "- reportService: ReportService\n- eventRepo: EventRepository",
         "+ handleViewReport(eventId: Long): RevenueSummaryDto\n+ calculateZoneAnalytics(eventId: Long): List<ZoneRevenueDto>\n+ formatReportData(report: RevenueReport): RevenueSummaryDto"],
        ["RevenueReportView\n(<<boundary>>)", 
         "- eventSelector: ComboBox\n- kpiPanel: Panel\n- zoneChart: ChartView",
         "+ onSelectEvent(eventId: Long): void\n+ displayKPIs(dto: RevenueSummaryDto): void\n+ renderZoneChart(data: List<ZoneRevenueDto>): void\n+ showError(msg: String): void"]
    ]
    add_styled_table(doc, d5_detail_headers, d5_detail_data, col_widths=[1.5, 2.5, 2.5])

    add_heading_3(doc, "d. Bảng phân tích chi tiết các phương thức tính toán (Computational Methods)")
    add_body_p(doc, "Để các lớp không bị biến thành 'cấu trúc dữ liệu thụ động' (Anemic Domain Model), toàn bộ logic tính toán tài chính được đóng gói trực tiếp vào các thực thể:")

    calc_headers = ["Tên phương thức tính toán", "Lớp sở hữu", "Kiểu trả về", "Công thức / Thuật toán tính toán"]
    calc_data = [
        ["calculateTotalCapacity()", "RevenueReport", "int", "Tổng sức chứa của khán đài = tổng số ghế của tất cả các phân khu (ZonePricing):\nTotalCapacity = sum(zone.seatCount)"],
        ["calculateTotalTicketsSold()", "RevenueReport", "int", "Tổng số vé thực tế đã bán thành công = tổng số vé bán ra của từng phân khu:\nTotalSold = sum(zone.soldCount)"],
        ["calculateGrossRevenue()", "RevenueReport", "double", "Tổng doanh thu gộp = tổng tích số giữa số vé đã bán và đơn giá vé từng khu vực:\nGrossRevenue = sum(zone.soldCount * zone.price)"],
        ["calculateNetRevenue()", "RevenueReport", "double", "Doanh thu thuần thực nhận sau khi khấu trừ thuế VAT và phí nền tảng:\nNetRevenue = GrossRevenue * (1 - taxRate - platformFeeRate)"],
        ["calculateOccupancyRate()", "RevenueReport", "double", "Tỷ lệ lấp đầy khán đài theo phần trăm:\nOccupancyRate = (TotalSold / (double) TotalCapacity) * 100.0%"],
        ["calculateAverageTicketPrice()", "RevenueReport", "double", "Giá vé bình quân trên mỗi vé bán ra:\nAvgPrice = TotalSold > 0 ? (GrossRevenue / TotalSold) : 0.0"],
        ["calculateZoneContribution(zoneId)", "RevenueReport", "double", "Tỷ trọng đóng góp doanh thu của một khu vực so với tổng doanh thu:\nContribution = (ZoneGross / GrossRevenue) * 100.0%"],
        ["evaluatePerformance()", "RevenueReport", "PerformanceStatus", "Đánh giá phân loại sức mua theo thang tỷ lệ lấp đầy:\n- Occupancy >= 85%: EXCELLENT (Cháy vé)\n- 70% <= Occupancy < 85%: GOOD (Đạt chỉ tiêu)\n- 50% <= Occupancy < 70%: AVERAGE (Hòa vốn)\n- Occupancy < 50%: POOR (Cần giải cứu vé)"],
        ["calculateZoneGross()", "ZonePricing", "double", "Doanh thu của riêng phân khu vé = price * soldCount"],
        ["getSoldRate()", "ZonePricing", "double", "Tỷ lệ bán của riêng phân khu = (soldCount / (double) maxQuota) * 100.0%"]
    ]
    add_styled_table(doc, calc_headers, calc_data, col_widths=[1.8, 1.1, 1.1, 2.5])

    add_heading_3(doc, "e. Các ghi chú kiến trúc và thiết kế giải thích chi tiết sơ đồ (Architectural & Design Notes)")
    
    add_body_p(doc, "Trong sơ đồ lớp thiết kế, RevenueSummaryDto (Data Transfer Object) và ZoneRevenueDto là các đối tượng truyền tải dữ liệu thuần túy (POJO) giữa tầng Điều khiển (RevenueReportController) và tầng Giao diện (RevenueReportView). Việc sử dụng DTO mang lại 3 lợi ích kiến trúc cốt lõi:\n"
                    "1. Tính đóng gói và bảo mật (Encapsulation & Security): DTO che giấu cấu trúc bảng cơ sở dữ liệu và các thông tin nghiệp vụ nội bộ nhạy cảm của Entity, không để lộ xuống tầng Presentation.\n"
                    "2. Tối ưu hóa hiệu năng và làm phẳng dữ liệu (Flattening & Performance): Thay vì truyền các đối tượng Entity phức tạp có liên kết vòng, Controller gọi các hàm tính toán của Entity, đóng gói toàn bộ kết quả đã tính toán (Gross Revenue, Net Revenue, Occupancy Rate, Performance Status) vào một đối tượng DTO phẳng, nhẹ. Giao diện người dùng (UI) chỉ việc đọc các giá trị này để hiển thị lên thẻ KPI và vẽ biểu đồ mà không cần tính toán lại.\n"
                    "3. Giải quyết vấn đề Lazy Loading trong ORM: Khi sử dụng các framework ORM (như Hibernate/JPA), việc truy cập các thuộc tính liên kết lười ngoài phạm vi Session/Transaction dễ dẫn đến lỗi LazyInitializationException. DTO được khởi tạo bên trong ranh giới Service/Controller giải quyết triệt để lỗi này.",
               "1. Khái niệm DTO (Data Transfer Object) và lý do áp dụng: ")

    add_body_p(doc, "Hệ thống áp dụng nghiêm ngặt mẫu phân rã trách nhiệm 3 lớp của Jacobson:\n"
                    "• <<boundary>> (RevenueReportView): Lớp giao diện người dùng, chịu trách nhiệm nhận sự kiện tương tác (chọn sự kiện từ ComboBox) và kết xuất dữ liệu DTO lên màn hình (KPI cards, biểu đồ tròn phân khu).\n"
                    "• <<control>> (RevenueReportController): Đóng vai trò điều phối luồng xử lý (Orchestrator). Controller không trực tiếp chứa các công thức toán học tính tiền, mà điều hướng: nhận yêu cầu từ View -> nạp Entity -> kích hoạt các hàm tính toán của Entity -> đóng gói kết quả vào DTO -> gửi trả View.\n"
                    "• <<entity>> (RevenueReport, ZonePricing, Showtime, Event): Lớp thực thể nghiệp vụ chứa dữ liệu và trực tiếp đóng gói các thuật toán tính toán (Rich Domain Model).\n"
                    "• <<enumeration>> (PerformanceStatus): Kiểu liệt kê định nghĩa tập hợp các giá trị đánh giá chuẩn mực (EXCELLENT, GOOD, AVERAGE, POOR).\n"
                    "• <<dto>> (RevenueSummaryDto): Đối tượng mang dữ liệu kết quả giữa Control và Boundary.",
               "2. Phân tách vai trò theo mẫu thiết kế BCE (Boundary - Control - Entity): ")

    add_body_p(doc, "Mối quan hệ giữa Suất diễn (Showtime) và Phân khu ghế (SeatZone) về bản chất là quan hệ nhiều - nhiều (*..*). Tuy nhiên, tại mỗi suất diễn cụ thể, một phân khu sẽ có đơn giá vé riêng (price), chỉ tiêu phát hành riêng (maxQuota) và số vé đã bán thực tế riêng (soldCount). Do đó, lớp ZonePricing đóng vai trò là Lớp liên kết nghiệp vụ (Association Class), phân rã quan hệ *..* thành 2 quan hệ 1..* (Showtime 1 -> * ZonePricing * -> 1 SeatZone). Thiết kế này loại bỏ hoàn toàn sự dư thừa liên kết (Redundant Association) và phản ánh chính xác nghiệp vụ bán vé theo từng đêm diễn.",
               "3. Giải quyết quan hệ N-N giữa Showtime và SeatZone: ")

    add_body_p(doc, "Theo nguyên lý Information Expert của GRASP, trách nhiệm tính toán phải được gán cho lớp sở hữu đầy đủ thông tin nhất để thực hiện tính toán đó. Do RevenueReport chứa tập hợp các phân khu ZonePricing và thuế phí, việc đặt các phương thức calculateGrossRevenue(), calculateNetRevenue(), calculateOccupancyRate() trực tiếp trong RevenueReport đảm bảo lớp có cả Trạng thái (State) và Hành vi (Behavior), đáp ứng tiêu chuẩn khắt khe của môn học, tránh mô hình Anemic Domain Model.",
               "4. Nguyên lý đóng gói hành vi tính toán (Information Expert): ")

    # Final summary conclusion
    add_heading_1(doc, "KẾT LUẬN VÀ CAM KẾT HOÀN THÀNH")
    add_body_p(doc, "Tài liệu phân tích và thiết kế hệ thống trên đã hoàn thiện đầy đủ 6 yêu cầu kiểm tra môn học theo đúng đề cương bài tập lớn do Thầy Nguyễn Đức Hiển giao:")
    add_bullet_p(doc, "Đầy đủ thông tin nhóm, tên đề tài, phân công nhiệm vụ và phạm vi chức năng cho từng thành viên.", "1. Thông tin nhóm: ")
    add_bullet_p(doc, "Biểu đồ Use Case tổng thể toàn hệ thống và các biểu đồ Use Case phân rã chi tiết cho từng chức năng kèm bảng đặc tả tóm tắt nghiệp vụ.", "2. Biểu đồ Use Case: ")
    add_bullet_p(doc, "Kịch bản phân tích (Scenario) chuẩn hóa với các trường Tác nhân, Tiền điều kiện, Đảm bảo tối thiểu/thành công, Chuỗi sự kiện chính và Luồng ngoại lệ.", "3. Kịch bản phân tích: ")
    add_bullet_p(doc, "Bảng đặc tả thành phần điều khiển UI, kịch bản tương tác người dùng - hệ thống và bản vẽ thiết kế giao diện (Mockup Wireframe) trực quan.", "4. Kịch bản & Thiết kế giao diện: ")
    add_bullet_p(doc, "Biểu đồ lớp thực thể phân tích tổng thể và các phân hệ, thể hiện đúng bản chất mô hình hóa khái niệm miền bài toán với các phương thức tính toán đóng gói.", "5. Biểu đồ lớp phân tích: ")
    add_bullet_p(doc, "Biểu đồ lớp thực thể thiết kế tổng thể và chi tiết theo mô hình 3 lớp (BCE & DTO) với kiểu dữ liệu chặt chẽ, ràng buộc khóa chính và bảng thuật toán các phương thức tính toán.", "6. Biểu đồ lớp thiết kế: ")

    # Save to multiple target filenames to ensure full compatibility
    targets = ["N13 Nhóm 01.docx", "N12 Nhóm 01 - HoanChinh.docx", "N12 Nhóm 01.docx"]
    for t_name in targets:
        out_path = os.path.join(BASE_DIR, t_name)
        try:
            doc.save(out_path)
            print(f"Document successfully generated and saved to: {out_path}")
        except PermissionError:
            print(f"Note: '{t_name}' is currently locked by Word, skipped overwriting.")

if __name__ == "__main__":
    build_full_docx()
