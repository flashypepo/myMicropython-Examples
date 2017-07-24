# two_neopixels - runs animations from config-file on two neopixels
# 2017-0121 PePo new, combinedmatrix and stick Python code
# ------------------
import machine
import neopixel
import utime
import ujson

# standard configuration that never changes
# NodeMCU: 
# matrix 8*8 pixels: attached to pin D7 (GPIO13)
# stick 1*8 pixels: attached to pin D8 (GPIO15)
PIXEL_PIN1 = machine.Pin(13, machine.Pin.OUT)
PIXEL_PIN2 = machine.Pin(15, machine.Pin.OUT)
# number of neopixels
PIXEL_COUNT1 = 64  # 8x8 pixels
PIXEL_COUNT2 = 8  # stick 1*8

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

# Linear interpolation helper:
def _lerp(x, x0, x1, y0, y1):
    return y0 + (x - x0) * ((y1 - y0)/(x1 - x0))

# Animation functions
# blank the neopixels
def blank(config, np, pixel_count):
    np.fill((0,0,0))
    np.write()

# solid animation
def solid(config, np, pixel_count):
    colors = config['colors']
    elapsed = utime.ticks_ms() // config['period_ms']
    current = elapsed % len(colors)
    np.fill(colors[current])
    np.write()

# chasing animation
def chase(config, np, pixel_count):
    colors = config['colors']
    elapsed = utime.ticks_ms() // config['period_ms']
    for i in range(pixel_count):
        current = (elapsed+i) % len(colors)
        np[i] = colors[current]
    np.write()

# smooth animation
def smooth(config, np, pixel_count):
    # Smooth pulse of all pixels at the same color.  Interpolates inbetween colors
    # for smoother animation.
    colors = config['colors']
    period_ms = config['period_ms']
    ticks = utime.ticks_ms()
    step = ticks // period_ms
    offset = ticks % period_ms
    color0 = colors[step % len(colors)]
    color1 = colors[(step+1) % len(colors)]
    color = (int(_lerp(offset, 0, period_ms, color0[0], color1[0])),
             int(_lerp(offset, 0, period_ms, color0[1], color1[1])),
             int(_lerp(offset, 0, period_ms, color0[2], color1[2])))
    np.fill(color)
    np.write()

# extra helper function to blank pixels of a specific neopixel
# 2017_0121 PePo -added np als argument
def off(np):
    np.fill((0,0,0))
    np.write()

# Setup code #
# Load configuration from config JSON file.
# using Python context manager
# 2017_0121 parameters are to be used for both neopixels!
with open('config.json', 'r') as infile:
    config = ujson.load(infile)

# config: mirror_colors
if (config['mirror_colors']):
    config['colors'] = mirror(config['colors'])

# initialize the neopixels and turn them off
np1 = neopixel.NeoPixel(PIXEL_PIN1, PIXEL_COUNT1)
np2 = neopixel.NeoPixel(PIXEL_PIN2, PIXEL_COUNT2)
off(np1)
off(np2)

# determine the animation function to call
animation = globals().get(config['animation'], blank)

# Main loop
while True:
    animation(config, np1, PIXEL_COUNT1) #matrix
    animation(config, np2, PIXEL_COUNT2) #stick
    utime.sleep(0.01)
