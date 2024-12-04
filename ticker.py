from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()

def get_price(ticker):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={os.environ.get('ALPHAVANTAGE_API_KEY')}"
    response = requests.get(request_url)
    ticker_response = response.json()
    last_refreshed = ticker_response["Meta Data"]["3. Last Refreshed"]
    latest_close = ticker_response["Time Series (Daily)"][last_refreshed]["4. close"]
    return latest_close

if __name__ == "__main__":
    print("Get a ticker value")
    ticker = input("Please enter a stock ticker: ")

    result = get_price(ticker)

    print("\n")
    pprint(result)


