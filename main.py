from chip8.screens import CoverScreen
import pygame
from pygame import display, event
from chip8 import *

pygame.init()
cover = CoverScreen()
loop = True
while loop:
    for e in event.get():
        if e.type == pygame.QUIT:
            loop = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if (button := cover.buttonClicked()):
                    print(button)
    cover.draw()
    display.update()

# if __name__ == "__main__":
#     ...