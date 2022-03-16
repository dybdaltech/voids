import esper
import pygame
#
from random import randint
from game.components.Velocity_component import Velocity
from game.components.drawable_component import Drawable

class MovementProcessor(esper.Processor):
    def __init__(self, minx, miny, maxx, maxy):
        super().__init__()  
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
    def move_to(self, entity):
        pygame.math.Vector2(randint(0, 260), randint(0, 260)).normalize()
        entity.pos += entity.direction * entity.velocity    

    def process(self):
        for ent, (vel, rend) in self.world.get_components(Velocity, Drawable):
            self.move_to(vel)
            pass 
            
            #rend.x += vel.pos[0]
            #rend.y += vel.pos[1]
            #rend.x = max(self.minx, rend.x)
            #rend.y = max(self.miny, rend.y)
            #rend.x = min(self.maxx - rend.w, rend.x)
            #rend.y = min(self.maxy - rend.h, rend.y)