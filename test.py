from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver 路徑
chrome_path = '/usr/local/bin/chromedriver'

# 設定 Chrome options
options = Options()
options.add_argument('--headless')  # 可視情況拿掉這行觀察頁面
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# 啟動 WebDriver
service = Service(executable_path=chrome_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
    driver.get(url)

    # 使用 WebDriverWait 等待表格載入（實際是 document.write 完成）
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table'))
    )

    # 印出整個渲染後的 HTML
    print(driver.page_source)

finally:
    driver.quit()

