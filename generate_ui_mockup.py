import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

plt.rcParams['font.family'] = 'Times New Roman'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "diagrams")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_ui_mockup():
    fig, ax = plt.subplots(figsize=(14, 9.5), dpi=220)
    ax.set_xlim(0, 1400)
    ax.set_ylim(0, 950)
    ax.axis('off')

    # Main Window Box
    window_rect = FancyBboxPatch((40, 30), 1320, 890, boxstyle="round,pad=0",
                                 edgecolor='#334155', facecolor='#F8FAFC', lw=1.8, zorder=1)
    ax.add_patch(window_rect)

    # Title Bar
    title_bar = patches.Rectangle((40, 880), 1320, 40, edgecolor='#334155', facecolor='#1E293B', lw=1.8, zorder=2)
    ax.add_patch(title_bar)

    # Window buttons (Mac/modern style)
    for idx, col in enumerate(['#EF4444', '#F59E0B', '#10B981']):
        c = patches.Circle((65 + idx * 22, 900), 6, facecolor=col, edgecolor='none', zorder=3)
        ax.add_patch(c)

    ax.text(700, 900, "HỆ THỐNG ĐẶT VÉ SỰ KIỆN TRỰC TUYẾN - MÀN HÌNH THỐNG KÊ DOANH THU (RevenueReportView)",
            ha='center', va='center', fontsize=11, weight='bold', color='#F8FAFC', zorder=3)

    # =========================================================================
    # FILTER BAR
    # =========================================================================
    filter_box = FancyBboxPatch((60, 800), 1280, 65, boxstyle="round,pad=4",
                                edgecolor='#CBD5E1', facecolor='#FFFFFF', lw=1.2, zorder=2)
    ax.add_patch(filter_box)

    # Filter controls
    ax.text(80, 832, "Chọn sự kiện:", fontsize=9.5, weight='bold', color='#1E293B', va='center')
    cb_event = FancyBboxPatch((170, 815), 360, 34, boxstyle="round,pad=2", edgecolor='#94A3B8', facecolor='#F1F5F9', lw=1.1, zorder=3)
    ax.add_patch(cb_event)
    ax.text(185, 832, "Born Pink World Tour Hanoi 2026   ▼", fontsize=9, color='#0F172A', va='center', zorder=4)

    ax.text(560, 832, "Từ ngày:", fontsize=9.5, weight='bold', color='#1E293B', va='center')
    dp1 = FancyBboxPatch((630, 815), 110, 34, boxstyle="round,pad=2", edgecolor='#94A3B8', facecolor='#FFFFFF', lw=1.1, zorder=3)
    ax.add_patch(dp1)
    ax.text(645, 832, "01/08/2026", fontsize=9, color='#0F172A', va='center', zorder=4)

    ax.text(760, 832, "Đến ngày:", fontsize=9.5, weight='bold', color='#1E293B', va='center')
    dp2 = FancyBboxPatch((840, 815), 110, 34, boxstyle="round,pad=2", edgecolor='#94A3B8', facecolor='#FFFFFF', lw=1.1, zorder=3)
    ax.add_patch(dp2)
    ax.text(855, 832, "30/09/2026", fontsize=9, color='#0F172A', va='center', zorder=4)

    # Buttons
    btn_search = FancyBboxPatch((980, 815), 110, 34, boxstyle="round,pad=2", edgecolor='#1E3A8A', facecolor='#1E3A8A', lw=1.2, zorder=3)
    ax.add_patch(btn_search)
    ax.text(1035, 832, "Tra cứu", ha='center', va='center', fontsize=9.5, weight='bold', color='#FFFFFF', zorder=4)

    btn_excel = FancyBboxPatch((1110, 815), 105, 34, boxstyle="round,pad=2", edgecolor='#15803D', facecolor='#16A34A', lw=1.2, zorder=3)
    ax.add_patch(btn_excel)
    ax.text(1162, 832, "Xuất Excel", ha='center', va='center', fontsize=9, weight='bold', color='#FFFFFF', zorder=4)

    btn_pdf = FancyBboxPatch((1230, 815), 90, 34, boxstyle="round,pad=2", edgecolor='#B91C1C', facecolor='#DC2626', lw=1.2, zorder=3)
    ax.add_patch(btn_pdf)
    ax.text(1275, 832, "In PDF", ha='center', va='center', fontsize=9, weight='bold', color='#FFFFFF', zorder=4)

    # =========================================================================
    # KPI CARDS ROW (4 CARDS)
    # =========================================================================
    def draw_kpi_card(x, y, w, h, title, value, subtext, bg_col, border_col, text_col):
        card = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=4", edgecolor=border_col, facecolor=bg_col, lw=1.4, zorder=2)
        ax.add_patch(card)
        ax.text(x + 16, y + h - 22, title.upper(), fontsize=8.5, weight='bold', color='#475569', zorder=3)
        ax.text(x + 16, y + h - 55, value, fontsize=15, weight='bold', color=text_col, zorder=3)
        ax.text(x + 16, y + 16, subtext, fontsize=8.0, color='#64748B', style='italic', zorder=3)

    card_w = 300
    card_h = 105
    card_y = 675

    draw_kpi_card(60, card_y, card_w, card_h,
                  "Tổng doanh thu gộp (Gross Revenue)", "15.450.000.000 đ", "Đã thanh toán 18.500 vé",
                  '#EFF6FF', '#2563EB', '#1E3A8A')

    draw_kpi_card(385, card_y, card_w, card_h,
                  "Doanh thu thuần (Net Revenue)", "13.132.500.000 đ", "Sau khấu trừ 10% VAT & 5% phí sàn",
                  '#F0FDF4', '#16A34A', '#15803D')

    draw_kpi_card(710, card_y, card_w, card_h,
                  "Tỷ lệ lấp đầy (Occupancy Rate)", "92.5 %", "Hiệu suất: EXCELLENT (Cháy vé)",
                  '#FEFCE8', '#CA8A04', '#854D0E')

    draw_kpi_card(1035, card_y, card_w, card_h,
                  "Giá vé bình quân (Average Price)", "835.135 đ / vé", "Phát hành: 20.000 vé toàn sân",
                  '#FAF5FF', '#9333EA', '#6B21A8')

    # =========================================================================
    # ROW 2: CHART (LEFT) & TABLE (RIGHT)
    # =========================================================================
    # Panel Left: Chart
    chart_panel = FancyBboxPatch((60, 60), 450, 595, boxstyle="round,pad=4",
                                 edgecolor='#CBD5E1', facecolor='#FFFFFF', lw=1.2, zorder=2)
    ax.add_patch(chart_panel)
    ax.text(80, 625, "PHÂN BỔ DOANH THU THEO PHÂN KHU (Zone Contribution)", fontsize=10, weight='bold', color='#1E293B', zorder=3)

    # Draw Pie Chart inside left panel
    # Center (285, 380)
    pie_center = (285, 390)
    pie_radius = 120
    wedge_colors = ['#2563EB', '#38BDF8', '#F59E0B', '#10B981']
    percentages = [45.3, 27.2, 17.5, 10.0]
    labels = ['VIP: 45.3%', 'CAT 1: 27.2%', 'CAT 2: 17.5%', 'STANDING: 10.0%']
    
    # Draw simple donut/pie representation
    start_angle = 0
    for idx, pct in enumerate(percentages):
        angle = pct * 3.6
        w = patches.Wedge(pie_center, pie_radius, start_angle, start_angle + angle,
                          facecolor=wedge_colors[idx], edgecolor='#FFFFFF', lw=1.5, zorder=3)
        ax.add_patch(w)
        start_angle += angle

    # Center white hole for donut effect
    hole = patches.Circle(pie_center, 55, facecolor='#FFFFFF', edgecolor='#E2E8F0', lw=1.2, zorder=4)
    ax.add_patch(hole)
    ax.text(pie_center[0], pie_center[1] + 6, "15.45 TỶ", ha='center', va='center', fontsize=11, weight='bold', color='#0F172A', zorder=5)
    ax.text(pie_center[0], pie_center[1] - 12, "Doanh thu", ha='center', va='center', fontsize=8, color='#64748B', zorder=5)

    # Legend for chart
    for idx, (lbl, col) in enumerate(zip(labels, wedge_colors)):
        ly = 200 - idx * 28
        box_leg = patches.Rectangle((120, ly - 6), 14, 14, facecolor=col, edgecolor='none', zorder=3)
        ax.add_patch(box_leg)
        ax.text(145, ly + 2, lbl, fontsize=9, color='#1E293B', va='center', zorder=3)

    # Panel Right: Detailed Table
    table_panel = FancyBboxPatch((530, 60), 810, 595, boxstyle="round,pad=4",
                                  edgecolor='#CBD5E1', facecolor='#FFFFFF', lw=1.2, zorder=2)
    ax.add_patch(table_panel)
    ax.text(550, 625, "BẢNG CHI TIẾT DOANH THU TỪNG PHÂN KHU (Zone Breakdown Table)", fontsize=10, weight='bold', color='#1E293B', zorder=3)

    # Draw Table
    headers = ["Phân khu (Zone)", "Đơn giá (Price)", "Chỉ tiêu", "Đã bán", "Tỷ lệ lấp đầy", "Doanh thu gộp", "Tỷ trọng"]
    col_x = [550, 670, 780, 860, 940, 1060, 1220]
    row_y = 575

    # Table Header Row
    hdr_bg = patches.Rectangle((540, row_y - 12), 790, 30, facecolor='#1E3A8A', edgecolor='none', zorder=3)
    ax.add_patch(hdr_bg)
    for i, h_name in enumerate(headers):
        ax.text(col_x[i], row_y + 3, h_name, fontsize=8.5, weight='bold', color='#FFFFFF', va='center', zorder=4)

    table_data = [
        ["VIP", "3.500.000 đ", "2.000", "2.000", "100.0 %", "7.000.000.000 đ", "45.3 %"],
        ["CAT 1", "2.100.000 đ", "2.000", "2.000", "100.0 %", "4.200.000.000 đ", "27.2 %"],
        ["CAT 2", "1.350.000 đ", "2.000", "2.000", "100.0 %", "2.700.000.000 đ", "17.5 %"],
        ["STANDING", "1.100.000 đ", "14.000", "12.500", "89.3 %", "1.550.000.000 đ", "10.0 %"]
    ]

    cur_y = row_y - 40
    for r_idx, r_data in enumerate(table_data):
        row_bg_col = '#F8FAFC' if r_idx % 2 == 1 else '#FFFFFF'
        r_bg = patches.Rectangle((540, cur_y - 10), 790, 30, facecolor=row_bg_col, edgecolor='#E2E8F0', lw=0.8, zorder=3)
        ax.add_patch(r_bg)
        for c_idx, val in enumerate(r_data):
            weight = 'bold' if c_idx == 0 or c_idx == 5 else 'normal'
            color = '#1D4ED8' if c_idx == 5 else ('#047857' if c_idx == 4 else '#1E293B')
            ax.text(col_x[c_idx], cur_y + 4, val, fontsize=8.5, weight=weight, color=color, va='center', zorder=4)
        cur_y -= 34

    # Summary Row
    sum_bg = patches.Rectangle((540, cur_y - 12), 790, 34, facecolor='#FEF3C7', edgecolor='#F59E0B', lw=1.2, zorder=3)
    ax.add_patch(sum_bg)
    sum_data = ["TỔNG CỘNG", "-", "20.000", "18.500", "92.5 %", "15.450.000.000 đ", "100.0 %"]
    for c_idx, val in enumerate(sum_data):
        ax.text(col_x[c_idx], cur_y + 5, val, fontsize=9, weight='bold', color='#92400E', va='center', zorder=4)

    # Sub-note under table
    cur_y -= 45
    ax.text(550, cur_y, "• Đánh giá hiệu suất: EXCELLENT (Cháy vé toàn bộ các phân khu VIP, CAT 1, CAT 2)",
            fontsize=8.5, weight='bold', color='#15803D', zorder=4)
    cur_y -= 22
    ax.text(550, cur_y, "• Thuế VAT 10% (1.545.000.000 đ) và Phí nền tảng 5% (772.500.000 đ) đã được khấu trừ tự động vào Doanh thu thuần.",
            fontsize=8.0, color='#64748B', style='italic', zorder=4)
    cur_y -= 22
    ax.text(550, cur_y, "• Thời gian cập nhật số liệu: 23/09/2026 15:30:00 (Hệ thống tính toán thời gian thực theo giao dịch đã thanh toán thành công).",
            fontsize=8.0, color='#64748B', style='italic', zorder=4)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "ui_m5_view_revenue.png")
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("UI Mockup generated successfully at:", path)

if __name__ == "__main__":
    generate_ui_mockup()
