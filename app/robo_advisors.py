# app/robo_advisor.py
import requests
import json 
import datetime
import csv
import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

symbol = input("Please specify a stock symbol (e.g. AMZN) and press enter: ")

while True:
    if (len(str(symbol)))>5: 
       print("Detected invalid input! Please try again...")
       quit()
    elif not symbol.isalpha():
       print("Detected invalid input! Please try again...")
       # https://stackoverflow.com/questions/36432954/python-validation-to-ensure-input-only-contains-characters-a-z
       quit()
    else:
        break
API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
def get_response(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response

def transform_response(parsed_response):
    tsd = parsed_response["Time Series (Daily)"]

    rows = []
    for date, daily_prices in tsd.items(): 
        row = {
            "timestamp": date,
            "open": float(daily_prices["1. open"]),
            "high": float(daily_prices["2. high"]),
            "low": float(daily_prices["3. low"]),
            "close": float(daily_prices["4. close"]),
            "volume": int(daily_prices["5. volume"])
        }
        rows.append(row)

    return rows

def write_to_csv(rows, csv_filepath):
    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() 
        for row in rows:
            writer.writerow(row)

    return True

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

def buy_sell(recent_low, recent_high):
        if float(recent_low) < 0.5*float(recent_high): 
            return("Don't Buy")
            #break
        else:
            return ("Buy")
            #break

def WHY(recent_low, recent_high):
        if float(recent_low) < 0.5*float(recent_high): 
            return("Stock is too volatile")
            #break
        else:
            return ("Stock is stable, may provide steady returns")
            #break
if __name__ == "__main__":

    time_now = datetime.datetime.now()
    parsed_response = get_response(symbol)

    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

    rows = transform_response(parsed_response)

    latest_close = rows[0]["close"]
    high_prices = [row["high"] for row in rows] 
    low_prices = [row["low"] for row in rows] 
    recent_high = max(high_prices)
    recent_low = min(low_prices)


    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

    write_to_csv(rows, csv_filepath)
    Recommendation = buy_sell(recent_low, recent_high)
    Reason = WHY(recent_low, recent_high)
    
    formatted_time_now = time_now.strftime("%Y-%m-%d %H:%M:%S") 
    formatted_csv_filepath = csv_filepath.split("..")[1] 
    print("-------------------------")
    print(f"SYMBOL: {symbol}")
    print("-------------------------")
    print(f"REQUEST AT: {formatted_time_now}")
    print(f"REFRESH DATE: {last_refreshed}")
    print("-------------------------")
    print(f"RECENT HIGH:  {to_usd(recent_high)}")
    print(f"LATEST CLOSE: {to_usd(latest_close)}")
    print(f"RECENT LOW:   {to_usd(recent_low)}")
    print("-------------------------")
    print(f"RECOMMENDATION: {Recommendation}") 
    print(f"BECAUSE: {Reason}")
    print(f"WRITING DATA TO CSV: {formatted_csv_filepath}")
    print("-------------------------")
    print("HAPPY INVESTING!")
