import esper
import pygame
from math import sqrt
from random import randint

from game.components.void_component import VoidType, VoidColors, VoidComponent
from game.components.Velocity_component import Velocity
from game.processors.MovementProcessor import MovementProcessor

class VoidProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, void in self.world.get_component(VoidComponent):
            #TODO: Do the AI functions
            if self.world.has_component(ent, Velocity):
                self.world.component_for_entity(ent, Velocity).x += randint(-5, 5)
                self.world.component_for_entity(ent, Velocity).y += randint(-5, 5)