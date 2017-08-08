# temperature reading from DHT22
# Huzzah: pin 0
# DHT22 Vcc = 3.3V, =5V no difference
# 2017-0808 PePo initial setup

import machine, time
import dht

__DHT_PIN = const(0) # NodeMCU: pin 0
d = dht.DHT22(machine.Pin(__DHT_PIN))

#define demo
def run(dt=2.0):
    while True:
        d.measure()
        print('Temperature:{0:0.1f} C\tHumidity {1:0.1f} %'.format(d.temperature(), d.humidity()))
        time.sleep(dt)

#run demo
try:
    print('DHT22 demo')
    run()
except:
    print('interrupted - done')
