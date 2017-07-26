# 2017_0708 PePo general demo: bargraph and oled
# pre-conditio: import oled and import bar ifrom various folders
import machine
import bar
import oled

def demo():
    machine.freq(160000000)
    print('demonstration led-bar... Ctrl-C to stop')
    bar.demo_bar(0.1)
    print('demonstration OLED... Ctrl-C to stop')
    oled.demo(oled.i2c, 'Micropython rock-and-roll!!')
    machine.freq(80000000)

try:
    while True:
        demo()
except KeyboardInterrupt:
    print ('demos done')
