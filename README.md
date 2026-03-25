![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-green.svg)
## 📰 Automated News Data Scraper & Parser

This project provides an automated solution for extracting structured data from digital newspapers (specifically optimized for [Người Lao Động Newspaper](https://nld.com.vn/)). It replaces manual data entry by programmatically retrieving **article titles, publication dates, and author names**.

 ## 1. Requirements

To execute this script, the following environment and libraries are required:

* Python Runtime: Version 3.9 or higher. 

* Third-party Libraries:

    * requests: For handling HTTP/1.1 protocols and retrieving HTML source code.

    * beautifulsoup4: For parsing HTML/XML documents using DOM tree navigation.

    * Operating System: Cross-platform (Windows, macOS, Linux).

## Installation Command:
**Bash**
```bash
pip install requests beautifulsoup4
```

## 2. Technical Specifications

The script is engineered with a focus on data integrity and standardized output:

**🔍 Extraction Logic (DOM Selection)**

  The parser targets specific CSS selectors to isolate relevant nodes:  

    * Title: Identifies h1.detail-title.

    * Timestamp: Locates .detail-time.

    * Author: Extracts from .detail-author.

**🛠 Data Sanitization (Regex & String Manipulation)**

* Temporal Normalization: Uses Regular Expressions (Regex) to filter and extract the date in DD/MM/YYYY format, discarding time-specific metadata.

    * Regex Pattern: \d{2}/\d{2}/\d{4}

* Author Parsing: Implements string splitting and prefix removal (e.g., stripping "By:", "News & Photo:") to isolate the core pseudonym.

**📊 Data Persistence & Encoding**

* Format: Exported to .csv (Comma-Separated Values).

* Encoding: Utilizes utf-8-sig (Byte Order Mark) to ensure full compatibility with Microsoft Excel in Vietnamese locales, preventing character corruption.

* Write Mode: Implements an "Append" (a) logic with header-check to allow multi-run data accumulation in a single file.

## 3. Usage Instructions

Follow these steps to operate the automation tool:

**Step 1: Clone and Initialize**

Ensure the script (main.py) is located in your project directory. Open your terminal or Command Prompt.

**Step 2: Execution**

Run the script using the Python interpreter:
```bash
python main.py
```
**Step 3: Input**

The terminal will prompt for a URL. Copy and paste the target newspaper link:

![](Pictures\url_input.png)

```Plaintext
Enter Newspaper URL: https://nld.com.vn/example-article.htm
  ```
  
**Step 4: Verification**

Upon successful execution, the script will output the absolute path of the generated file:



Output File: data_chuan_hoa.csv

Status: A console message will confirm "Extraction Successful" along with a preview of the processed data.

![](Pictures\extracted.png)

.csv file after extracted

![](Pictures\csv_file.png)


Author: **Huynh Khoi**

Role: Mechatronics Engineer