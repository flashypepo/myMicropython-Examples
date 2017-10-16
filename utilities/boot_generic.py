''' This file is executed on every boot (including wake-boot from deepsleep)
2017-0904 PePo updated: no debug, disable webrepl, removed home-wifi connection
source: https://youtu.be/yGKZOwzGePY - Tony D! MP ESP8266 HTTP examples
 '''
import esp
esp.osdebug(None)
'''
import webrepl
webrepl.start()
#'''
