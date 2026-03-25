# 📰 Automated News Scraper

Dự án sử dụng Python để tự động hóa quy trình thu thập dữ liệu từ báo điện tử, thay thế thao tác sao chép thủ công.

## 🛠 Đặc tính kỹ thuật
- **Parsing Engine:** BeautifulSoup4 & Requests.
- **Data Processing:** Sử dụng **Regex** để lọc ngày tháng chuẩn `DD/MM/YYYY`.
- **Output:** Xuất file CSV định dạng `utf-8-sig` tương thích hoàn toàn với Excel.

## 🚀 Cách sử dụng
1. Cài đặt thư viện: `pip install requests beautifulsoup4`
2. Chạy script: `python main.py`
3. Nhập URL và nhận kết quả tại file `data_chuan_hoa.csv`.