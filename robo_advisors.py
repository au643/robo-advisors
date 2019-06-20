# app/robo_advisor.py
import requests
import json 
import datetime
request_url = "http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)
#print (type(response))
#print (response.status_code)
#print(response.text)
#

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

parsed_response = json.loads(response.text)
tsd = parsed_response ["Time Series (Daily)"]
dates = list(tsd.keys())
latest_day = dates [0]

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]
now = datetime.datetime.now()

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + str(now.strftime("%Y-%m-%d %H:%M:%S")))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE:  {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

