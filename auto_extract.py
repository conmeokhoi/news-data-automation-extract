import requests
from bs4 import BeautifulSoup
import csv
import os
import re

def clean_date(raw_date):
    # Sử dụng Regex để tìm mẫu ngày/tháng/năm (DD/MM/YYYY)
    match = re.search(r'\d{2}/\d{2}/\d{4}', raw_date)
    return match.group(0) if match else "N/A"

def clean_author(raw_author):
    # Nếu có dấu ":" (ví dụ: "Bài và ảnh: Trần Văn A"), lấy phần sau dấu ":"
    if ":" in raw_author:
        raw_author = raw_author.split(":")[-1]
    # Loại bỏ các từ khóa thừa phổ biến (nếu có)
    prefixes = ["Theo", "Ảnh", "Tin"]
    for p in prefixes:
        raw_author = raw_author.replace(p, "")
    return raw_author.strip()

def auto_newspaper_scraper():
    print("--- CÔNG CỤ TRÍCH XUẤT & LỌC DỮ LIỆU CHUẨN ---")
    url = input("Nhập URL tờ báo: ").strip()
    
    if not url.startswith("http"):
        print("Lỗi: URL không hợp lệ.")
        return

    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. Trích xuất thô
        title_raw = soup.select_one('.detail-title')
        time_raw = soup.select_one('.detail-time')
        author_raw = soup.select_one('.detail-author')

        # 2. Làm sạch dữ liệu (Data Cleaning)
        title = title_raw.get_text().strip() if title_raw else "N/A"
        date_only = clean_date(time_raw.get_text()) if time_raw else "N/A"
        author_only = clean_author(author_raw.get_text()) if author_raw else "N/A"

        data = {
            "Tiêu đề": title,
            "Ngày đăng": date_only,
            "Tác giả": author_only,
            "Đường dẫn": url
        }

        # 3. Lưu file CSV
        file_name = "data_chuan_hoa.csv"
        file_exists = os.path.isfile(file_name)

        with open(file_name, mode='a', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

        print("\n" + "="*50)
        print(f"[XÁC NHẬN] Đã trích xuất xong!")
        print(f"-> Ngày: {date_only}")
        print(f"-> Tác giả: {author_only}")
        print(f"-> File lưu tại: {os.path.abspath(file_name)}")
        print("="*50)

    except Exception as e:
        print(f"\n[LỖI] {e}")

if __name__ == "__main__":
    auto_newspaper_scraper()
    input("\nNhấn Enter để kết thúc chương trình...")