''' demo of reading a button, interrupt-based!
Two modes:
1. callback including updates on LED and OLED - not good practices
2. callback, properly defined. Requires program checks status (while True).
2017-0808 PePo initial setup
'''
import micropython
import machine, time
import ssd1306

__LED_PIN = const(14) #GPIO14
__BUTTON_PIN = const(12) #GPIO12

#define led to be set on / off by button
led = machine.Pin(__LED_PIN, machine.Pin.OUT)
led.off()
# status of led: True=on, False=off
led_status = False

# create i2c for OLED display
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
print('i2c.scan: ', i2c.scan())   #[60]
# OLED screen dimensions
__WIDTH = const(128)
__HEIGHT = const(32)
oled = ssd1306.SSD1306_I2C(__WIDTH, __HEIGHT, i2c)

''' define callback with LED and OLED updates
# direct control of LED and OLED is not best practices. Why?
# => too slow and it hold up other processing
def callback_oled(p):
    print('button {0} pressed'.format(p))
    led.value(not led.value())
    refreshOLED('LED: {0} '.format(led.value())) #LED value
#'''

#''' define a proper callback
def callback(p):
    global led_status
    # best practices: set variabel and pick it up in other part of program
    led_status = not led_status
#'''

# helper to refresh OLED display
def refreshOLED(msg):
    oled.fill(0) # clear oled
    oled.text('Button demo',0,0) #header
    oled.text(msg,0,10)
    oled.show()

# define button on Pin GPIO12
button = machine.Pin(__BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

#define buton-click interrupt on falling edge due to PULL_UP!
''' using a 'slow' callback
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback_oled)
refreshOLED('Press button!')
oled.show()
print('done')
#'''

#''' using proper callback
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)
print('done')
# required to have a loop to display current status of led...
def run():
    while True:
        if led_status:
            led.on()
        else:
            led.off()
        refreshOLED('LED: {0} '.format(led_status))

# the demo
try:
    print('Button demo')
    refreshOLED('Press button!')
    run()
except:
    print('Done')
    refreshOLED('Done!')
#'''
