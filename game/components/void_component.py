from math import sqrt
from dataclasses import dataclass
import pygame
from enum import Enum

class VoidType(Enum):
    BOID = 1
    HOIK = 2

@dataclass
class VoidComponent:
    void_type: VoidType
    x: int
    y: int
    ttl: int
    
    def distance_to_target(self, target):
        dx = self.x - target.x
        dy = self.y - target.y

        return sqrt(dx * dx + dy*dy)
