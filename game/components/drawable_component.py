import pygame
import esper

class Drawable:
    def __init__(self, draw_form, posx, posy, depth=0, image=None):
        self.image = image
        self.draw_form = draw_form
        self.depth = depth
        self.x = posx
        self.y = posy
        if draw_form == "rect":
            self.h = 10
            self.w = 10
        else:
            self.w = image.get_width()
            self.h = image.get_height()

    