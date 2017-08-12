# ESP32 - versions >25th July 2017: address starts at 0x1000 to allow flash size autodetect.
# 2017-0726 test op de WeMOS Lolin32 was successful!

$esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash

$esptool.py --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect -fm dio 0x1000 esp32-20170725-v1.9.1-381-g96de4d13.bin
