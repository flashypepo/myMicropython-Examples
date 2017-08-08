''' demo of reading a button
 2017-0808 PePo - added OLED display to demo
 Adafruit article:
 https://learn.adafruit.com/micropython-hardware-digital-i-slash-o/digital-inputs
'''
import machine, time
import ssd1306

__LED_PIN = const(14) #GPIO14
__BUTTON_PIN = const(12) #GPIO12

#define led to be set on / off by button
led = machine.Pin(__LED_PIN, machine.Pin.OUT)
led.off()
# OPTIONAL: status of led: True=on, False=off
# led_status = False

# create i2c for OLED display
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
print('i2c.scan: ', i2c.scan())   #[60]
# OLED screen dimensions
__WIDTH = const(128)
__HEIGHT = const(32)
oled = ssd1306.SSD1306_I2C(__WIDTH, __HEIGHT, i2c)

# define button on Pin GPIO12
button = machine.Pin(__BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

# helper to refresh OLED display
def refreshOLED(msg):
    oled.fill(0) # clear oled
    oled.text('Button demo',0,0) #header
    oled.text(msg,0,10)
    oled.show()

# demo ...
def run():
    while True:
        first = button.value()
        time.sleep(0.01)
        second = button.value()
        if first and not second:
            print('Button pressed!')
            led.on()
            refreshOLED('LED: {0} '.format(led.value()))
        elif not first and second:
            print('Button released!')
            led.off()
            refreshOLED('LED: {0} '.format(led.value()))

# run demo
try:
    print('Button demo, press button...')
    refreshOLED('Press button!')
    run()
except:
    print('Done')
    refreshOLED('Done!')
