# TEST: print readings from DS18B20 temperarure sensor
# WeMOS D1 Mini - sensor attached to D5 (GPIO14)
# Note: sensor makes use of OneWire protocol
# 2017_0818 PePo test with T-node and LED on GPIO12 (D6)
from micropython import const
import machine, time
import onewire, ds18x20

__SENSOR_PIN = const(14) # WeMOS D1 mini D5
__LED_PIN = const(12) # WeMOS D1 mini D6

def setup():
    # create onewire object on GPIO-pin
    ow = onewire.OneWire(machine.Pin(__SENSOR_PIN))
    print('OneWire bus devices:', ow.scan())
    #output: [bytearray(b'(\xff\xa1/\x83\x16\x03~')]

    # led: on = T-measurement, off=else
    led = machine.Pin(__LED_PIN, machine.Pin.OUT)
    led.off()

    #create a sensor-object
    ds = ds18x20.DS18X20(ow)
    roms = ds.scan()
    return (ds, roms, led)
# setup
ds, roms, led = setup()
def run(dt = 1.0):
    try:
        while True:
            led.on()
            ds.convert_temp()
            time.sleep_ms(750)
            for rom in roms:
                print('Temperature {0:0.2f} C'.format(ds.read_temp(rom)))
                led.off()
                time.sleep(dt)
    except:
        print('run() interrupted.')
