"""
bitcoin alert, retrieves bitcoin-price and, in future, alert me
My idea is to run this on a ESP32/ESP8266 type device with OLED-display

pre-condition: device connected to internet

Based upon: https://www.hackster.io/rahulkumarsingh/crypto-alert-system-using-bolt-iot-d62df1
2018_0114 PePo adopted to D1 mini OLED-shield, running on ESP32 minikit
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
#oled = ssd1306.SSD1306_I2C (128, 32, i2c)
oled = ssd1306.SSD1306_I2C (64, 48, i2c)
# helper -> classOLED.method(3 arg: row1, row2, row3)
def displayOnOLED(europrice, usdprice):
    oled.fill(0)
    oled.text("Bitcoin price", 0, 0)
    #oled.text("EUR {0:7.2f}".format(europrice), 0, 10)
    #oled.text("USD {0:7.2f}".format(usdprice), 0, 20)
    oled.text("E{0:7.1f}".format(europrice), 0, 10)
    oled.text("${0:7.1f}".format(usdprice), 0, 20)
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

''' 2018_0115 deprecated
def idle(dt, row=28):
    now = time.ticks_ms()
    # Calculate deadline for operation and test for it
    delta = dt*1000
    stepx = delta // oled.width
    deadline = time.ticks_add(now, delta)
    dcol = stepx // oled.width
    #print("now:", now)
    #print("deadline:", deadline)
    #print("stepx:", stepx)
    #col = 0
    isToggle = True
    leftover = time.ticks_diff(deadline, time.ticks_ms())
    while leftover > 0:
        oled.text(b' ', 0, row)
        if isToggle:
            oled.text('-', 0, row)
            isToggle = False
        else:
            oled.text('|', 0, row)
            isToggle = True
        oled.show()
        time.sleep(0.5)
#'''
 
def run(dt=20):
    while True:
        market_europrice, market_usdprice = price_check()
        #print ("Market price is euro", market_europrice, ", usd", market_usdprice)
        print ("Market price is €{0:7.2f} (${1:7.2f})".format(market_europrice,market_usdprice))
        
        # repeat refresh OLED wit wait-symbol (| <-> -), which needs fill(0)
        now = time.ticks_ms()
        # Calculate deadline for operation and test for it
        delta = dt*1000
        deadline = time.ticks_add(now, delta)
        isToggle = True
        row = 30
        leftover = time.ticks_diff(deadline, time.ticks_ms())
        while leftover > 0:
            oled.fill(0)# blank
            displayOnOLED(market_europrice, market_usdprice)
            if isToggle:
                oled.text('-', 0, row)
                isToggle = False
            else:
                oled.text('|', 0, row)
                isToggle = True
            oled.show()
            time.sleep(0.5)
            leftover = time.ticks_diff(deadline, time.ticks_ms())
            #idle(dt); #time.sleep(dt)

#get bitcoin-price every 1 minute
waittime = 15 #seconds
run(waittime)
