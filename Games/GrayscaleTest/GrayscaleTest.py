# Grayscale library demo
#
# Shows four different screens, then reboots. Cycle through the screens by
# pressing A (rightmost button), go to calibration screen by pressing B (lefmost
# button). When on calibration screen, up and down change the grayscale timing
# in large increments, left and right in small increments, A or B confirms.

# Fix import path so it finds the grayscale library
import sys
sys.path.insert(0, "/".join(__file__.split("/")[0:-1]))

# Do imports
import thumby
from framebuf import FrameBuffer, MONO_VLSB
from time import ticks_ms, sleep_us, sleep_ms
import grayscale

# Initialization

thumby.audio.stop()
thumby.display.setFPS(0)
#thumby.display.brightness(28)
gs = grayscale.Grayscale()

# Helper functions

def waitKey():
    while thumby.buttonA.pressed() or thumby.buttonB.pressed():
        pass
    while True:
        if thumby.buttonA.pressed():
            return
        if thumby.buttonB.pressed():
            return

# Drawing primitives demo

gs.fill(gs.BLACK)
gs.drawFilledRectangle(16, 9, 40, 21, gs.WHITE)
gs.drawText("Hello", 18, 11, gs.LIGHTGRAY)
gs.drawText("world!", 18, 19, gs.DARKGRAY)
gs.update()
waitKey()

# Bouncing cat demo

while thumby.buttonA.pressed() or thumby.buttonB.pressed():
    pass

cat = grayscale.Sprite(
    12, 9,         # Dimensions
    bytearray([    # Layer 2 data
        255,255,87,7,3,3,3,67,3,7,7,255,
        1,1,1,0,0,0,0,0,0,0,1,1
    ]),
    bytearray([    # Layer 1 data
        175,7,169,254,237,255,191,157,190,233,255,175,
        1,1,0,1,1,1,1,1,1,1,1,1
    ]),
    30, 15         # Position
)

dx = dy = 1
while True:
    gs.fill(gs.WHITE)
    gs.drawSprite(cat)
    cat.x += dx
    cat.y += dy
    if cat.x == 0 or cat.x == 60:
        dx = -1 * dx
    if cat.y == 0 or cat.y == 31:
        dy = -1 * dy
    gs.update()
    sleep_ms(50)

    if thumby.buttonA.pressed():
        break
    if thumby.buttonB.pressed():
        break

# Full screen images demo

girlSprite = grayscale.Sprite(72, 40, bytearray([
    128,4,160,8,130,32,8,162,0,40,130,8,160,10,64,39,53,187,234,149,106,181,214,253,135,1,81,44,210,40,74,180,192,40,129,1,135,207,191,254,232,218,144,96,1,131,7,13,30,59,237,246,217,38,219,171,94,173,106,225,148,64,8,130,32,8,162,0,40,2,144,4,
    0,84,0,18,64,136,2,168,2,80,10,64,10,160,5,168,1,85,135,30,189,122,127,103,37,134,17,0,133,64,3,1,11,141,6,181,20,31,15,87,79,215,255,255,216,32,193,160,112,208,248,243,239,159,124,235,212,187,69,186,215,94,248,200,130,32,10,160,5,80,4,0,
    0,149,32,133,80,8,66,40,2,169,4,81,8,162,8,146,36,129,40,130,104,213,74,136,224,224,192,68,198,201,134,192,137,64,2,224,16,232,182,125,255,255,255,255,107,206,63,191,222,127,71,241,215,127,244,0,3,15,61,126,233,246,219,255,16,74,0,74,32,5,168,1,
    2,80,10,160,10,81,4,145,34,136,33,74,208,138,32,198,122,212,173,116,170,5,20,143,16,167,1,177,87,62,99,114,48,125,180,189,254,223,255,255,127,63,187,254,255,232,167,253,87,217,255,255,255,200,190,232,0,162,0,81,4,147,35,136,37,144,69,16,37,128,42,64,
    160,21,64,20,66,17,136,34,200,146,196,145,195,215,168,127,138,117,10,37,138,20,128,197,195,32,88,151,33,212,201,226,200,245,234,226,255,254,167,73,0,5,2,195,11,243,2,225,95,223,191,255,127,255,250,255,122,136,66,41,4,80,10,32,138,32,74,17,68,18,64,21
]), bytearray([
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,68,21,106,149,74,41,2,120,254,254,255,255,255,255,127,127,127,126,126,120,48,64,0,0,0,0,0,0,0,0,2,1,4,18,9,38,217,36,84,160,80,128,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,0,128,218,248,230,255,127,191,252,254,244,250,249,194,227,224,240,168,176,40,0,0,0,0,0,0,0,0,0,0,0,0,3,20,43,68,186,69,40,160,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,224,240,119,31,31,63,59,57,54,121,63,127,191,255,31,239,23,73,130,0,0,0,0,0,0,0,64,0,0,0,0,40,128,0,0,0,0,2,1,22,9,36,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,240,248,248,252,254,254,255,255,255,235,0,224,248,254,78,0,1,28,13,15,2,11,2,1,0,0,0,128,192,64,0,0,0,88,2,0,0,0,0,0,55,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,128,128,128,252,255,255,255,255,255,255,255,127,255,127,62,63,31,7,0,0,0,128,192,224,224,240,240,240,240,248,246,255,250,253,60,252,28,253,30,160,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
]))

parrotSprite = grayscale.Sprite(72, 40, bytearray([
    160,64,0,0,0,0,0,0,0,0,0,48,208,228,218,98,209,161,194,1,2,5,138,3,203,133,133,43,141,23,13,47,95,86,174,95,94,183,95,39,79,55,31,118,30,78,54,172,244,212,246,249,185,231,72,160,0,164,210,0,128,232,64,96,102,97,116,242,224,244,245,106,
    0,0,0,20,40,4,40,4,18,72,16,189,168,62,236,89,131,223,126,8,70,249,148,237,242,181,249,189,218,55,136,165,20,161,68,34,235,32,69,0,72,4,4,24,4,74,4,148,0,2,1,32,4,0,133,106,179,247,94,232,149,73,107,19,245,86,236,233,100,157,139,140,
    0,64,64,64,0,128,0,0,88,40,192,1,105,50,32,24,31,254,223,222,188,75,187,23,247,9,231,193,15,129,6,0,130,0,64,144,64,136,160,72,176,64,160,64,160,248,232,112,32,8,0,8,0,0,0,1,23,14,60,48,32,10,40,145,1,3,5,18,3,14,63,91,
    16,48,52,36,100,227,64,64,128,193,35,1,42,33,112,108,96,222,248,242,204,187,73,255,251,223,227,252,91,247,94,121,252,252,191,254,189,252,223,126,249,253,250,252,255,253,122,244,57,222,42,156,170,78,24,165,74,16,68,16,192,16,161,71,24,250,232,128,104,128,4,184,
    201,130,199,100,67,239,1,150,241,112,114,124,249,182,8,85,251,239,191,253,251,223,253,239,191,250,231,155,79,192,211,253,239,125,255,127,221,127,175,127,255,95,255,111,255,124,247,188,235,188,234,77,176,74,181,66,121,68,169,66,244,191,74,150,45,127,191,255,236,128,253,123
]), bytearray([
    64,0,0,0,0,0,0,0,0,0,0,0,40,24,36,156,46,94,63,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,254,252,244,240,240,224,192,128,0,0,0,0,0,160,128,128,128,128,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,64,254,255,255,254,124,0,1,127,255,255,255,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,191,255,111,255,255,255,255,255,255,255,255,255,248,248,240,224,224,128,192,130,129,3,6,147,98,112,112,
    128,128,128,128,128,0,0,0,0,0,0,128,135,207,223,231,224,0,0,0,3,7,7,15,15,31,31,63,255,127,255,255,127,255,191,111,191,119,95,183,79,191,95,191,95,7,23,143,223,247,255,247,255,255,255,255,255,255,255,255,255,245,215,111,255,255,255,253,252,241,192,132,
    207,207,203,195,131,0,128,240,124,62,222,255,223,223,143,147,159,33,7,13,19,4,4,0,0,0,0,3,0,0,1,6,3,3,0,1,2,3,0,1,6,2,5,3,0,2,133,11,198,33,213,99,85,177,231,90,181,239,187,239,63,239,94,184,231,5,23,127,151,127,251,71,
    54,125,56,153,128,16,254,105,14,143,141,131,6,73,247,170,4,16,64,2,4,0,0,0,0,0,0,0,0,0,0,0,0,128,0,128,32,128,80,128,0,160,0,144,0,131,8,67,20,67,21,178,79,181,74,189,134,187,86,189,11,64,181,105,210,128,64,0,19,127,2,132
]))

gs.drawSprite(girlSprite)
gs.update()
waitKey()

gs.drawSprite(parrotSprite)
gs.update()
waitKey()

gs.stop()

thumby.reset()
