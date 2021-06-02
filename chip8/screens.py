"""File for reusable Components"""

from typing import Optional, Tuple
from pygame import key, display, HWSURFACE, DOUBLEBUF, Color, draw, Surface, font
import os
from .constants import *
from .utils import *

# Size of each chip-8 pixel on computer screen
SCALE = 5

class CoverScreen():

    def __init__(self, surface : Surface, height : int = SCREENHEIGHT["normal"], width : int = SCREENWIDTH["normal"], name : str = "Chip-8 Emulator"):
        self.gameFiles = [i for i in os.listdir(GAMEFILEPATH) if "." not in i]
        if len(self.gameFiles) == 0:
            raise Exception("No games found")
        self.height = height
        self.width = width
        self.surface = surface
        self.setCaption(name)
        self.clearScreen()
        display.flip()
        self.loadButtons()

    def loadButtons(self):
        self.buttons = [button(1, 1, text = i) for i in self.gameFiles]
    
    def setCaption(self, name: str):
        display.set_caption(name)

    def reinitialize(self):
        display.quit()
        display.init()
        self.screen = display.set_mode((self.width * SCALE, self.height * SCALE), HWSURFACE | DOUBLEBUF, 8)
        self.clearScreen()
        display.flip()

    def clearScreen(self) -> None:
        self.surface.fill(PIXELCOLORS[0])
    
    def draw(self):
        # Draw buttons
        pass

    def animate(self):
        pass

class GameScreen(object):

    def __init__(self, surface, height=SCREENHEIGHT["normal"], width=SCREENWIDTH["normal"], name = "Game"):
        self.height = height
        self.width = width
        self.surface = surface if surface else display.set_mode((width * SCALE, height * SCALE), HWSURFACE | DOUBLEBUF, 8)
        self.setCaption(name)
        self.clearScreen()
        display.flip()
    
    def setCaption(self, name: str):
        display.set_caption(name)

    def reinitialize(self):
        display.quit()
        display.init()
        self.screen = display.set_mode((self.width * SCALE, self.height * SCALE), HWSURFACE | DOUBLEBUF, 8)
        self.clearScreen()
        display.flip()

    def drawPixel(self, x : int, y : int, color : int) -> None:
        draw.rect(self.surface, PIXELCOLORS[color], (x * SCALE, y * SCALE, SCALE, SCALE))

    def getPixel(self, x : int, y : int) -> int:
        pixelColor = self.surface.get_at((x * SCALE, y * SCALE))
        if pixelColor == PIXELCOLORS[0]:
            return 0
        return 1

    def clearScreen(self) -> None:
        self.surface.fill(PIXELCOLORS[0])

    def setExtended(self):
        # Destroys the current screen object
        self.height = SCREENHEIGHT['extended']
        self.width = SCREENWIDTH['extended']
        self.reinitialize()

    def setNormal(self):
        # Destroys the current screen object
        self.height = SCREENHEIGHT['normal']
        self.width = SCREENWIDTH['normal']
        self.reinitialize()

    # def scrollDown(self, num_lines):
    #     """
    #     Scroll the screen down by num_lines.
        
    #     :param num_lines: the number of lines to scroll down 
    #     """
    #     for y_pos in range(self.height - num_lines, -1, -1):
    #         for x_pos in range(self.width):
    #             pixel_color = self.getPixel(x_pos, y_pos)
    #             self.drawPixel(x_pos, y_pos + num_lines, pixel_color)

    #     # Blank out the lines above the ones we scrolled
    #     for y_pos in range(num_lines):
    #         for x_pos in range(self.width):
    #             self.drawPixel(x_pos, y_pos, 0)

    #     display.flip()

    # def scrollLeft(self):
    #     """
    #     Scroll the screen left 4 pixels.
    #     """
    #     for y_pos in range(self.height):
    #         for x_pos in range(4, self.width):
    #             pixel_color = self.getPixel(x_pos, y_pos)
    #             self.drawPixel(x_pos - 4, y_pos, pixel_color)

    #     # Blank out the lines to the right of the ones we just scrolled
    #     for y_pos in range(self.height):
    #         for x_pos in range(self.width - 4, self.width):
    #             self.drawPixel(x_pos, y_pos, 0)

    #     display.flip()

    # def scrollRight(self):
    #     """
    #     Scroll the screen right 4 pixels.
    #     """
    #     for y_pos in range(self.height):
    #         for x_pos in range(self.width - 4, -1, -1):
    #             pixel_color = self.getPixel(x_pos, y_pos)
    #             self.drawPixel(x_pos + 4, y_pos, pixel_color)

    #     # Blank out the lines to the left of the ones we just scrolled
    #     for y_pos in range(self.height):
    #         for x_pos in range(4):
    #             self.drawPixel(x_pos, y_pos, 0)
    #     display.flip()
