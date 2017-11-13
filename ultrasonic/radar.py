# radar: sweep servo and measure distance
# 2017-1112 PePo new - cmbination of servo and ultrasonic sensor HC-SR04

from micropython import const
import machine
import time

import servo
import ultrasonic
#import ssd1306
import myssd1306 as ssd1306  #includes draw_bitmap

# HSR04 GPIO pins
trigger = 12 #gpio[ "D6" ]
echo = 14 #gpio[ "D5" ]
# setup sensor hc on pins trigger and echo
hc = ultrasonic.Ultrasonic( trigger, echo)
# storage for distance value
dist = 0

# WeMOS-LoLin32-OLED i2c pins
_SCL = const(4)
_SDA = const(5)
# create i2c and OLED-i2c objects
i2c = machine.I2C(scl=machine.Pin(_SCL), sda=machine.Pin(_SDA))
#i2c = I2C(scl=Pin(SCL), sda=Pin(SDA), freq=100000)
i2c.scan()   #[60]

# WeMOS-LoLin32-OLED 128*64
_DISPLAY_WIDTH  = const(128)  # Width of display in pixels.
_DISPLAY_HEIGHT = const(64)   # LoLin-ESP32-OLED height of display.
oled = ssd1306.SSD1306_I2C(_DISPLAY_WIDTH, _DISPLAY_HEIGHT, i2c)

# OLED helper: blank oled screen
def eraseOled():
    oled.fill(0)
    oled.show()

# OLED helper: specify display_pixel function including oled.show()
def display_text(message, col=0, row=25, toErase=True):
    if toErase:
        oled.fill(0)
    oled.text('Radar demo', 0, 10) # header
    oled.text(message, col, row)
    oled.show()

# setup servo and initialise it at angle 0
SV_PIN = const(15) # pin servo
sv = servo.Servo(machine.Pin(15, machine.Pin.OUT))
#sv.write_angle(0)

# servo sweeps between MIN and MAX angle (degrees)
MIN_ANGLE = const(60)
MAX_ANGLE = const(120)
angle = MIN_ANGLE # current angle of servo
delta_angle = 2 # increment of servo - integer, please
# SERVO helper function: gotoAngle in small increments
def gotoAngle(sv, angle, inc = delta_angle):
    for i in range(angle, inc):
        sv.write_angle(i)
        time.sleep(0.1)

# delay between distance measurents
sleep_delay = 0.4

# main program:
# 1. position servo (between 0 .. 180 degrees)
# 2. measure distance
# 2. show on OLED
# 3. dump on serial to other systems
def run(delay=sleep_delay):
    global sv, angle, dist, delta_angle
    try:
        display_text('Radar demo', 0, 10) # header
        while True:
            # position servo
            #TODO: gotoAngle(serv, angle)
            sv.write_angle(angle)

            # Get reading from sensor
            #PePo TODO: dist = hc.distance_in_cm()
            dist = hc.distance()

            #display on OLED)
            display_text('afstand: {0:3.1f} cm'.format(dist*100))
            #send to serial port - only the value in cm
            print('{0:3.1f}'.format(dist*100))

            time.sleep(delay)

            # calculate new servo angle
            angle += delta_angle
            if angle > MAX_ANGLE:
                angle = MAX_ANGLE
                delta_angle = -5 #reverse increment
            if angle < MIN_ANGLE:
                angle = MIN_ANGLE
                delta_angle = 5

    except Exception as e:
        eraseOled()
        sv.deinit() #de-initialise servo pin!
        print ('Done!')
        print (e)

# execute
#run(delay = 0.8)
