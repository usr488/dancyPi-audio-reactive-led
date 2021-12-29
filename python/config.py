"""Settings for audio reactive LED strip"""
from __future__ import print_function
from __future__ import division
import os

DEVICE = 'pi'

"""Device used to control LED strip. Must be 'pi',  'esp8266' or 'blinkstick'

'esp8266' means that you are using an ESP8266 module to control the LED strip
and commands will be sent to the ESP8266 over WiFi.

'pi' means that you are using a Raspberry Pi as a standalone unit to process
audio input and control the LED strip directly.

'blinkstick' means that a BlinkstickPro is connected to this PC which will be used
to control the leds connected to it.
"""

if DEVICE == 'esp8266':
    UDP_IP = '192.168.0.150'
    """IP address of the ESP8266. Must match IP in ws2812_controller.ino"""
    UDP_PORT = 7777
    """Port number used for socket communication between Python and ESP8266"""
    SOFTWARE_GAMMA_CORRECTION = False
    """Set to False because the firmware handles gamma correction + dither"""

if DEVICE == 'pi':
    LED_PIN = 18
    """GPIO pin connected to the LED strip pixels (must support PWM)"""
    LED_FREQ_HZ = 800000
    """LED signal frequency in Hz (usually 800kHz)"""
    LED_DMA = 5
    """DMA channel used for generating PWM signal (try 5)"""
    BRIGHTNESS = 255
    """Brightness of LED strip between 0 and 255"""
    LED_INVERT = False
    """Set True if using an inverting logic level converter"""
    SOFTWARE_GAMMA_CORRECTION = True
    """Set to True because Raspberry Pi doesn't use hardware dithering"""

if DEVICE == 'blinkstick':
    SOFTWARE_GAMMA_CORRECTION = True
    """Set to True because blinkstick doesn't use hardware dithering"""

USE_GUI = False
"""Whether or not to display a PyQtGraph GUI plot of visualization"""

DISPLAY_FPS = True
"""Whether to display the FPS when running (can reduce performance)"""

N_PIXELS = 144
"""Number of pixels in the LED strip (must match ESP8266 firmware)"""

GAMMA_TABLE_PATH = os.path.join(os.path.dirname(__file__), 'gamma_table.npy')
"""Location of the gamma correction table"""

MIC_RATE = 48000
"""Sampling frequency of the microphone in Hz"""

FPS = 50
"""Desired refresh rate of the visualization (frames per second)

FPS indicates the desired refresh rate, or frames-per-second, of the audio
visualization. The actual refresh rate may be lower if the computer cannot keep
up with desired FPS value.

Higher framerates improve "responsiveness" and reduce the latency of the
visualization but are more computationally expensive.

Low framerates are less computationally expensive, but the visualization may
appear "sluggish" or out of sync with the audio being played if it is too low.

The FPS should not exceed the maximum refresh rate of the LED strip, which
depends on how long the LED strip is.
"""
_max_led_FPS = int(((N_PIXELS * 30e-6) + 50e-6)**-1.0)
assert FPS <= _max_led_FPS, 'FPS must be <= {}'.format(_max_led_FPS)

MIN_FREQUENCY = 200
"""Frequencies below this value will be removed during audio processing"""

MAX_FREQUENCY = 12000
"""Frequencies above this value will be removed during audio processing"""

N_FFT_BINS = 24
"""Number of frequency bins to use when transforming audio to frequency domain

Fast Fourier transforms are used to transform time-domain audio data to the
frequency domain. The frequencies present in the audio signal are assigned
to their respective frequency bins. This value indicates the number of
frequency bins to use.

A small number of bins reduces the frequency resolution of the visualization
but improves amplitude resolution. The opposite is true when using a large
number of bins. More bins is not always better!

There is no point using more bins than there are pixels on the LED strip.
"""

N_ROLLING_HISTORY = 2
"""Number of past audio frames to include in the rolling window"""

MIN_VOLUME_THRESHOLD = 1e-7
"""No music visualization displayed if recorded audio volume below threshold"""


#OPTIONS FOR SPECTRUM MODE COLOURS

"""
These are the options for the spectrum colour mode added by Zherit

SPEC_ORDER can be any combination of the letters r, g, and b written as "xyz"
where x is the priority colour, y is the secondary, and z is tertiary. You must
have unique entries for x y and z ie. "rrb" will NOT work. You can also enter
"rand" for the colours to be randomized.

RAND_MODE can be set to "random" or "wheel" depending on if you want a truly
random colour sequence or you would like to cycle through all options one
at a time. *NOTE: SPEC_ORDER must be set to "rand" for this to work

RAND_FREQ sets the frequency at which to change the colours in "rand" mode.
It is based off of FPS so if your FPS is set to 50 then changing colours
every half second would be RAND_FREQ = 25. *NOTE: SPEC_ORDER must be set to
"rand" for this to work

RAND_NUM and CYCLE_COUNT are used by the program as variables. DO NOT TOUCH THESE


"""
SPEC_ORDER = "bgr"
RAND_MODE = "wheel"
RAND_FREQ = 15


#DO NOT TOUCH
RAND_NUM = 0
CYCLE_COUNT = 0
