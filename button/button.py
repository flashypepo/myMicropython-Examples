# demo of reading a button on Huzzah
# 2017-0808 PePo initial setup
# Adafruit article:
# https://learn.adafruit.com/micropython-hardware-digital-i-slash-o/digital-inputs

from micropython import const
import machine, time

# class LED

# see Adafruit article!
# 2018-0313 PePo: button with LED: requires two GPIO-pins
#   BUTTON_PIN, PULL_UP for proper state
#   LED_PIN, Pin.OUT
#   WeMOS Lolin32, led=built-in = 5
#define button:
BUTTON_PIN = const(12)
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
#define led:
LED_PIN = const(13)
led = Led(LED_PIN)
led.off()

# loop
while True:
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        print('Button pressed!')
        ledOn()
    elif not first and second:
        print('Button released!')
        ledOff()
