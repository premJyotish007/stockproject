import requests


def printDictFormatted(d):
    for key in d:
        print(str(key) + ": " + str(d[key]))
def getCurrentStockPrice(sym):
    url = "https://yfapi.net/v6/finance/quote"

    querystring = {"symbols": sym}

    headers = {
        'x-api-key': "5xkunZ5a3H6kv1QLIG5EyIi47Up8SqN19Wp9oIc5"
        }

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        stock_info_dict = response.json()["quoteResponse"]["result"][0]
        return stock_info_dict["bid"]
    except:
        return "100 API Calls exceeded"