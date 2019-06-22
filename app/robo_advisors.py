# app/robo_advisor.py
import requests
import json 
import datetime
import csv
import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment


api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
symbol = "MSFT"

request_url = f"http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)
#print (type(response))
#print (response.status_code)
#print(response.text)
#
#valid_ids = [str(p["id"]) for p in products] # doing comparisons with string versions of these ids
#total_price = 0 
#selected_ids = []
#
#while True:
#    selected_id = input("Please input a product identifier, or 'DONE': " ) # the data input will always be a str
#
#   if selected_id == "DONE":
#       break # stops the loop
#   elif str(selected_id) in valid_ids:
#       selected_ids.append(selected_id)
#   else:
#       print("Detected invalid input! Please try again...")
     
#print ("SELECTED PRODUCTS:" )




def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

parsed_response = json.loads(response.text)
tsd = parsed_response ["Time Series (Daily)"]
dates = list(tsd.keys())
latest_day = dates [0]

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]
now = datetime.datetime.now()

high_prices = []
low_prices = []
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))
recent_high = max(high_prices)
recent_low = min(low_prices)

csv_file_path = os.path.join(os.path.dirname(__file__),"..","data","prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high":daily_prices["2. high"],
            "low":daily_prices["3. low"],
            "close":daily_prices["4. close"],
            "volume":daily_prices["5. volume"],
            })


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE:  {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")

print("HAPPY INVESTING!")
print("-------------------------")

