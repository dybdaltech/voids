import esper
import pygame
#
from game.components.Velocity_component import Velocity
from game.components.drawable_component import Drawable

class MovementProcessor(esper.Processor):
    def __init__(self, minx, miny, maxx, maxy):
        super().__init__()  
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self):
        for ent, (vel, rend) in self.world.get_components(Velocity, Drawable):

            rend.x += vel.x
            rend.y += vel.y
            rend.x = max(self.minx, rend.x)
            rend.y = max(self.miny, rend.y)
            rend.x = min(self.maxx - rend.w, rend.x)
            rend.y = min(self.maxy - rend.h, rend.y)