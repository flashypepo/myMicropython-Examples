"""
generic class LED
requires GPIO to which led is attached
2018-0313 PePo new
"""
import machine

class Led:
    def __init__(self, pin):
        """
        defines a Led-object attached to pin
        """
        self._led = machine.Pin(pin, machine.Pin.OUT)

    def on(self):
        self._led.value(1)

    def off(self):
        self._led.value(0)

    def toggle(self):
        self._led.value(not self._led.value())

    @property
    def value(self):
        return self._led.value()

