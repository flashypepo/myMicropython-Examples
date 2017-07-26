# Example of mounting a SD-card filesysteem 
# and reading a file from SD-card
#
# pre-condition: DOS-formatted microSD in SD card drive
#                sdcard.py is on the filesystem
#                WeMOS D1 mini and SD card shield attached.
# WeMOS: SD card communicates through SPI: SPI(1), CS = D8 / GPIO15
# see Jupyter Notebook "WeMOS D1 mini experimenten"
#
# 2017-0601 PePo new, sdcard.py is on filesystem
# TODO: add sdcard.py as frozen module into ESP8266 firmware
#

# ---------------------------
# ---------------------------

# ---------------------------
# imports and init of sdcard
# ---------------------------
import machine, sdcard, os
sd = sdcard.SDCard(machine.SPI(1), machine.Pin(15))

# ---------------------------
# mount SD card
# ---------------------------
os.mount(sd, '/fc')
# listing of files on SC-card!
os.listdir('/fc')

# ---------------------------
# read a file from the SD-card
# ---------------------------
fn = '/fc/main.py'
with open(fn,'r') as f:
    result1 = f.read()
    print(len(result1), 'bytes read')
    print(result1)

# output: 
#  24 bytes read
#  print("main.py: hello")


# ---------------------------
# unmount SD card filesystem
# ---------------------------
os.umount('/fc')

# test: listing of the flash filesystem
os.listdir()
