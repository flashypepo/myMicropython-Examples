"""
bitcoin alert, retrieves bitcoin-price and, in future, alert me
My idea is to run this on a ESP32/ESP8266 type device with OLED-display

pre-condition: device connected to internet

Based upon: https://www.hackster.io/rahulkumarsingh/crypto-alert-system-using-bolt-iot-d62df1
2017-1229 PePo new
"""
try:
    import urequests as requests
except:
    import requests
import json
import time

# API: https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR,USD
def price_check():
    url = "https://min-api.cryptocompare.com/data/price"
    querystring = "?fsym=BTC&tsyms=EUR,USD"
    #laptop: querystring = {"fsym":"BTC","tsyms":"EUR"}
    #laptop: response = urequests.request("GET", url, params=querystring)
    response = requests.get(url + querystring)
    response = json.loads(response.text)
    euro_price = response['EUR']
    usd_price = response['USD']
    return euro_price, usd_price

def run(dt=20):
    while True:
        market_europrice, market_usdprice = price_check()
        #print ("Market price is euro", market_europrice, ", usd", market_usdprice)
        print ("Market price is €{0:7.2f} (${1:7.2f})".format(market_europrice,market_usdprice))
        time.sleep(dt)

#get bitcoin-price every 1 minute
waittime = 60 #seconds
run(waittime)
