import pygame
import esper

from game.helpers.drawable_forms import Forms

class Drawable:
    def __init__(self, form, posx, posy, depth=0, image=None):
        self.image = image
        self.form = form
        self.depth = depth
        self.x = posx
        self.y = posy
        if form.FormType == Forms.RECTANGLE:
            self.h = form.height
            self.w = form.width

        if form.FormType == Forms.SQUARE:
            self.h = form.height
            self.w = form.width
        if form.FormType == Forms.TEXT:
            pass

    