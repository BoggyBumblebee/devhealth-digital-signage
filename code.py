# SPDX-FileCopyrightText: 2022 Christopher Marsh-Bourdon (boggybumblebee)
#
# SPDX-License-Identifier: MIT

"""
DEVELOPMENT HEALTH DIGITAL SIGNAGE for Adafruit Matrix Portal: displays stats about GitHub/SonarQube projects. 
Requires WiFi internet access.

Written by Christopher Marsh-Bourdon (boggybumblebee).
MIT license, all text above must be included in any redistribution.

BDF fonts from the X.Org project.
"""

# pylint: disable=import-error
import gc
import time
import math
import board
import busio
import displayio
from rtc import RTC
from adafruit_matrixportal.network import Network
from adafruit_matrixportal.matrix import Matrix
from adafruit_bitmap_font import bitmap_font
import adafruit_display_text.label
import adafruit_lis3dh

try:
    from secrets import secrets
except ImportError:
    print('WiFi secrets are kept in secrets.py, please add them there!')
    raise

# CONFIGURABLE SETTINGS ----------------------------------------------------

BITPLANES = 6      # Ideally 6, but can set lower if RAM is tight

# SOME UTILITY FUNCTIONS AND CLASSES ---------------------------------------

# ONE-TIME INITIALIZATION --------------------------------------------------

MATRIX = Matrix(bit_depth=BITPLANES)
DISPLAY = MATRIX.display
ACCEL = adafruit_lis3dh.LIS3DH_I2C(busio.I2C(board.SCL, board.SDA), address=0x19)
_ = ACCEL.acceleration # Dummy reading to blow out any startup residue
time.sleep(0.1)
DISPLAY.rotation = (int(((math.atan2(-ACCEL.acceleration.y,
                                     -ACCEL.acceleration.x) + math.pi) /
                         (math.pi * 2) + 0.875) * 4) % 4) * 90

SMALL_FONT = bitmap_font.load_font('/fonts/helvR10.bdf')
SMALL_FONT.load_glyphs('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_/!?')

# Display group is set up once, then we just shuffle items around later.
# Order of creation here determines their stacking order.
GROUP = displayio.Group()

# Element 0 is a stand-in item (splash screen), later replaced with the scrolling badges
# pylint: disable=bare-except
try:
    FILENAME = 'images/devhealth.bmp'

    # CircuitPython 7+ compatible
    BITMAP = displayio.OnDiskBitmap(FILENAME)
    TILE_GRID = displayio.TileGrid(BITMAP, pixel_shader=BITMAP.pixel_shader)

    GROUP.append(TILE_GRID)
except:
    GROUP.append(adafruit_display_text.label.Label(SMALL_FONT, color=0xFF0000, text='Whoops!'))
    GROUP[0].x = (DISPLAY.width - GROUP[0].bounding_box[2] + 1) // 2
    GROUP[0].y = DISPLAY.height // 2 - 1

DISPLAY.show(GROUP)

NETWORK = Network(status_neopixel=board.NEOPIXEL, debug=False)
NETWORK.connect()

# MAIN LOOP ----------------------------------------------------------------

while True:
    gc.collect()
    NOW = time.time() # Current epoch time in seconds

    DISPLAY.refresh() # Force full repaint (splash screen sometimes sticks)
    time.sleep(5)
