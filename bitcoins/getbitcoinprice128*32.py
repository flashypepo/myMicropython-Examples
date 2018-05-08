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

# OLED support, TODO lateron: classOLED
import machine
import ssd1306
# i2c + oled
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000)
oled = ssd1306.SSD1306_I2C (128, 32, i2c)
# helper -> classOLED.method(3 arg: row1, row2, row3)
def displayOnOLED(europrice, usdprice):
    oled.fill(0)
    oled.text("Bitcoin price", 0, 0)
    oled.text("EUR {0:7.2f}".format(europrice), 0, 10)
    oled.text("USD {0:7.2f}".format(usdprice), 0, 20)
    oled.show()

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

def idle(dt, row=26):
    now = time.ticks_ms()
    # Calculate deadline for operation and test for it
    delta = dt*1000
    stepx = delta // oled.width
    deadline = time.ticks_add(now, delta)
    dcol = stepx // oled.width
    #print("now:", now)
    #print("deadline:", deadline)
    #print("stepx:", stepx)
    col = 0
    i = 0
    leftover = time.ticks_diff(deadline, time.ticks_ms())
    while leftover > 0:
        oled.text('. ', col, row)
        oled.show()
        # check if col needs to be incremented...
        i = i + 1
        #print("i:", i)
        #print("leftover", leftover)
        # increment col in leftover/127 steps
        if leftover % 127:
            col = col + 1
            #print("col:", col)
        time.sleep(0.01)
        leftover = time.ticks_diff(deadline, time.ticks_ms())

def run(dt=20):
    while True:
        market_europrice, market_usdprice = price_check()
        #print ("Market price is euro", market_europrice, ", usd", market_usdprice)
        print ("Market price is €{0:7.2f} (${1:7.2f})".format(market_europrice,market_usdprice))
        displayOnOLED(market_europrice, market_usdprice)
        idle(dt); #time.sleep(dt)

#get bitcoin-price every 1 minute
waittime = 15 #seconds
run(waittime)
