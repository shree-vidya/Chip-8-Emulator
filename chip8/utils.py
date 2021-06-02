
'''File for coverpages'''

from pygame import Surface, font, draw
from typing import Optional, Tuple
from .constants import FILEPATH
import os


class button():
    def __init__(self, x, y, color = (0, 0, 0), width = 10, height = 10, textcolor = (255 ,255 ,255), text = '', size=60):
        # Change constructor
        self.color = color

        # If animated, set these below values runtime
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # ----------------------------------------------
        self.text = text
        self.textcolor = textcolor
        self.size = size

    def draw(self, surface : Surface, outline : Optional[int] = None):
        if outline:
            draw.rect(surface, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        draw.rect(surface, self.color, (self.x,self.y,self.width,self.height),0)
        if self.text != '':
            text = font.Font(os.path.join(FILEPATH, 'Fonts', 'MaidenOrange.ttf'), self.size).render(self.text, 1, self.textcolor)
            surface.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)+10))

    def isOver(self, pos : Tuple[int, int]):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
    

if __name__ == "__main__":
    ...