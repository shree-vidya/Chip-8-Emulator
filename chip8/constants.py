from pygame import Color, color
import os
from enum import Enum

# Path for font file
FILEPATH = os.path.join(os.getcwd(), "Resources")

# Default game files path
GAMEFILEPATH = os.path.join(os.getcwd(), "Resources", "Games")

# The height of the screen in pixels. Note this may be augmented by the
# scale_factor set by the initializer.
SCREENHEIGHT = {
    "normal": 32,
    "extended": 64
}

# The width of the screen in pixels. Note this may be augmented by the
# scale_factor set by the initializer.
SCREENWIDTH = {
    "normal": 64,
    "extended": 128
}

# The format of the colors is in RGBA format.
PIXELCOLORS = {
    0: Color(0, 0, 0, 255),
    1: Color(250, 250, 250, 255)
}

class Coverpage(Color, Enum):
    BACKGROUND = Color(255, 0, 255, 255)