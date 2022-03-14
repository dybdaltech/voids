import pygame
import esper

from game.helpers.drawable_forms import Forms

class TextComponent:
    def __init__(self, text, position, color=None):
        self.text = text
        self.position = position
        self.color = color

    