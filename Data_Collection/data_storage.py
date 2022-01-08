
# Imports the script to scrape stock data from Yahoo Finance
import scraper
# Imports pandas to work the spreadsheet on backend
import pandas as pd
from datetime import date
# DataFrame that will contain stock data to be passed into the spreadsheet
df = pd.DataFrame()
try:
    df = pd.read_csv("Stock_Data.csv")
except:
    pass

stocks_to_track = ["AAPL", "MSFT", "GOOG", "FB", "AMZN", "NFLX", "TSLA", "DIS"]

def fetch_data(list_stocks):
    to_insert = []
    for stock in list_stocks:
        d = {"Date": str(date.today().strftime("%m/%d/%y")), "Symbol": stock, "Price": scraper.getCurrentStockPrice(stock)}
        to_insert.append(d) 

    return pd.DataFrame(to_insert)

df = df.append(fetch_data(stocks_to_track), ignore_index=True)
try:
    del df["Unnamed: 0"]
except:
    pass
df.to_csv("Stock_Data.csv", index=True)

print("Running")



