import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

plt.rcParams['font.family'] = 'Times New Roman'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "diagrams")
os.makedirs(OUTPUT_DIR, exist_ok=True)

class DetailedUMLBox:
    def __init__(self, stereotype, name, attrs=None, methods=None, w=280, bg_hdr='#BFDBFE', border='#1E3A8A'):
        self.stereotype = stereotype
        self.name = name
        self.attrs = attrs or []
        self.methods = methods or []
        self.w = w
        self.bg_hdr = bg_hdr
        self.border = border
        
        self.line_h = 19
        self.h_hdr = 38
        self.h_attrs = max(len(self.attrs) * self.line_h + 12, 24)
        self.h_methods = max(len(self.methods) * self.line_h + 12, 24)
        self.h = self.h_hdr + self.h_attrs + self.h_methods
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
        rect = patches.Rectangle((self.x, self.y - self.h), self.w, self.h,
                                 edgecolor=self.border, facecolor='#FFFFFF', lw=1.5, zorder=3)
        ax.add_patch(rect)

        hdr_rect = patches.Rectangle((self.x, self.y - self.h_hdr), self.w, self.h_hdr,
                                     edgecolor=self.border, facecolor=self.bg_hdr, lw=1.5, zorder=4)
        ax.add_patch(hdr_rect)

        ax.text(self.x + self.w / 2, self.y - 12, f'<<{self.stereotype}>>', ha='center', va='center',
                fontsize=8.0, style='italic', color='#1E3A8A', zorder=5)
        ax.text(self.x + self.w / 2, self.y - 27, self.name, ha='center', va='center',
                fontsize=10.0, weight='bold', color='#0F172A', zorder=5)
        
        sep_y = self.y - self.h_hdr - self.h_attrs
        ax.plot([self.x, self.x + self.w], [sep_y, sep_y], color=self.border, lw=1.1, zorder=4)

        cur_y = self.y - self.h_hdr - 14
        for a in self.attrs:
            ax.text(self.x + 10, cur_y, a, ha='left', va='center',
                    fontsize=8.0, color='#1E293B', fontfamily='Consolas', zorder=5)
            cur_y -= self.line_h

        cur_y = sep_y - 14
        for m in self.methods:
            # Highlight calculation methods
            is_calc = any(kw in m for kw in ['calculate', 'compute', 'evaluate', 'getSoldRate', 'Contribution'])
            color = '#1E3A8A' if is_calc else '#1E293B'
            weight = 'bold' if is_calc else 'normal'
            ax.text(self.x + 10, cur_y, m, ha='left', va='center',
                    fontsize=8.0, color=color, weight=weight, fontfamily='Consolas', zorder=5)
            cur_y -= self.line_h

def draw_uc_actor(ax, x, y, name, color='#1E3A8A'):
    circle = patches.Circle((x, y + 25), 12, edgecolor=color, facecolor='#DBEAFE', lw=2, zorder=5)
    ax.add_patch(circle)
    ax.plot([x, x], [y + 13, y - 20], color=color, lw=2.2, zorder=5)
    ax.plot([x - 20, x + 20], [y, y], color=color, lw=2.2, zorder=5)
    ax.plot([x, x - 18], [y - 20, y - 50], color=color, lw=2.2, zorder=5)
    ax.plot([x, x + 18], [y - 20, y - 50], color=color, lw=2.2, zorder=5)
    ax.text(x, y - 70, name, ha='center', va='top', fontsize=9.5, weight='bold', color='#0F172A', zorder=5)

def draw_ellipse_uc(ax, cx, cy, text, rx=110, ry=26, color='#1D4ED8', bg='#EFF6FF'):
    ellipse = patches.Ellipse((cx, cy), rx*2, ry*2, edgecolor=color, facecolor=bg, lw=1.5, zorder=4)
    ax.add_patch(ellipse)
    ax.text(cx, cy, text, ha='center', va='center', fontsize=8.8, color='#0F172A', zorder=5, multialignment='center')

def draw_uc_boundary(ax, x, y, w, h, title):
    rect = patches.Rectangle((x, y), w, h, edgecolor='#94A3B8', facecolor='#F8FAFC', lw=1.6, linestyle='--', zorder=1)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h - 22, title, ha='center', va='center', fontsize=11.5, weight='bold', color='#1E293B', zorder=2)

def connect_uc(ax, p1, p2, color='#64748B', lw=1.3):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, lw=lw, zorder=3)

def arrow_uc(ax, p1, p2, label="", color='#2563EB'):
    ax.annotate("", xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle="->", color=color, lw=1.3, linestyle="--"), zorder=4)
    if label:
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + 8
        ax.text(mx, my, label, ha='center', va='center', fontsize=8, color=color, style='italic',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFFFFF', edgecolor='none', alpha=0.9), zorder=5)

def gen_m5_detailed_uc_diagram():
    fig, ax = plt.subplots(figsize=(12, 8.5), dpi=220)
    ax.set_xlim(0, 1100)
    ax.set_ylim(0, 750)
    ax.axis('off')

    draw_uc_boundary(ax, 210, 30, 680, 690, "CHỨC NĂNG: XEM THỐNG KÊ DOANH THU SỰ KIỆN")

    # Actors
    draw_uc_actor(ax, 100, 380, "Ban tổ chức\n(Organizer)")
    draw_uc_actor(ax, 990, 380, "Quản trị viên\n(Admin)")

    # Central Use Case
    draw_ellipse_uc(ax, 550, 380, "Xem thống kê\ndoanh thu sự kiện", rx=130, ry=34, color='#1E3A8A', bg='#BFDBFE')

    # <<include>> Use Cases
    draw_ellipse_uc(ax, 550, 610, "Chọn sự kiện cần thống kê", rx=115, ry=26, bg='#FEF3C7', color='#D97706')
    draw_ellipse_uc(ax, 360, 500, "Tổng hợp & Tính toán KPIs\n(Doanh thu & Tỷ lệ lấp đầy)", rx=125, ry=28, bg='#FEF3C7', color='#D97706')

    # <<extend>> Use Cases
    draw_ellipse_uc(ax, 740, 500, "Lọc theo suất diễn\n& khoảng ngày", rx=115, ry=26, bg='#F1F5F9', color='#475569')
    draw_ellipse_uc(ax, 380, 180, "Xem chi tiết phân bổ\ndoanh thu theo phân khu", rx=125, ry=28, bg='#EFF6FF', color='#2563EB')
    draw_ellipse_uc(ax, 720, 180, "Xuất báo cáo doanh thu\n(Excel / PDF)", rx=120, ry=28, bg='#EFF6FF', color='#2563EB')

    # Connect Actors to Central UC
    connect_uc(ax, (120, 380), (420, 380))
    connect_uc(ax, (970, 380), (680, 380))

    # <<include>> arrows (from central UC to included UC)
    arrow_uc(ax, (550, 414), (550, 584), "<<include>>")
    arrow_uc(ax, (470, 405), (410, 472), "<<include>>")

    # <<extend>> arrows (from extending UC to central UC)
    arrow_uc(ax, (690, 474), (630, 405), "<<extend>>")
    arrow_uc(ax, (430, 208), (510, 346), "<<extend>>")
    arrow_uc(ax, (670, 208), (590, 346), "<<extend>>")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "uc_m5_view_revenue_detail.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def draw_assoc(ax, p1, p2, mult1="", mult2="", label="", color='#334155'):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, lw=1.3, zorder=2)
    if mult1:
        ax.text(p1[0] + 6, p1[1] + 6, mult1, fontsize=8, color='#334155', weight='bold', zorder=5)
    if mult2:
        ax.text(p2[0] - 16, p2[1] + 6, mult2, fontsize=8, color='#334155', weight='bold', zorder=5)
    if label:
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + 6
        ax.text(mx, my, label, ha='center', va='bottom', fontsize=7.8, color='#0F172A', style='italic', zorder=5)

def draw_dependency(ax, p1, p2, label="", color='#2563EB'):
    ax.annotate("", xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle="->", color=color, lw=1.3, linestyle="--"), zorder=4)
    if label:
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + 6
        ax.text(mx, my, label, ha='center', va='bottom', fontsize=7.8, color=color, style='italic', zorder=5)

def gen_m5_detailed_class_diagram():
    fig, ax = plt.subplots(figsize=(14.5, 9.5), dpi=220)
    ax.set_xlim(0, 1450)
    ax.set_ylim(0, 950)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP THIẾT KẾ CHI TIẾT (BCE & DTO) - CHỨC NĂNG: XEM THỐNG KÊ DOANH THU SỰ KIỆN",
              fontsize=13, weight='bold', color='#1E3A8A', pad=15)

    # Row 1: Boundary, Control, Entity RevenueReport, Enum PerformanceStatus
    b_view = DetailedUMLBox("boundary", "RevenueReportView",
                            ["- eventSelector: ComboBox", "- kpiPanel: Panel", "- zoneChart: ChartView"],
                            ["+ onSelectEvent(eventId: Long): void",
                             "+ displayKPIs(dto: RevenueSummaryDto): void",
                             "+ renderZoneChart(data: List<ZoneRevenueDto>): void",
                             "+ showError(msg: String): void"],
                            w=270, bg_hdr='#E0E7FF').place(40, 890)

    b_ctrl = DetailedUMLBox("control", "RevenueReportController",
                            ["- reportService: ReportService", "- eventRepo: EventRepository"],
                            ["+ handleViewReport(eventId: Long): RevenueSummaryDto",
                             "+ calculateZoneAnalytics(eventId: Long): List<ZoneRevenueDto>",
                             "+ formatReportData(report: RevenueReport): RevenueSummaryDto"],
                            w=310, bg_hdr='#FEF08A', border='#CA8A04').place(360, 890)

    b_rep = DetailedUMLBox("entity", "RevenueReport",
                           ["- reportId: Long",
                            "- eventId: Long",
                            "- calculatedAt: LocalDateTime",
                            "- taxRate: double",
                            "- platformCommissionRate: double",
                            "- zonePricings: List<ZonePricing>"],
                           ["+ calculateTotalCapacity(): int",
                            "+ calculateTotalTicketsSold(): int",
                            "+ calculateGrossRevenue(): double",
                            "+ calculateNetRevenue(): double",
                            "+ calculateOccupancyRate(): double",
                            "+ calculateAverageTicketPrice(): double",
                            "+ calculateZoneContribution(zoneId: Long): double",
                            "+ evaluatePerformance(): PerformanceStatus"],
                           w=380, bg_hdr='#BFDBFE', border='#1E3A8A').place(720, 890)

    b_enum = DetailedUMLBox("enum", "PerformanceStatus",
                            ["EXCELLENT (>= 85%)", "GOOD (70% - 84%)", "AVERAGE (50% - 69%)", "POOR (< 50%)"],
                            [], w=240, bg_hdr='#F1F5F9', border='#64748B').place(1150, 890)

    # Row 2: DTO, ZonePricing, Showtime, Event
    b_dto = DetailedUMLBox("dto", "RevenueSummaryDto",
                           ["- grossRevenue: double",
                            "- netRevenue: double",
                            "- occupancyRate: double",
                            "- averagePrice: double",
                            "- status: PerformanceStatus",
                            "- zoneBreakdowns: List"],
                           ["+ getGrossRevenue(): double",
                            "+ getNetRevenue(): double",
                            "+ getOccupancyRate(): double"],
                           w=270, bg_hdr='#DCFCE7', border='#15803D').place(40, 480)

    b_zp = DetailedUMLBox("entity", "ZonePricing",
                          ["- id: Long", "- zoneName: String", "- price: double", "- maxQuota: int", "- soldCount: int"],
                          ["+ calculateZoneGross(): double",
                           "+ calculateRemainingSeats(): int",
                           "+ getSoldRate(): double",
                           "+ isSoldOut(): boolean"],
                          w=320, bg_hdr='#BFDBFE').place(360, 480)

    b_show = DetailedUMLBox("entity", "Showtime",
                            ["- id: Long", "- showDate: LocalDate", "- startTime: LocalTime"],
                            ["+ calculateShowtimeRevenue(): double", "+ getSoldTicketsCount(): int"],
                            w=310, bg_hdr='#BFDBFE').place(740, 480)

    b_ev = DetailedUMLBox("entity", "Event",
                          ["- id: Long", "- title: String", "- status: EventStatus"],
                          ["+ getTotalCapacity(): int", "+ getActiveShowtimes(): List<Showtime>"],
                          w=280, bg_hdr='#BFDBFE').place(1110, 480)

    boxes = [b_view, b_ctrl, b_rep, b_enum, b_dto, b_zp, b_show, b_ev]
    for b in boxes:
        b.draw(ax)

    # Relationships
    draw_dependency(ax, b_view.right, b_ctrl.left, label="triggers")
    draw_dependency(ax, b_ctrl.right, b_rep.left, label="invokes")
    draw_dependency(ax, b_rep.right, b_enum.left, label="evaluates to")

    draw_dependency(ax, b_ctrl.pt('bottom', -50), b_dto.top, label="creates DTO")
    draw_dependency(ax, b_dto.pt('top', -40), b_view.bottom, label="displays")

    draw_assoc(ax, b_rep.pt('bottom', -80), b_zp.top, mult1="1", mult2="*", label="aggregates")
    draw_assoc(ax, b_rep.pt('bottom', 80), b_show.top, mult1="1", mult2="*", label="summarizes")
    draw_assoc(ax, b_ev.left, b_show.right, mult1="1", mult2="*")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "design_m5_view_revenue_detail.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_m5_sequence_diagram():
    fig, ax = plt.subplots(figsize=(13.5, 9.0), dpi=220)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 750)
    ax.axis('off')

    plt.title("BIỂU ĐỒ TUẦN TỰ (SEQUENCE DIAGRAM) - CHỨC NĂNG: XEM THỐNG KÊ DOANH THU SỰ KIỆN",
              fontsize=12.5, weight='bold', color='#1E3A8A', pad=15)

    # Lifelines
    lifelines = [
        ("Organizer\n(Actor)", 90),
        (":RevenueReportView\n(Boundary)", 300),
        (":RevenueReportController\n(Control)", 530),
        ("report:RevenueReport\n(Entity)", 760),
        ("p:ZonePricing\n(Entity)", 930)
    ]

    y_top = 670
    y_bot = 60

    for name, x in lifelines:
        # Box header
        rect = patches.Rectangle((x - 65, y_top - 35), 130, 35,
                                 edgecolor='#1E3A8A', facecolor='#EFF6FF', lw=1.4, zorder=3)
        ax.add_patch(rect)
        ax.text(x, y_top - 18, name, ha='center', va='center', fontsize=8.5, weight='bold', color='#0F172A', zorder=4)
        # Vertical dashed line
        ax.plot([x, x], [y_top - 35, y_bot], color='#94A3B8', linestyle='--', lw=1.2, zorder=1)

    # Execution bars
    def draw_exec(x, y1, y2, color='#DBEAFE'):
        rect = patches.Rectangle((x - 6, y2), 12, y1 - y2,
                                 edgecolor='#1E3A8A', facecolor=color, lw=1.2, zorder=2)
        ax.add_patch(rect)

    draw_exec(90, 620, 100)
    draw_exec(300, 610, 110)
    draw_exec(530, 590, 130)
    draw_exec(760, 560, 200)
    draw_exec(930, 480, 420)

    # Messages
    def msg(y, x1, x2, text, is_ret=False, color='#1E3A8A'):
        ls = '--' if is_ret else '-'
        arr = '->' if not is_ret else '-->'
        ax.annotate("", xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.3, linestyle=ls), zorder=4)
        mx = (x1 + x2) / 2
        ax.text(mx, y + 6, text, ha='center', va='bottom', fontsize=8.0, color='#0F172A',
                bbox=dict(boxstyle='round,pad=0.15', facecolor='#FFFFFF', edgecolor='none', alpha=0.9), zorder=5)

    msg(610, 90, 300, "1. onSelectEvent(eventId)")
    msg(580, 300, 530, "2. handleViewReport(eventId)")
    msg(550, 530, 760, "3. <<create>> (eventId, taxRate, feeRate)")

    msg(500, 760, 760 + 50, "4. calculateGrossRevenue()")
    # Self-call loop
    ax.annotate("", xy=(760, 480), xytext=(760 + 50, 500),
                arrowprops=dict(arrowstyle="->", color='#1E3A8A', lw=1.2), zorder=4)

    msg(460, 760, 930, "5. [loop] calculateZoneGross()")
    msg(430, 930, 760, "6. return zoneGrossAmount", is_ret=True)

    msg(380, 530, 760, "7. calculateNetRevenue()")
    msg(340, 530, 760, "8. calculateOccupancyRate()")
    msg(300, 530, 760, "9. evaluatePerformance()")
    msg(260, 760, 530, "10. return PerformanceStatus (EXCELLENT)", is_ret=True)

    msg(210, 530, 530 + 50, "11. formatReportData()")
    ax.annotate("", xy=(530, 190), xytext=(530 + 50, 210),
                arrowprops=dict(arrowstyle="->", color='#1E3A8A', lw=1.2), zorder=4)

    msg(160, 530, 300, "12. return RevenueSummaryDto", is_ret=True)
    msg(120, 300, 90, "13. displayKPIs & renderZoneChart()", is_ret=True)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "seq_m5_view_revenue.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def gen_m5_analysis_class_diagram():
    fig, ax = plt.subplots(figsize=(14, 9.5), dpi=220)
    ax.set_xlim(0, 1400)
    ax.set_ylim(0, 950)
    ax.axis('off')

    plt.title("BIỂU ĐỒ LỚP PHÂN TÍCH (ANALYSIS CLASS DIAGRAM) - CHỨC NĂNG: XEM THỐNG KÊ DOANH THU SỰ KIỆN",
              fontsize=12.5, weight='bold', color='#1E3A8A', pad=15)

    # 1. Organizer (Actor / Entity)
    b_org = DetailedUMLBox("analysis", "Organizer",
                           ["userId", "companyName", "taxId", "email"],
                           ["+ selectEvent()", "+ viewRevenueReport()"],
                           w=260, bg_hdr='#DBEAFE', border='#1E3A8A').place(50, 890)

    # 2. Event (Entity)
    b_ev = DetailedUMLBox("analysis", "Event",
                          ["eventId", "title", "category", "status"],
                          ["+ getTotalCapacity()", "+ getShowtimes()"],
                          w=260, bg_hdr='#DBEAFE', border='#1E3A8A').place(50, 520)

    # 3. RevenueReport (Core Entity with computational methods)
    b_rep = DetailedUMLBox("analysis", "RevenueReport",
                           ["reportId", "eventId", "calculatedAt", "taxRate", "platformFeeRate",
                            "totalTicketsSold", "grossRevenue", "netRevenue", "occupancyRate"],
                           ["+ calculateTotalCapacity()",
                            "+ calculateTotalTicketsSold()",
                            "+ calculateGrossRevenue()",
                            "+ calculateNetRevenue()",
                            "+ calculateOccupancyRate()",
                            "+ calculateAverageTicketPrice()",
                            "+ calculateZoneContribution(zoneId)",
                            "+ evaluatePerformance()"],
                           w=380, bg_hdr='#BFDBFE', border='#1E3A8A').place(440, 890)

    # 4. ZonePricing (Entity with calculations)
    b_zp = DetailedUMLBox("analysis", "ZonePricing",
                          ["pricingId", "zoneName", "price", "maxQuota", "soldCount"],
                          ["+ calculateZoneGross()",
                           "+ calculateRemainingSeats()",
                           "+ getSoldRate()"],
                          w=310, bg_hdr='#DBEAFE', border='#1E3A8A').place(440, 420)

    # 5. Showtime (Entity with calculations)
    b_show = DetailedUMLBox("analysis", "Showtime",
                            ["showtimeId", "showDate", "startTime", "endTime"],
                            ["+ calculateShowtimeRevenue()",
                             "+ getSoldTicketsCount()"],
                            w=310, bg_hdr='#DBEAFE', border='#1E3A8A').place(930, 890)

    # 6. SeatZone (Entity)
    b_sz = DetailedUMLBox("analysis", "SeatZone",
                          ["zoneId", "zoneName", "colorHex", "seatCount"],
                          ["+ countTotalSeats()"],
                          w=310, bg_hdr='#DBEAFE', border='#1E3A8A').place(930, 420)

    boxes = [b_org, b_ev, b_rep, b_zp, b_show, b_sz]
    for b in boxes:
        b.draw(ax)

    # Relationships
    draw_assoc(ax, b_org.bottom, b_ev.top, mult1="1", mult2="*", label="manages")
    draw_assoc(ax, b_org.right, b_rep.left, mult1="1", mult2="*", label="requests")
    draw_assoc(ax, b_ev.right, b_zp.left, mult1="1", mult2="*", label="configures")
    draw_assoc(ax, b_rep.bottom, b_zp.top, mult1="1", mult2="*", label="aggregates")
    draw_assoc(ax, b_rep.right, b_show.left, mult1="1", mult2="*", label="summarizes")
    draw_assoc(ax, b_zp.right, b_sz.left, mult1="*", mult2="1", label="maps to")
    draw_assoc(ax, b_show.bottom, b_zp.pt('right', 30), mult1="1", mult2="*", label="prices via")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "analysis_m5_view_revenue_detail.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

def main():
    print("Generating detailed UC, design, and analysis diagrams for Module 5 key use case...")
    gen_m5_detailed_uc_diagram()
    gen_m5_analysis_class_diagram()
    gen_m5_detailed_class_diagram()
    gen_m5_sequence_diagram()
    print("Done generating all M5 key use case diagrams!")

if __name__ == "__main__":
    main()
