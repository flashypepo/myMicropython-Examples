# NeoPixel driver for MicroPython on ESP8266
# MIT license; Copyright (c) 2016 Damien P. George

from esp import neopixel_write

class NeoPixelRGBW:
    def __init__(self, pin, n):
        self.pin = pin
        self.n = n
        self.buf = bytearray(n * 4)
        self.pin.init(pin.OUT)

    def __setitem__(self, index, val):
        r, g, b, w = val
        self.buf[index * 4] = g
        self.buf[index * 4 + 1] = r
        self.buf[index * 4 + 2] = b
        self.buf[index * 4 + 3] = w

    def __getitem__(self, index):
        i = index * 4
        return self.buf[i + 1], self.buf[i], self.buf[i + 2], self.buf[i + 3]

    def fill(self, color):
        r, g, b, w = color
        for i in range(len(self.buf) / 4):
            self.buf[i * 4] = g
            self.buf[i * 4 + 1] = r
            self.buf[i * 4 + 2] = b
            self.buf[i * 4 + 3] = w

    def write(self):
        neopixel_write(self.pin, self.buf, True)
