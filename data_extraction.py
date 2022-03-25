from datetime import datetime
import pandas as pd
import requests
def extract_data(tickers):
    # reads from the existing stock_data.csv and prints its contents
    df = pd.read_csv("stock_data.csv")

    # imports the database of ticker symbols to perform analysis on
    df_tickers = pd.read_csv("TICKER_SYMBOLS.csv")


    # Functions to get data from yahoo finance api
    url = "https://yfapi.net/v6/finance/quote"

    headers = {
        'x-api-key': "5xkunZ5a3H6kv1QLIG5EyIi47Up8SqN19Wp9oIc5"
        }

    def dict_metrics(sym):
        querystring = {"symbols": sym}
        try:
            return requests.request("GET", url, headers=headers, params=querystring).json()["quoteResponse"]["result"][0]
        except:
            print("100 API Calls exceeded")

    def printDictFormatted(d):
        for key in d:
            print(str(key) + ": " + str(d[key]))
    def metric(sym, col):
        querystring = {"symbols": sym}
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            stock_info_dict = response.json()["quoteResponse"]["result"][0]
            return stock_info_dict[col]
        except:
            return "100 API Calls exceeded"

            
    # Draws a random sample of 5 tickers from the tickers database to insert data for and prints.
    # df_tickers_sample = df_tickers.sample(5)
    # tickers = df_tickers_sample["ticker"]
    # tickers

    #Appends all data for tickers in the "tickers" list
    for ticker in tickers:
        df = df.append(dict_metrics(ticker), ignore_index=True)

    #Function to reposition an already existing column in the dataframe
    def insert_at(df, pos, column_name):
        df.insert(pos, column_name, df.pop(column_name))



    try:
        insert_at(df, 0, "symbol")
        insert_at(df, 1, "bid")
        insert_at(df, 2, "marketCap")
        insert_at(df, 3, "displayName")
    except:
        print("Column cannot be popped")

    # reads the dataframe of stock data into a csv named "stock_data.csv"
    df.to_csv("stock_data.csv", index = False)

tickers = ["FB", "AAPL", "AMZN", "NFLX", "GOOG", "DIS", "AMD"]

#defines the time of when the code should run
while True:
    now = datetime.now()
    hours = [hr for hr in range(8, 16)]
    if (now.hour in hours and now.minute == 0 and now.second == 0):
        extract_data(tickers)
        if (now.hour == 15):
            break

        
    
        

