# get temperature readings from DS18B20 temperature sensor
# Configuration Temperature-node:
# WeMOS D1 Mini - sensor attached to D5 (GPIO14)
#        ,,     - LED attached to D6 (GPIO12)
from micropython import const
import machine, time
import onewire, ds18x20

__SENSOR_PIN = const(14) # WeMOS D1 mini D5

# setup sensor and returns sensor ds, roms and led
def setup():
    # create onewire object on GPIO-pin
    ow = onewire.OneWire(machine.Pin(__SENSOR_PIN))
    print('OneWire bus devices:', ow.scan())
    #output: [bytearray(b'(\xff\xa1/\x83\x16\x03~')]

    #create a sensor-object
    ds = ds18x20.DS18X20(ow)
    #roms = ds.scan()
    # return ds, roms
    return (ds)

def test(ds, dt = 1.0):
    try:
        roms = ds.scan()
        while True:
            ds.convert_temp()
            time.sleep_ms(750)
            for rom in roms:
                print('Temperature {0:0.2f} C'.format(ds.read_temp(rom)))
            time.sleep(dt)
    except:
        print('test() intercepted.')

#@property <- howto use?
def temperature(ds):
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        t = ds.read_temp(rom)
        #OK:print ('Temperature {0:0.2f} C'.format(t))
    #OK:print ('Temperature {0:0.2f} C'.format(t))
    return t
