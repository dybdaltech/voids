from math import dist
import esper
import pygame
#
from random import randint
from game.components.Velocity_component import Velocity
from game.components.drawable_component import Drawable
from game.components.void_component import VoidComponent

class MovementProcessor(esper.Processor):
    def __init__(self, minx, miny, maxx, maxy):
        super().__init__()  
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy


    def get_voids_vicinity(self, entity):
        others = []
        for ent, (void, vel) in self.world.get_components(VoidComponent, Velocity):
            if void.void_type == 2:
                others.append(ent)
        return others

    def get_distance_to_target(self, entity, target):
        distance = entity.pos.distance_to(target.pos)
        return distance

    def move_to(self, entity, target=None):
        others = self.get_voids_vicinity(entity)
        target = pygame.math.Vector2(1, 1)
        for other in others:
            other_pos = self.world.component_for_entity(other, Velocity)
            distance = self.get_distance_to_target(entity, other_pos)
            if distance <= 30:
                target = other_pos.pos
            else:
                continue
        if target[0] <= 1 or target[0] >= 500:
            target[0] = 0
        elif target[1] <= 1 or target[1] >= 500:
            target[1] = 0
        
        print(target)
        entity.direction = target
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