import esper
import pygame
from math import sqrt

from game.components.void_component import VoidType, VoidColors, VoidComponent
from game.components.Velocity_component import Velocity


class VoidProcessor(esper.Processor):
    def __init__(self) -> None:
        super().__init__()





    def process(self):
        for ent, void in self.world.get_component(VoidComponent, Velocity):
            #TODO: Do the AI functions
            pass