from math import sqrt
from dataclasses import dataclass
import enum
import pygame
from enum import Enum

class VoidType(Enum):
    BOID = 1
    HOIK = 2

class VoidColors(Enum):
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0,255, 0)


@dataclass
class VoidComponent:
    void_type: VoidType
    color: VoidColors
    x: int
    y: int
    
    def distance_to_target(self, target):
        dx = self.x - target.x
        dy = self.y - target.y

        return sqrt(dx * dx + dy*dy)
