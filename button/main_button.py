# main.py for testing OLED-displays and sensors# 2017-0808 PePo added button (GPIO12)# 2017-0805 PePo added LDR35 (ADC)# 2017-0728 PePo new TMP36 (ADC)
''' import oledssd1306 as test
print('re-set device, run test.demo()')#'''''' tmp36 experiment#import temperature.tmp36 #zonder OLED
import temperature.tmp36_oled
#'''
''' LDR35 experiment
import light.ldr_oled
#'''
#''' Button / interrupt experiment
#import button.demo
import button.demo_oled
#import button.demo_oled_interrupt
#'''
