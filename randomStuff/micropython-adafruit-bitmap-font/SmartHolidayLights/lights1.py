# lights.py - part 1 from Tony Dicola - Adafruit
# 2016-1204 PePo new/copied from https://gist.github.com/tdicola/55c7ba333933bccaa75526a07b266bf2

# ------------------
import machine
import neopixel
import utime

# configuration NodeMCU
PIXEL_PIN = machine.Pin(13, machine.Pin.OUT) # pin D7
PIXEL_COUNT = 64  # number of neopixels
PERIOD_MS = 100   # amount of time (in milliseconds) 
                  # to spend at each animation step.
                  # Increase to slow down the animation or
                  # decrease to speed up animation
FRAME = 0

# global state
# ramp of colors from blue up to red (with pink in-between).
colors = [(0,0,255), (16,0,128), (32,0,64), (64,0,32), (128,0,16), (255,0,0)]
# ramp of alternate colors...
#colors = [(0,255,0), (16,128,0), (32,64,0), (64,32,0), (128,16,0), (255,0,0)]
# ramp of colors Blue, Green and Red
#colors = [(0,0,255), (0,255,0), (255,0,0)]

# mirror the colors to make a ramp up and ramp down with no repeated colors.
def mirror(values):
    # Add the input values in reverse order to the end of the array
    # However slice off the very first and very last item (the [1:1] syntax)
    # to prevent the first and last values from repeating.
    # for example an input of:
    # [1, 2, 3]
    # returns:
    # [1, 2, 3, 2]
    # instead of returning:
    # [1, 2, 3, 3, 2, 1]
    # which would duplicate 3 and 1 as you loop through the elements
    values.extend(list(reversed(values))[1:-1])
    return values
colors = mirror(colors)

# Animation functions
def solid():
    elapsed = utime.ticks_ms() // PERIOD_MS
    current = elapsed % len(colors)
    np.fill(colors[current])
    np.write()

def chase():
    elapsed = utime.ticks_ms() // PERIOD_MS
    for i in range(PIXEL_COUNT):
        current = (elapsed+i) % len(colors)
        np[i] = colors[current]
    np.write()

def alternate():
    flip_flop = FRAME % 2
    for i in range(PIXEL_COUNT):
        if flip_flop == 0:
            np[i] = (128,0,0)
            flip_flop = 1
        else:
            np[i] = (0,128,0)
            flip_flop = 0
    np.write()

# Animate lights function runs a main loop given the animation function to call.
# In the web REPL try calling:
#   import lights
#   lights.animate_lights(lights.chase)
# To run the chase animation (press Ctrl-C to interrupt and stop animation).
def animate_lights(animation):
    while True:
        animation()
        utime.sleep(0.01)

# 2016_1204 PePo added off() to blank neopixels
def off():
    np.fill((0,0,0))
    np.write()

# Setup code
np = neopixel.NeoPixel(PIXEL_PIN, PIXEL_COUNT)
off()

# testing animation
#animate_lights(solid)
#animate_lights(chase)
#animate_lights(alternate)