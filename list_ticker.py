import requests
import pandas as pd

# 抓取台灣證交所上市公司代號與名稱（上市）
def fetch_twse_listed_companies():
    url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    df = pd.read_html(res.text)[0]

    # 整理欄位
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.rename(columns={"有價證券代號及名稱": "代號名稱"})
    df["證券代號"] = df["代號名稱"].str.extract(r"(\d{4})")
    df["名稱"] = df["代號名稱"].str.extract(r"\d{4}　(.+)")
    df["yfinance_ticker"] = df["證券代號"] + ".TW"
    df = df[["證券代號", "名稱", "yfinance_ticker"]].dropna()
    return df

df = fetch_twse_listed_companies()

# 印出前幾筆
print(df.head())

# 若要存成 CSV
df.to_csv("twse_yfinance_tickers.csv", index=False, encoding='utf-8-sig')
