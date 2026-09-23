import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

plt.rcParams['font.family'] = 'Times New Roman'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "diagrams")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ====================================================================
# UML Box Class with exact bounding and edge attachment points
# ====================================================================
class UMLBox:
    def __init__(self, name, attrs=None, methods=None, is_design=False, w=220):
        self.name = name
        self.attrs = attrs or []
        self.methods = methods or []
        self.is_design = is_design
        self.w = w
        
        self.line_h = 20
        if is_design:
            self.h_hdr = 38
            self.h_attrs = max(len(self.attrs) * self.line_h + 12, 26)
            self.h_methods = max(len(self.methods) * self.line_h + 12, 26)
            self.h = self.h_hdr + self.h_attrs + self.h_methods
        else:
            self.h_hdr = 32
            self.h_attrs = max(len(self.attrs) * self.line_h + 12, 28)
            self.h_methods = 0
            self.h = self.h_hdr + self.h_attrs
        self.x = 0
        self.y = 0

    def place(self, x, y_top):
        self.x = x
        self.y = y_top
        return self

    @property
    def top(self):
        return (self.x + self.w / 2, self.y)

    @property
    def bottom(self):
        return (self.x + self.w / 2, self.y - self.h)

    @property
    def left(self):
        return (self.x, self.y - self.h / 2)

    @property
    def right(self):
        return (self.x + self.w, self.y - self.h / 2)

    def pt(self, side, offset=0):
        if side == 'top':
            return (self.x + self.w / 2 + offset, self.y)
        elif side == 'bottom':
            return (self.x + self.w / 2 + offset, self.y - self.h)
        elif side == 'left':
            return (self.x, self.y - self.h / 2 + offset)
        elif side == 'right':
            return (self.x + self.w, self.y - self.h / 2 + offset)

    def draw(self, ax):
        border_col = '#1E3A8A'
        bg_hdr = '#DBEAFE' if not self.is_design else '#BFDBFE'
        bg_body = '#FFFFFF'

        # Outer box
        rect = patches.Rectangle((self.x, self.y - self.h), self.w, self.h,
                                 edgecolor=border_col, facecolor=bg_body, lw=1.4, zorder=3)
        ax.add_patch(rect)

        # Header box
        hdr_rect = patches.Rectangle((self.x, self.y - self.h_hdr), self.w, self.h_hdr,
                                     edgecolor=border_col, facecolor=bg_hdr, lw=1.4, zorder=4)
        ax.add_patch(hdr_rect)

        if self.is_design:
            ax.text(self.x + self.w / 2, self.y - 12, '<<entity>>', ha='center', va='center',
                    fontsize=8.0, style='italic', color='#1E3A8A', zorder=5)
            ax.text(self.x + self.w / 2, self.y - 27, self.name, ha='center', va='center',
                    fontsize=9.5, weight='bold', color='#0F172A', zorder=5)
            
            sep_y = self.y - self.h_hdr - self.h_attrs
            ax.plot([self.x, self.x + self.w], [sep_y, sep_y], color=border_col, lw=1.1, zorder=4)

            cur_y = self.y - self.h_hdr - 14
            for a in self.attrs:
                ax.text(self.x + 10, cur_y, a, ha='left', va='center',
                        fontsize=8.0, color='#1E293B', fontfamily='Consolas', zorder=5)
                cur_y -= self.line_h

            cur_y = sep_y - 14
            for m in self.methods:
                ax.text(self.x + 10, cur_y, m, ha='left', va='center',
                        fontsize=8.0, color='#1E293B', fontfamily='Consolas', zorder=5)
                cur_y -= self.line_h
        else:
            ax.text(self.x + self.w / 2, self.y - self.h_hdr / 2, self.name, ha='center', va='center',
                    fontsize=10.0, weight='bold', color='#0F172A', zorder=5)
            cur_y = self.y - self.h_hdr - 14
            for a in self.attrs:
                ax.text(self.x + 10, cur_y, a, ha='left', va='center',
                        fontsize=8.5, color='#1E293B', zorder=5)
                cur_y -= self.line_h

# ====================================================================
# Relationship Line Functions
# ====================================================================
def line(ax, p1, p2, color='#334155', lw=1.3, ls='-'):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, lw=lw, linestyle=ls, zorder=2)

def polyline(ax, pts, color='#334155', lw=1.3, ls='-'):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=color, lw=lw, linestyle=ls, zorder=2)

def draw_assoc(ax, p1, p2, mult1="", mult2="", label="", color='#334155'):
    line(ax, p1, p2, color=color, lw=1.3)
    if mult1:
        ax.text(p1[0] + 6, p1[1] + 6, mult1, fontsize=8, color='#334155', weight='bold', zorder=5)
    if mult2:
        ax.text(p2[0] - 16, p2[1] + 6, mult2, fontsize=8, color='#334155', weight='bold', zorder=5)
    if label:
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + 6
        ax.text(mx, my, label, ha='center', va='bottom', fontsize=7.8, color='#0F172A', style='italic', zorder=5)

def draw_polyline_assoc(ax, pts, mult1="", mult2="", label="", color='#334155'):
    polyline(ax, pts, color=color, lw=1.3)
    p1 = pts[0]
    p2 = pts[-1]
    if mult1:
        ax.text(p1[0] + 6, p1[1] + 6, mult1, fontsize=8, color='#334155', weight='bold', zorder=5)
    if mult2:
        ax.text(p2[0] - 16, p2[1] + 6, mult2, fontsize=8, color='#334155', weight='bold', zorder=5)
    if label:
        mid_idx = len(pts) // 2
        mx, my = pts[mid_idx][0], pts[mid_idx][1] + 6
        ax.text(mx, my, label, ha='center', va='bottom', fontsize=7.8, color='#0F172A', style='italic', zorder=5)

def draw_inheritance(ax, child_pt, parent_pt, color='#1E3A8A'):
    ax.annotate("", xy=parent_pt, xytext=child_pt,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4, mutation_scale=12), zorder=4)

def draw_polyline_inheritance(ax, pts, color='#1E3A8A'):
    # Draw polyline except last segment
    for i in range(len(pts) - 2):
        line(ax, pts[i], pts[i+1], color=color, lw=1.4)
    # Draw arrow on last segment
    ax.annotate("", xy=pts[-1], xytext=pts[-2],
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4, mutation_scale=12), zorder=4)

def draw_composition(ax, p_diamond, p_target, mult1="", mult2="", color='#0F172A'):
    # Diamond at p_diamond
    dx = 12 if p_target[0] >= p_diamond[0] else -12
    dy = 0
    if abs(p_target[1] - p_diamond[1]) > abs(p_target[0] - p_diamond[0]):
        dx = 0
        dy = 12 if p_target[1] >= p_diamond[1] else -12

    if dx != 0:
        pts = [[p_diamond[0], p_diamond[1]],
               [p_diamond[0] + dx/2, p_diamond[1] + 6],
               [p_diamond[0] + dx, p_diamond[1]],
               [p_diamond[0] + dx/2, p_diamond[1] - 6]]
        p_start = (p_diamond[0] + dx, p_diamond[1])
    else:
        pts = [[p_diamond[0], p_diamond[1]],
               [p_diamond[0] + 6, p_diamond[1] + dy/2],
               [p_diamond[0], p_diamond[1] + dy],
               [p_diamond[0] - 6, p_diamond[1] + dy/2]]
        p_start = (p_diamond[0], p_diamond[1] + dy)

    diamond = patches.Polygon(pts, closed=True, edgecolor=color, facecolor=color, lw=1.2, zorder=5)
    ax.add_patch(diamond)
    line(ax, p_start, p_target, color=color, lw=1.3)

    if mult1:
        ax.text(p_start[0] + 6, p_start[1] + 6, mult1, fontsize=8, color='#334155', weight='bold', zorder=5)
    if mult2:
        ax.text(p_target[0] + 6, p_target[1] + 6, mult2, fontsize=8, color='#334155', weight='bold', zorder=5)

# ====================================================================
# USE CASE HELPERS
# ====================================================================
def draw_uc_actor(ax, x, y, name, color='#1E3A8A'):
    circle = patches.Circle((x, y + 25), 12, edgecolor=color, facecolor='#DBEAFE', lw=2, zorder=5)
    ax.add_patch(circle)
    ax.plot([x, x], [y + 13, y - 20], color=color, lw=2.2, zorder=5)
    ax.plot([x - 20, x + 20], [y, y], color=color, lw=2.2, zorder=5)
    ax.plot([x, x - 18], [y - 20, y - 50], color=color, lw=2.2, zorder=5)
    ax.plot([x, x + 18], [y - 20, y - 50], color=color, lw=2.2, zorder=5)
    ax.text(x, y - 70, name, ha='center', va='top', fontsize=9.5, weight='bold', color='#0F172A', zorder=5)

def draw_uc_external(ax, x, y, w, h, name, color='#047857', bg='#D1FAE5'):
    rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=5", edgecolor=color, facecolor=bg, lw=1.8, zorder=5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h*0.7, '<<actor>>', ha='center', va='center', fontsize=8.5, style='italic', color=color, zorder=5)
    ax.text(x + w/2, y + h*0.35, name, ha='center', va='center', fontsize=9.5, weight='bold', color='#065F46', zorder=5)

def draw_ellipse_uc(ax, cx, cy, text, rx=110, ry=26, color='#1D4ED8', bg='#EFF6FF'):
    ellipse = patches.Ellipse((cx, cy), rx*2, ry*2, edgecolor=color, facecolor=bg, lw=1.5, zorder=4)
    ax.add_patch(ellipse)
    ax.text(cx, cy, text, ha='center', va='center', fontsize=8.8, color='#0F172A', zorder=5, multialignment='center')

def draw_uc_boundary(ax, x, y, w, h, title):
    rect = patches.Rectangle((x, y), w, h, edgecolor='#94A3B8', facecolor='#F8FAFC', lw=1.6, linestyle='--', zorder=1)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h - 22, title, ha='center', va='center', fontsize=11.5, weight='bold', color='#1E293B', zorder=2)

def connect_uc(ax, p1, p2, color='#64748B', lw=1.2):
    line(ax, p1, p2, color=color, lw=lw)

def arrow_uc(ax, p1, p2, label="", color='#2563EB'):
    ax.annotate("", xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle="->", color=color, lw=1.3, linestyle="--"), zorder=4)
    if label:
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + 8
        ax.text(mx, my, label, ha='center', va='center', fontsize=8, color=color, style='italic',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFFFFF', edgecolor='none', alpha=0.9), zorder=5)


# ====================================================================
# 1. BIỂU ĐỒ USE CASE
# ====================================================================

def gen_uc_tong_the():
    fig, ax = plt.subplots(figsize=(12, 8.5), dpi=220)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 700)
    ax.axis('off')

    draw_uc_boundary(ax, 220, 20, 560, 660, "HỆ THỐNG ĐẶT VÉ THAM GIA SỰ KIỆN TRỰC TUYẾN")

    # Left Actors
    draw_uc_actor(ax, 110, 520, "Khách hàng\n(Customer)")
    draw_uc_actor(ax, 110, 190, "Ban tổ chức\n(Organizer)")

    # Right Actors
    draw_uc_external(ax, 820, 540, 150, 70, "Cổng thanh toán\n(VNPAY / MoMo)")
    draw_uc_external(ax, 820, 350, 150, 70, "Hệ thống Email / SMS\n(Notification)")
    draw_uc_actor(ax, 890, 150, "Quản trị viên\n(Administrator)")

    # Use Cases
    # Module 1
    draw_ellipse_uc(ax, 380, 620, "Đăng ký & Đăng nhập")
    draw_ellipse_uc(ax, 620, 620, "Quản lý thông tin cá nhân")
    # Module 2
    draw_ellipse_uc(ax, 380, 510, "Tìm kiếm & Xem sự kiện")
    draw_ellipse_uc(ax, 620, 510, "Lưu sự kiện yêu thích")
    # Module 3
    draw_ellipse_uc(ax, 380, 400, "Xếp hàng đợi ảo")
    draw_ellipse_uc(ax, 620, 400, "Xem sơ đồ & Giữ ghế")
    # Module 4
    draw_ellipse_uc(ax, 380, 290, "Tạo đơn & Nhập mã giảm giá")
    draw_ellipse_uc(ax, 620, 290, "Thanh toán vé trực tuyến")
    draw_ellipse_uc(ax, 500, 215, "Nhận vé điện tử (QR Code)")
    # Module 5
    draw_ellipse_uc(ax, 380, 130, "Thiết kế sơ đồ ghế sân khấu")
    draw_ellipse_uc(ax, 620, 130, "Tạo & Quản lý sự kiện, giá vé")
    draw_ellipse_uc(ax, 500, 55, "Quản lý check-in & Báo cáo doanh thu")

    # Connect Customer
    for uc_pt in [(270, 620), (270, 510), (510, 510), (270, 400), (510, 400), (270, 290), (510, 290), (390, 215)]:
        connect_uc(ax, (130, 520), uc_pt)

    # Connect Organizer
    for uc_pt in [(270, 620), (270, 130), (510, 130), (390, 55)]:
        connect_uc(ax, (130, 190), uc_pt)

    # Connect External Actors
    connect_uc(ax, (730, 290), (820, 575)) # Payment GW to Thanh toan
    connect_uc(ax, (730, 620), (820, 385)) # Email to Quản lý tài khoản
    connect_uc(ax, (610, 215), (820, 385)) # Email to Nhận vé QR
    connect_uc(ax, (730, 130), (870, 150)) # Admin to Quản lý sự kiện
    connect_uc(ax, (610, 55), (870, 150))  # Admin to Báo cáo

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "uc_tong_the.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_uc_module1():
    fig, ax = plt.subplots(figsize=(10, 7), dpi=220)
    ax.set_xlim(0, 900)
    ax.set_ylim(0, 600)
    ax.axis('off')

    draw_uc_boundary(ax, 220, 20, 480, 560, "PHÂN HỆ 1: QUẢN LÝ TÀI KHOẢN NGƯỜI DÙNG")

    draw_uc_actor(ax, 110, 300, "Người dùng\n(User)")
    draw_uc_external(ax, 730, 280, 150, 70, "Dịch vụ Email / SMS\n(Notification)")

    draw_ellipse_uc(ax, 360, 510, "Đăng ký tài khoản")
    draw_ellipse_uc(ax, 580, 510, "Gửi mã OTP xác nhận", rx=85, ry=22, bg='#FEF3C7', color='#D97706')

    draw_ellipse_uc(ax, 360, 410, "Đăng nhập")
    draw_ellipse_uc(ax, 580, 410, "Khóa tài khoản tạm thời\n(sai quá 5 lần)", rx=90, ry=22, bg='#FEE2E2', color='#DC2626')

    draw_ellipse_uc(ax, 360, 310, "Đổi mật khẩu")

    draw_ellipse_uc(ax, 360, 210, "Quên / Lấy lại mật khẩu")
    draw_ellipse_uc(ax, 580, 210, "Gửi link reset mật khẩu", rx=85, ry=22, bg='#FEF3C7', color='#D97706')

    draw_ellipse_uc(ax, 360, 120, "Chỉnh sửa thông tin cá nhân")
    draw_ellipse_uc(ax, 360, 50, "Cài đặt nhận thông báo")

    for y in [510, 410, 310, 210, 120, 50]:
        connect_uc(ax, (130, 300), (250, y))

    arrow_uc(ax, (470, 510), (495, 510), "<<include>>")
    arrow_uc(ax, (490, 410), (470, 410), "<<extend>>")
    arrow_uc(ax, (470, 210), (495, 210), "<<include>>")

    connect_uc(ax, (665, 510), (730, 330))
    connect_uc(ax, (665, 210), (730, 300))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "uc_module1.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_uc_module2():
    fig, ax = plt.subplots(figsize=(10, 7), dpi=220)
    ax.set_xlim(0, 900)
    ax.set_ylim(0, 600)
    ax.axis('off')

    draw_uc_boundary(ax, 220, 20, 540, 560, "PHÂN HỆ 2: TÌM KIẾM & XEM SỰ KIỆN")

    draw_uc_actor(ax, 110, 300, "Khách hàng\n(Customer)")

    draw_ellipse_uc(ax, 380, 510, "Xem sự kiện nổi bật")
    draw_ellipse_uc(ax, 380, 420, "Tìm kiếm sự kiện theo từ khóa")
    draw_ellipse_uc(ax, 380, 330, "Lọc sự kiện (Ngày, Địa điểm,\nThể loại, Giá vé)")
    draw_ellipse_uc(ax, 380, 240, "Xem chi tiết sự kiện & Nghệ sĩ")
    draw_ellipse_uc(ax, 380, 145, "Lưu sự kiện vào yêu thích")
    draw_ellipse_uc(ax, 630, 145, "Nhận thông báo khi mở bán", rx=95, ry=22, bg='#FEF3C7', color='#D97706')
    draw_ellipse_uc(ax, 380, 55, "Chia sẻ thông tin sự kiện")

    for y in [510, 420, 330, 240, 145, 55]:
        connect_uc(ax, (130, 300), (270, y))

    arrow_uc(ax, (535, 145), (490, 145), "<<extend>>")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "uc_module2.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_uc_module3():
    fig, ax = plt.subplots(figsize=(10, 7), dpi=220)
    ax.set_xlim(0, 900)
    ax.set_ylim(0, 600)
    ax.axis('off')

    draw_uc_boundary(ax, 220, 20, 520, 560, "PHÂN HỆ 3: XẾP HÀNG VÀ CHỌN CHỖ")

    draw_uc_actor(ax, 110, 300, "Khách hàng\n(Customer)")
    draw_uc_external(ax, 755, 230, 135, 65, "Bộ đếm thời gian\n(Timer Service)")

    draw_ellipse_uc(ax, 370, 510, "Tham gia hàng đợi ảo (Queue)")
    draw_ellipse_uc(ax, 370, 420, "Theo dõi số thứ tự & Thời gian chờ")
    draw_ellipse_uc(ax, 370, 330, "Xem sơ đồ sân khấu & Ghế trống")
    draw_ellipse_uc(ax, 370, 240, "Chọn vị trí ghế theo khu vực")
    draw_ellipse_uc(ax, 370, 145, "Giữ ghế tạm thời (Lock 10 phút)")
    draw_ellipse_uc(ax, 610, 145, "Giải phóng ghế khi hết hạn", rx=95, ry=22, bg='#FEE2E2', color='#DC2626')
    draw_ellipse_uc(ax, 370, 55, "Hủy chọn ghế / Thoát hàng đợi")

    for y in [510, 420, 330, 240, 145, 55]:
        connect_uc(ax, (130, 300), (260, y))

    arrow_uc(ax, (480, 145), (515, 145), "<<extend>>")
    connect_uc(ax, (705, 145), (755, 250))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "uc_module3.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_uc_module4():
    fig, ax = plt.subplots(figsize=(10.5, 7.2), dpi=220)
    ax.set_xlim(0, 950)
    ax.set_ylim(0, 620)
    ax.axis('off')

    draw_uc_boundary(ax, 220, 20, 540, 580, "PHÂN HỆ 4: TÍNH TIỀN VÀ XUẤT VÉ")

    draw_uc_actor(ax, 110, 310, "Khách hàng\n(Customer)")
    draw_uc_external(ax, 780, 400, 150, 65, "Cổng thanh toán\n(VNPAY / MoMo)")
    draw_uc_external(ax, 780, 130, 150, 65, "Dịch vụ Email\n(Ticket Mailer)")

    draw_ellipse_uc(ax, 370, 530, "Tạo đơn hàng / Hóa đơn mua vé")
    draw_ellipse_uc(ax, 370, 435, "Nhập mã giảm giá (Voucher)")
    draw_ellipse_uc(ax, 625, 435, "Kiểm tra hợp lệ mã voucher", rx=90, ry=22, bg='#FEF3C7', color='#D97706')

    draw_ellipse_uc(ax, 370, 340, "Chọn phương thức thanh toán")
    draw_ellipse_uc(ax, 370, 245, "Thực hiện thanh toán trực tuyến")
    draw_ellipse_uc(ax, 625, 245, "Xác thực OTP & Kết quả GD", rx=90, ry=22, bg='#D1FAE5', color='#059669')

    draw_ellipse_uc(ax, 370, 145, "Xuất vé điện tử QR Code động")
    draw_ellipse_uc(ax, 370, 55, "Lưu vào mục 'Vé của tôi'")

    for y in [530, 435, 340, 245, 145, 55]:
        connect_uc(ax, (130, 310), (260, y))

    arrow_uc(ax, (480, 435), (535, 435), "<<include>>")
    arrow_uc(ax, (480, 245), (535, 245), "<<include>>")

    connect_uc(ax, (715, 245), (780, 430))
    connect_uc(ax, (480, 145), (780, 160))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "uc_module4.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_uc_module5():
    fig, ax = plt.subplots(figsize=(10.5, 7.2), dpi=220)
    ax.set_xlim(0, 950)
    ax.set_ylim(0, 620)
    ax.axis('off')

    draw_uc_boundary(ax, 220, 20, 540, 580, "PHÂN HỆ 5: QUẢN LÝ & THỐNG KÊ DÀNH CHO BAN TỔ CHỨC")

    draw_uc_actor(ax, 110, 310, "Ban tổ chức\n(Organizer)")
    draw_uc_actor(ax, 880, 220, "Quản trị viên\n(Admin)")

    draw_ellipse_uc(ax, 380, 530, "Thiết kế & Tạo sơ đồ ghế sân khấu")
    draw_ellipse_uc(ax, 380, 435, "Đăng bài tạo sự kiện mới")
    draw_ellipse_uc(ax, 380, 340, "Quản lý suất diễn & Cấu hình giá vé")
    draw_ellipse_uc(ax, 380, 245, "Thiết lập đợt bán & Mã khuyến mãi")
    draw_ellipse_uc(ax, 380, 145, "Quản lý danh sách khách & Soát vé")
    draw_ellipse_uc(ax, 380, 55, "Xem báo cáo thống kê doanh thu")
    draw_ellipse_uc(ax, 630, 55, "Xuất báo cáo (Excel/PDF)", rx=85, ry=22, bg='#EFF6FF', color='#2563EB')

    for y in [530, 435, 340, 245, 145, 55]:
        connect_uc(ax, (130, 310), (270, y))

    arrow_uc(ax, (545, 55), (490, 55), "<<extend>>")
    connect_uc(ax, (490, 435), (860, 220))
    connect_uc(ax, (490, 55), (860, 220))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "uc_module5.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)


# ====================================================================
# 2. BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH
# ====================================================================

def gen_analysis_tong_the():
    fig, ax = plt.subplots(figsize=(13, 9.5), dpi=220)
    ax.set_xlim(0, 1250)
    ax.set_ylim(0, 900)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH TỔNG THỂ HỆ THỐNG", fontsize=13, weight='bold', color='#1E3A8A', pad=18)

    # Column 1: Left (x=50)
    b_nd = UMLBox("NguoiDung", ["maNguoiDung", "hoTen", "email", "soDienThoai", "matKhau", "vaiTro"], w=230).place(50, 830)
    b_kh = UMLBox("KhachHang", ["diemTichLuy"], w=110).place(50, 620)
    b_btc = UMLBox("BanToChuc", ["tenToChuc", "maSoThue", "giayPhep"], w=110).place(170, 620)
    b_hd_ao = UMLBox("HangDoiAo", ["maHangDoi", "soThuTu", "thoiGianVao", "trangThaiCho"], w=230).place(50, 480)
    b_giu_ghe = UMLBox("GiuGheTamThoi", ["maGiuGhe", "thoiGianBatDau", "thoiGianHetHan", "trangThai"], w=230).place(50, 280)

    # Column 2: Center (x=460)
    b_dd = UMLBox("DiaDiem", ["maDiaDiem", "tenDiaDiem", "diaChiChiTiet", "sucChuaToiDa"], w=230).place(460, 830)
    b_sd = UMLBox("SoDoGhe", ["maSoDo", "tenSoDo", "kieuSanKhau", "tongSoGhe"], w=230).place(460, 640)
    b_kv = UMLBox("KhuVucGhe", ["maKhuVuc", "tenKhuVuc", "mauSac", "loaiKhuVuc", "soLuongGhe"], w=230).place(460, 460)
    b_ghe = UMLBox("Ghe", ["maGhe", "hangGhe", "soThuTu", "toaDoX", "toaDoY"], w=230).place(460, 260)

    # Column 3: Right (x=870)
    b_sk = UMLBox("SuKien", ["maSuKien", "tenSuKien", "theLoai", "moTa", "hinhAnh", "trangThai"], w=240).place(870, 830)
    b_sdien = UMLBox("SuatDien", ["maSuatDien", "ngayDien", "thoiGianBatDau", "thoiGianKetThuc"], w=240).place(870, 610)
    b_giave = UMLBox("GiaVeKhuVuc", ["maGiaVe", "donGia", "soLuongToiDa"], w=240).place(870, 420)
    b_hd = UMLBox("HoaDon", ["maHoaDon", "ngayTao", "tongTien", "soTienGiam", "trangThai"], w=240).place(870, 260)

    boxes = [b_nd, b_kh, b_btc, b_hd_ao, b_giu_ghe, b_dd, b_sd, b_kv, b_ghe, b_sk, b_sdien, b_giave, b_hd]
    for b in boxes:
        b.draw(ax)

    # Relationships
    draw_inheritance(ax, b_kh.pt('top'), b_nd.pt('bottom', -50))
    draw_inheritance(ax, b_btc.pt('top'), b_nd.pt('bottom', 50))

    draw_assoc(ax, b_dd.right, b_sk.left, mult1="1", mult2="*", label="tổ chức tại")
    draw_assoc(ax, b_dd.bottom, b_sd.top, mult1="1", mult2="*", label="chứa")
    draw_composition(ax, b_sd.bottom, b_kv.top, mult1="1", mult2="*")
    draw_composition(ax, b_kv.bottom, b_ghe.top, mult1="1", mult2="*")

    draw_composition(ax, b_sk.bottom, b_sdien.top, mult1="1", mult2="*")
    draw_assoc(ax, b_sdien.bottom, b_giave.top, mult1="1", mult2="*")
    draw_assoc(ax, b_kv.right, b_giave.left, mult1="1", mult2="*")

    draw_assoc(ax, b_kh.pt('bottom', -20), b_hd_ao.top, mult1="1", mult2="*")
    draw_assoc(ax, b_hd_ao.bottom, b_giu_ghe.top, mult1="1", mult2="*")
    draw_assoc(ax, b_giu_ghe.right, b_ghe.left, mult1="*", mult2="1..*", label="khóa tạm")

    draw_polyline_assoc(ax, [b_btc.right, (350, 560), (350, 750), b_sk.left], mult1="1", mult2="*", label="quản lý")
    draw_polyline_assoc(ax, [b_kh.pt('bottom', 20), (140, 60), (990, 60), b_hd.bottom], mult1="1", mult2="*", label="thanh toán")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "analysis_tong_the.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_analysis_module1():
    fig, ax = plt.subplots(figsize=(10.5, 7.5), dpi=220)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 720)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH - PHÂN HỆ 1: QUẢN LÝ TÀI KHOẢN", fontsize=12, weight='bold', color='#1E3A8A', pad=15)

    b_nd = UMLBox("NguoiDung", ["maNguoiDung", "tenDangNhap", "matKhau", "hoTen", "email", "soDienThoai", "diaChi", "vaiTro", "ngayTao"], w=300).place(350, 660)
    b_kh = UMLBox("KhachHang", ["diemTichLuy", "hangThanhVien"], w=220).place(70, 390)
    b_btc = UMLBox("BanToChuc", ["tenToChuc", "maSoThue", "giayPhep", "thongTinMoTa"], w=220).place(650, 390)
    b_phien = UMLBox("PhienDangNhap", ["maPhien", "tokenXacThuc", "thoiGianBatDau", "thoiGianHetHan"], w=220).place(70, 190)
    b_tb = UMLBox("ThongBao", ["maThongBao", "tieuDe", "noiDung", "thoiGianGui", "daDoc"], w=220).place(650, 190)

    for b in [b_nd, b_kh, b_btc, b_phien, b_tb]:
        b.draw(ax)

    draw_inheritance(ax, b_kh.top, b_nd.pt('bottom', -60))
    draw_inheritance(ax, b_btc.top, b_nd.pt('bottom', 60))

    draw_assoc(ax, b_kh.bottom, b_phien.top, mult1="1", mult2="*", label="sở hữu")
    draw_polyline_assoc(ax, [b_nd.right, (910, b_nd.y - b_nd.h/2), (910, b_tb.y - b_tb.h/2), b_tb.right], mult1="1", mult2="*", label="nhận")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "analysis_module1.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_analysis_module2():
    fig, ax = plt.subplots(figsize=(10, 7.2), dpi=220)
    ax.set_xlim(0, 950)
    ax.set_ylim(0, 650)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH - PHÂN HỆ 2: TÌM KIẾM & XEM SỰ KIỆN", fontsize=12, weight='bold', color='#1E3A8A', pad=15)

    b_sk = UMLBox("SuKien", ["maSuKien", "tenSuKien", "theLoai", "moTa", "hinhAnhPoster", "trangThai"], w=250).place(350, 590)
    b_tl = UMLBox("TheLoai", ["maTheLoai", "tenTheLoai", "moTa"], w=200).place(60, 590)
    b_dd = UMLBox("DiaDiem", ["maDiaDiem", "tenDiaDiem", "diaChiChiTiet", "sucChua"], w=220).place(670, 590)

    b_sdien = UMLBox("SuatDien", ["maSuatDien", "ngayDien", "thoiGianBatDau", "thoiGianKetThuc"], w=250).place(350, 310)
    b_ns = UMLBox("NgheSi", ["maNgheSi", "tenNgheSi", "vaiTro", "tieuSu", "hinhAnh"], w=200).place(60, 310)
    b_yt = UMLBox("SuKienYeuThich", ["maYeuThich", "ngayLuu", "ghiChu"], w=220).place(670, 310)

    for b in [b_sk, b_tl, b_dd, b_sdien, b_ns, b_yt]:
        b.draw(ax)

    draw_assoc(ax, b_tl.right, b_sk.left, mult1="1", mult2="*", label="thuộc")
    draw_assoc(ax, b_sk.right, b_dd.left, mult1="*", mult2="1", label="tổ chức tại")
    draw_composition(ax, b_sk.bottom, b_sdien.top, mult1="1", mult2="*")
    draw_assoc(ax, b_ns.right, b_sdien.left, mult1="*", mult2="*", label="biểu diễn")
    draw_assoc(ax, b_sk.pt('bottom', 80), b_yt.top, mult1="1", mult2="*", label="được lưu")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "analysis_module2.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_analysis_module3():
    fig, ax = plt.subplots(figsize=(10.5, 7.5), dpi=220)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 720)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH - PHÂN HỆ 3: XẾP HÀNG & CHỌN CHỖ", fontsize=12, weight='bold', color='#1E3A8A', pad=15)

    b_sd = UMLBox("SoDoGhe", ["maSoDo", "tenSoDo", "loaiSanKhau", "tongSoGhe"], w=240).place(380, 660)
    b_kv = UMLBox("KhuVucGhe", ["maKhuVuc", "tenKhuVuc", "mauSac", "loaiKhuVuc"], w=240).place(380, 460)
    b_ghe = UMLBox("Ghe", ["maGhe", "hangGhe", "soThuTu", "toaDoX", "toaDoY"], w=240).place(380, 260)

    b_kh = UMLBox("KhachHang", ["maNguoiDung", "hoTen", "email"], w=220).place(60, 580)
    b_hd_ao = UMLBox("HangDoiAo", ["maHangDoi", "soThuTu", "thoiGianVao", "trangThaiCho"], w=220).place(60, 340)
    b_giu_ghe = UMLBox("GiuGheTamThoi", ["maGiuGhe", "thoiGianBatDau", "thoiGianHetHan", "trangThai"], w=240).place(700, 340)

    for b in [b_sd, b_kv, b_ghe, b_kh, b_hd_ao, b_giu_ghe]:
        b.draw(ax)

    draw_composition(ax, b_sd.bottom, b_kv.top, mult1="1", mult2="*")
    draw_composition(ax, b_kv.bottom, b_ghe.top, mult1="1", mult2="*")

    draw_assoc(ax, b_kh.bottom, b_hd_ao.top, mult1="1", mult2="*", label="tham gia")
    draw_polyline_assoc(ax, [b_kh.top, (170, 680), (820, 680), b_giu_ghe.top], mult1="1", mult2="*", label="đặt giữ")
    draw_assoc(ax, b_ghe.right, b_giu_ghe.left, mult1="1..*", mult2="1", label="khóa tạm")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "analysis_module3.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_analysis_module4():
    fig, ax = plt.subplots(figsize=(10, 7.2), dpi=220)
    ax.set_xlim(0, 950)
    ax.set_ylim(0, 650)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH - PHÂN HỆ 4: TÍNH TIỀN & XUẤT VÉ", fontsize=12, weight='bold', color='#1E3A8A', pad=15)

    b_hd = UMLBox("HoaDon", ["maHoaDon", "ngayTao", "tongTienTamTinh", "soTienGiam", "tongTienThanhToan", "trangThai"], w=270).place(340, 590)
    b_mg = UMLBox("MaGiamGia", ["maCode", "tyLeGiam", "giaTriToiDa", "ngayHetHan", "soLuongConLai"], w=220).place(50, 590)
    b_gd = UMLBox("GiaoDichThanhToan", ["maGiaoDich", "phuongThuc", "maThamChieu", "soTien", "trangThai"], w=230).place(670, 590)

    b_ve = UMLBox("Ve", ["maVe", "maQR", "trangThaiVe", "thoiGianCheckin", "donGia"], w=270).place(340, 290)
    b_kh = UMLBox("KhachHang", ["maNguoiDung", "hoTen", "email"], w=220).place(50, 290)
    b_ghe = UMLBox("Ghe", ["maGhe", "hangGhe", "soThuTu"], w=230).place(670, 290)

    for b in [b_hd, b_mg, b_gd, b_ve, b_kh, b_ghe]:
        b.draw(ax)

    draw_assoc(ax, b_mg.right, b_hd.left, mult1="0..1", mult2="*", label="áp dụng")
    draw_assoc(ax, b_hd.right, b_gd.left, mult1="1", mult2="1", label="thực hiện")
    draw_composition(ax, b_hd.bottom, b_ve.top, mult1="1", mult2="1..*")
    draw_assoc(ax, b_kh.right, b_ve.left, mult1="1", mult2="*", label="sở hữu")
    draw_assoc(ax, b_ve.right, b_ghe.left, mult1="1", mult2="1", label="gán với")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "analysis_module4.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_analysis_module5():
    fig, ax = plt.subplots(figsize=(10, 7.2), dpi=220)
    ax.set_xlim(0, 950)
    ax.set_ylim(0, 650)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ PHÂN TÍCH - PHÂN HỆ 5: QUẢN LÝ & THỐNG KÊ BTC", fontsize=12, weight='bold', color='#1E3A8A', pad=15)

    b_btc = UMLBox("BanToChuc", ["maNguoiDung", "tenToChuc", "maSoThue", "giayPhep", "thongTinLienHe"], w=250).place(350, 600)
    b_sk = UMLBox("SuKien", ["maSuKien", "tenSuKien", "theLoai", "moTa", "trangThai"], w=250).place(350, 390)
    b_sd = UMLBox("SoDoGhe", ["maSoDo", "tenSoDo", "loaiSanKhau", "tongSoGhe"], w=220).place(60, 390)
    b_sdien = UMLBox("SuatDien", ["maSuatDien", "ngayDien", "thoiGianBatDau", "thoiGianKetThuc"], w=220).place(670, 390)

    b_kv = UMLBox("KhuVucGhe", ["maKhuVuc", "tenKhuVuc", "mauSac", "soLuongGhe"], w=220).place(60, 160)
    b_gv = UMLBox("GiaVeKhuVuc", ["maGiaVe", "donGia", "soLuongPhatHanh"], w=250).place(350, 160)
    b_bc = UMLBox("BaoCaoDoanhThu", ["maBaoCao", "tongVeBan", "tongDoanhThu", "ngayLap"], w=220).place(670, 160)

    for b in [b_btc, b_sk, b_sd, b_sdien, b_kv, b_gv, b_bc]:
        b.draw(ax)

    draw_assoc(ax, b_btc.bottom, b_sk.top, mult1="1", mult2="*", label="quản lý")
    draw_assoc(ax, b_sd.right, b_sk.left, mult1="1", mult2="*", label="áp dụng")
    draw_composition(ax, b_sk.right, b_sdien.left, mult1="1", mult2="*")
    draw_composition(ax, b_sd.bottom, b_kv.top, mult1="1", mult2="*")
    draw_assoc(ax, b_kv.right, b_gv.left, mult1="1", mult2="*")
    draw_assoc(ax, b_sk.bottom, b_gv.top, mult1="1", mult2="*")
    draw_assoc(ax, b_sdien.bottom, b_bc.top, mult1="1", mult2="1", label="kết xuất")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "analysis_module5.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)


# ====================================================================
# 3. BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ
# ====================================================================

def gen_design_tong_the():
    fig, ax = plt.subplots(figsize=(14, 10.5), dpi=220)
    ax.set_xlim(0, 1350)
    ax.set_ylim(0, 1000)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ TỔNG THỂ HỆ THỐNG", fontsize=13, weight='bold', color='#1E3A8A', pad=18)

    # Col 1: Left (x=50)
    b_user = UMLBox("User",
                    ["- id: Long", "- username: String", "- passwordHash: String", "- email: String", "- role: UserRole"],
                    ["+ login(): boolean", "+ changePassword()"], is_design=True, w=250).place(50, 930)

    b_cust = UMLBox("Customer", ["- points: int"], ["+ addFavorite()"], is_design=True, w=120).place(50, 680)
    b_org = UMLBox("Organizer", ["- taxCode: String"], ["+ createEvent()"], is_design=True, w=120).place(180, 680)

    b_queue = UMLBox("VirtualQueue",
                     ["- id: Long", "- queueNo: int", "- sessionToken: String", "- status: QueueStatus"],
                     ["+ isMyTurn(): boolean", "+ expire(): void"], is_design=True, w=250).place(50, 480)

    b_hold = UMLBox("SeatHold",
                    ["- id: Long", "- holdToken: String", "- expiresAt: LocalDateTime"],
                    ["+ isExpired(): boolean", "+ cancel(): void"], is_design=True, w=250).place(50, 240)

    # Col 2: Center (x=500)
    b_venue = UMLBox("Venue",
                     ["- id: Long", "- name: String", "- address: String", "- maxCapacity: int"],
                     ["+ isAvailable(): boolean"], is_design=True, w=250).place(500, 930)

    b_smap = UMLBox("SeatMap",
                    ["- id: Long", "- name: String", "- stageType: String", "- totalSeats: int"],
                    ["+ validateLayout(): boolean"], is_design=True, w=250).place(500, 700)

    b_szone = UMLBox("SeatZone",
                     ["- id: Long", "- zoneName: String", "- colorHex: String", "- seatCount: int"],
                     ["+ getAvailableCount(): int"], is_design=True, w=250).place(500, 480)

    b_seat = UMLBox("Seat",
                    ["- id: Long", "- rowLabel: String", "- seatNo: int", "- isLocked: boolean"],
                    ["+ lock(): void", "+ isAvailable(): boolean"], is_design=True, w=250).place(500, 240)

    # Col 3: Right (x=950)
    b_event = UMLBox("Event",
                     ["- id: Long", "- title: String", "- category: String", "- status: EventStatus"],
                     ["+ publish(): void", "+ cancel(): void"], is_design=True, w=260).place(950, 930)

    b_show = UMLBox("Showtime",
                    ["- id: Long", "- showDate: LocalDate", "- startTime: LocalTime"],
                    ["+ isUpcoming(): boolean"], is_design=True, w=260).place(950, 700)

    b_order = UMLBox("Order",
                     ["- id: Long", "- orderNo: String", "- totalAmount: double", "- status: OrderStatus"],
                     ["+ calculateTotal(): double", "+ complete(): void"], is_design=True, w=260).place(950, 480)

    b_ticket = UMLBox("Ticket",
                      ["- id: Long", "- ticketCode: String", "- qrCode: String", "- isCheckedIn: boolean"],
                      ["+ generateQR(): String", "+ checkIn(): boolean"], is_design=True, w=260).place(950, 240)

    boxes = [b_user, b_cust, b_org, b_queue, b_hold, b_venue, b_smap, b_szone, b_seat, b_event, b_show, b_order, b_ticket]
    for b in boxes:
        b.draw(ax)

    # Connections
    draw_inheritance(ax, b_cust.pt('top'), b_user.pt('bottom', -50))
    draw_inheritance(ax, b_org.pt('top'), b_user.pt('bottom', 50))

    draw_assoc(ax, b_venue.right, b_event.left, mult1="1", mult2="*", label="hosts at")
    draw_assoc(ax, b_venue.bottom, b_smap.top, mult1="1", mult2="*", label="has")
    draw_composition(ax, b_smap.bottom, b_szone.top, mult1="1", mult2="*")
    draw_composition(ax, b_szone.bottom, b_seat.top, mult1="1", mult2="*")

    draw_composition(ax, b_event.bottom, b_show.top, mult1="1", mult2="*")
    draw_composition(ax, b_order.bottom, b_ticket.top, mult1="1", mult2="1..*")

    draw_assoc(ax, b_seat.right, b_ticket.left, mult1="1", mult2="1", label="maps to")
    draw_assoc(ax, b_hold.right, b_seat.left, mult1="*", mult2="1..*", label="locks")
    draw_assoc(ax, b_queue.bottom, b_hold.top, mult1="1", mult2="*")

    draw_polyline_assoc(ax, [b_org.right, (380, 610), (380, 850), b_event.left], mult1="1", mult2="*", label="creates")
    draw_polyline_assoc(ax, [b_smap.right, (850, 610), (850, 610), b_show.left], mult1="1", mult2="*", label="uses")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "design_tong_the.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_design_module1():
    fig, ax = plt.subplots(figsize=(11, 8), dpi=220)
    ax.set_xlim(0, 1050)
    ax.set_ylim(0, 780)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ - PHÂN HỆ 1: QUẢN LÝ TÀI KHOẢN", fontsize=12, weight='bold', color='#1E3A8A', pad=15)

    b_user = UMLBox("User",
                    ["- id: Long", "- username: String", "- passwordHash: String", "- email: String", "- phone: String", "- role: UserRole"],
                    ["+ authenticate(pwd: String): boolean", "+ changePassword(newPwd: String)", "+ updateInfo(dto: UserDto)"],
                    is_design=True, w=330).place(360, 720)

    b_cust = UMLBox("Customer",
                    ["- rewardPoints: int", "- memberTier: MemberTier"],
                    ["+ addRewardPoints(pts: int)", "+ getOrderHistory(): List"],
                    is_design=True, w=270).place(50, 440)

    b_org = UMLBox("Organizer",
                   ["- orgName: String", "- taxId: String", "- businessLicense: String"],
                   ["+ verifyLicense(): boolean", "+ getManagedEvents(): List"],
                   is_design=True, w=270).place(720, 440)

    b_sess = UMLBox("UserSession",
                    ["- id: Long", "- jwtToken: String", "- expiresAt: LocalDateTime"],
                    ["+ isExpired(): boolean", "+ refreshToken(): String"],
                    is_design=True, w=270).place(50, 210)

    b_noti = UMLBox("Notification",
                    ["- id: Long", "- title: String", "- message: String", "- isRead: boolean"],
                    ["+ markAsRead(): void", "+ sendEmailNotification()"],
                    is_design=True, w=270).place(720, 210)

    for b in [b_user, b_cust, b_org, b_sess, b_noti]:
        b.draw(ax)

    draw_inheritance(ax, b_cust.top, b_user.pt('bottom', -80))
    draw_inheritance(ax, b_org.top, b_user.pt('bottom', 80))

    draw_assoc(ax, b_cust.bottom, b_sess.top, mult1="1", mult2="*", label="has")
    draw_polyline_assoc(ax, [b_user.right, (1020, b_user.y - b_user.h/2), (1020, b_noti.y - b_noti.h/2), b_noti.right], mult1="1", mult2="*", label="receives")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "design_module1.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_design_module2():
    fig, ax = plt.subplots(figsize=(10.5, 7.5), dpi=220)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 700)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ - PHÂN HỆ 2: TÌM KIẾM & XEM SỰ KIỆN", fontsize=12, weight='bold', color='#1E3A8A', pad=15)

    b_ev = UMLBox("Event",
                  ["- id: Long", "- title: String", "- description: String", "- bannerUrl: String", "- status: EventStatus"],
                  ["+ publish(): void", "+ isUpcoming(): boolean", "+ getActiveShowtimes(): List"],
                  is_design=True, w=300).place(350, 640)

    b_cat = UMLBox("Category",
                   ["- id: Long", "- name: String", "- code: String"],
                   ["+ getEvents(): List"],
                   is_design=True, w=240).place(50, 640)

    b_ven = UMLBox("Venue",
                   ["- id: Long", "- name: String", "- address: String", "- capacity: int"],
                   ["+ checkCapacity(): boolean"],
                   is_design=True, w=240).place(710, 640)

    b_show = UMLBox("Showtime",
                    ["- id: Long", "- showDate: LocalDate", "- startTime: LocalTime", "- endTime: LocalTime"],
                    ["+ isAvailableForBooking(): boolean", "+ getAvailableSeats(): int"],
                    is_design=True, w=300).place(350, 330)

    b_art = UMLBox("Artist",
                   ["- id: Long", "- stageName: String", "- bio: String", "- avatarUrl: String"],
                   ["+ getParticipatingEvents(): List"],
                   is_design=True, w=240).place(50, 330)

    b_fav = UMLBox("FavoriteEvent",
                   ["- id: Long", "- customerId: Long", "- savedDate: LocalDateTime"],
                   ["+ notifySaleOpening(): void"],
                   is_design=True, w=240).place(710, 330)

    for b in [b_ev, b_cat, b_ven, b_show, b_art, b_fav]:
        b.draw(ax)

    draw_assoc(ax, b_cat.right, b_ev.left, mult1="1", mult2="*")
    draw_assoc(ax, b_ev.right, b_ven.left, mult1="*", mult2="1")
    draw_composition(ax, b_ev.bottom, b_show.top, mult1="1", mult2="*")
    draw_assoc(ax, b_art.right, b_show.left, mult1="*", mult2="*")
    draw_assoc(ax, b_ev.pt('bottom', 80), b_fav.top, mult1="1", mult2="*")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "design_module2.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_design_module3():
    fig, ax = plt.subplots(figsize=(10.5, 7.5), dpi=220)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 700)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ - PHÂN HỆ 3: XẾP HÀNG & CHỌN CHỖ", fontsize=12, weight='bold', color='#1E3A8A', pad=15)

    b_smap = UMLBox("SeatMap",
                    ["- id: Long", "- mapName: String", "- totalSeats: int", "- layoutSvg: String"],
                    ["+ validateLayout(): boolean", "+ getZones(): List<SeatZone>"],
                    is_design=True, w=270).place(365, 650)

    b_szone = UMLBox("SeatZone",
                     ["- id: Long", "- zoneName: String", "- colorHex: String", "- zoneType: ZoneType"],
                     ["+ getSeats(): List<Seat>", "+ countVacantSeats(): int"],
                     is_design=True, w=270).place(365, 430)

    b_seat = UMLBox("Seat",
                    ["- id: Long", "- rowLabel: String", "- seatNumber: int", "- isLocked: boolean"],
                    ["+ lockSeat(token: String): boolean", "+ unlockSeat(): void", "+ isAvailable(): boolean"],
                    is_design=True, w=270).place(365, 210)

    b_queue = UMLBox("VirtualQueue",
                     ["- id: Long", "- queueNumber: int", "- accessToken: String", "- status: QueueStatus"],
                     ["+ isTurn(): boolean", "+ generateToken(): String", "+ expireToken(): void"],
                     is_design=True, w=260).place(50, 480)

    b_hold = UMLBox("SeatHold",
                    ["- id: Long", "- holdToken: String", "- startTime: LocalDateTime", "- expiresAt: LocalDateTime"],
                    ["+ isExpired(): boolean", "+ getRemainingSeconds(): long", "+ confirmHold(): void"],
                    is_design=True, w=270).place(680, 320)

    for b in [b_smap, b_szone, b_seat, b_queue, b_hold]:
        b.draw(ax)

    draw_composition(ax, b_smap.bottom, b_szone.top, mult1="1", mult2="*")
    draw_composition(ax, b_szone.bottom, b_seat.top, mult1="1", mult2="*")
    draw_polyline_assoc(ax, [b_queue.top, (180, 560), (365, 560)], mult1="1", mult2="*")
    draw_polyline_assoc(ax, [b_seat.right, (650, b_seat.y - b_seat.h/2), (650, b_hold.y - b_hold.h/2), b_hold.left], mult1="1..*", mult2="1", label="locks")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "design_module3.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_design_module4():
    fig, ax = plt.subplots(figsize=(10.5, 7.5), dpi=220)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 700)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ - PHÂN HỆ 4: TÍNH TIỀN & XUẤT VÉ", fontsize=12, weight='bold', color='#1E3A8A', pad=15)

    b_ord = UMLBox("Order",
                   ["- id: Long", "- orderCode: String", "- subTotal: double", "- discount: double", "- finalTotal: double", "- status: OrderStatus"],
                   ["+ calculateFinalTotal(): double", "+ applyVoucher(v: Voucher)", "+ markAsPaid(): void"],
                   is_design=True, w=310).place(345, 650)

    b_vouch = UMLBox("Voucher",
                     ["- id: Long", "- code: String", "- percentOff: double", "- maxDiscount: double", "- validUntil: LocalDate"],
                     ["+ isValid(amount: double): boolean", "+ calculateDiscount(amount: double): double"],
                     is_design=True, w=260).place(40, 650)

    b_pay = UMLBox("PaymentTransaction",
                   ["- id: Long", "- transRef: String", "- method: PaymentMethod", "- transAmount: double", "- status: TransStatus"],
                   ["+ processPayment(): boolean", "+ verifyWebhook(): boolean"],
                   is_design=True, w=280).place(690, 650)

    b_tkt = UMLBox("Ticket",
                   ["- id: Long", "- ticketCode: String", "- qrCodeHash: String", "- price: double", "- isUsed: boolean"],
                   ["+ generateEncryptedQR(): String", "+ checkIn(): boolean", "+ cancelTicket(): void"],
                   is_design=True, w=310).place(345, 320)

    b_seat = UMLBox("Seat",
                    ["- id: Long", "- rowLabel: String", "- seatNumber: int"],
                    ["+ markBooked(): void"],
                    is_design=True, w=240).place(690, 320)

    for b in [b_ord, b_vouch, b_pay, b_tkt, b_seat]:
        b.draw(ax)

    draw_assoc(ax, b_vouch.right, b_ord.left, mult1="0..1", mult2="*")
    draw_assoc(ax, b_ord.right, b_pay.left, mult1="1", mult2="1")
    draw_composition(ax, b_ord.bottom, b_tkt.top, mult1="1", mult2="1..*")
    draw_assoc(ax, b_tkt.right, b_seat.left, mult1="1", mult2="1")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "design_module4.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_design_module5():
    fig, ax = plt.subplots(figsize=(10.5, 7.5), dpi=220)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 700)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THỰC THỂ THIẾT KẾ - PHÂN HỆ 5: QUẢN LÝ & THỐNG KÊ BTC", fontsize=12, weight='bold', color='#1E3A8A', pad=15)

    b_org = UMLBox("Organizer",
                   ["- id: Long", "- companyName: String", "- taxId: String", "- email: String"],
                   ["+ createEvent(dto): Event", "+ updatePricing()", "+ viewReports(): Report"],
                   is_design=True, w=280).place(360, 650)

    b_ev = UMLBox("Event",
                  ["- id: Long", "- title: String", "- status: EventStatus"],
                  ["+ addShowtime(st): void", "+ setSeatMap(sm): void"],
                  is_design=True, w=280).place(360, 420)

    b_smap = UMLBox("SeatMap",
                    ["- id: Long", "- mapName: String", "- totalSeats: int"],
                    ["+ renderSvg(): String", "+ cloneLayout(): SeatMap"],
                    is_design=True, w=250).place(50, 420)

    b_show = UMLBox("Showtime",
                    ["- id: Long", "- showDate: LocalDate", "- startTime: LocalTime"],
                    ["+ isPublished(): boolean"],
                    is_design=True, w=250).place(690, 420)

    b_zp = UMLBox("ZonePricing",
                  ["- id: Long", "- price: double", "- maxQuota: int", "- soldCount: int"],
                  ["+ isSoldOut(): boolean", "+ recordSale(): void"],
                  is_design=True, w=280).place(360, 190)

    b_rep = UMLBox("RevenueReport",
                   ["- id: Long", "- totalTicketsSold: int", "- grossRevenue: double", "- occupancyRate: double"],
                   ["+ exportExcel(): byte[]", "+ exportPdf(): byte[]"],
                   is_design=True, w=250).place(690, 190)

    for b in [b_org, b_ev, b_smap, b_show, b_zp, b_rep]:
        b.draw(ax)

    draw_assoc(ax, b_org.bottom, b_ev.top, mult1="1", mult2="*")
    draw_assoc(ax, b_smap.right, b_ev.left, mult1="1", mult2="*")
    draw_composition(ax, b_ev.right, b_show.left, mult1="1", mult2="*")
    draw_assoc(ax, b_ev.bottom, b_zp.top, mult1="1", mult2="*")
    draw_assoc(ax, b_show.bottom, b_rep.top, mult1="1", mult2="1")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "design_module5.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)


def main():
    print("Generating all 18 UML diagrams (v2 layout)...")
    gen_uc_tong_the()
    gen_uc_module1()
    gen_uc_module2()
    gen_uc_module3()
    gen_uc_module4()
    gen_uc_module5()

    gen_analysis_tong_the()
    gen_analysis_module1()
    gen_analysis_module2()
    gen_analysis_module3()
    gen_analysis_module4()
    gen_analysis_module5()

    gen_design_tong_the()
    gen_design_module1()
    gen_design_module2()
    gen_design_module3()
    gen_design_module4()
    gen_design_module5()
    print("All 18 UML diagrams successfully regenerated!")

if __name__ == "__main__":
    main()
