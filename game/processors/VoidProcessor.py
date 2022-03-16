import esper
import pygame
from math import sqrt
from random import randint
import logging
from game.components.void_component import VoidType, VoidComponent
from game.components.Velocity_component import Velocity
from game.components.Clock_component import ClockComponent
#from game.processors.MovementProcessor import MovementProcessor

logger = logging.getLogger("game_debug")

class VoidProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

        self.timer_event = pygame.USEREVENT+1
        pygame.time.set_timer(self.timer_event, 1000)

    #def move_to(self, entity):
    #    entity.pos += entity.direction * entity.velocity    

    def process(self):
        for ent, void in self.world.get_component(VoidComponent):
            #TODO: Do the AI functions
            logger.debug(f"[Voidling Processor] {ent} | {self.world.component_for_entity(ent, VoidComponent).void_type}")
            if self.world.has_component(ent, Velocity):
                pass
            if self.world.has_component(ent, ClockComponent):
                a = self.world.component_for_entity(ent, ClockComponent).clock.get_time()
                if void.ttl == randint(1, 1000):
                    self.world.delete_entity(ent)
        for event in pygame.event.get():
            if event.type == self.timer_event:
                print("test")