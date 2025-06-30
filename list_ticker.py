from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import time
import re

# 設定 headless Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
driver.get(url)

# 等待 JS 產生資料
time.sleep(5)

html = driver.page_source
driver.quit()

# 解析 HTML，找有「有價證券代號」字樣的 table
soup = BeautifulSoup(html, "html.parser")
full_text = soup.get_text()
tables = soup.find_all("table")
print(f"共抓到 {len(tables)} 張 table")

# 搜尋日期
match = re.search(r"最近更新日期[:：]\s*(\d{4}/\d{2}/\d{2})", full_text)
if match:
    date_str = match.group(1)
    print("✅ 找到最近更新日期：", date_str)
else:
    print("❌ 沒找到最近更新日期")


target_table = None
for t in tables:
    if "有價證券代號" in t.get_text():
        target_table = t
        break

if not target_table:
    raise Exception("找不到股票清單表格")

# 用 pandas 讀表格，避免 FutureWarning 用 StringIO 包裝
df = pd.read_html(StringIO(str(target_table)), encoding="big5")[0]

# 過濾出股票代碼為四碼數字的列
df = df[df[df.columns[0]].astype(str).str.match(r"^\d{4}")].copy()

# 拆出「股票代號」和「股票名稱」
df[['股票代號', '股票名稱']] = df[df.columns[0]].str.extract(r"^(\d{4})\s+(.+)$")

# 重新命名前面數字欄位
df = df.rename(columns={
    0: "合併欄位",
    1: "ISIN",
    2: "上市日",
    3: "市場別",
    4: "產業別",
    5: "CFICode",
    6: "備註"
})
print("欄位名稱：", df.columns)

# 取需要的欄位
df = df[["股票代號", "股票名稱", "ISIN", "產業別", "上市日", "市場別"]]

# 新增 yfinance 格式 ticker
df['ticker'] = df['股票代號'] + '.TW'

print(df.head())

# 全部列出
print(f"\n共 {len(df.dropna(subset=['股票代號', '股票名稱', 'ticker']))} 檔上市股票\n")
for index, row in df.dropna(subset=['股票代號', '股票名稱', 'ticker']).iterrows():
    print(f"{row['股票代號']:>4}  {row['股票名稱']:<10}  {row['ticker']}")
