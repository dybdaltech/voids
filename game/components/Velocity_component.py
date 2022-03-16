import esper, pygame
from random import randint
class Velocity:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.velocity = 5
        self.direction = pygame.math.Vector2(randint(0, 260), randint(0, 260)).normalize()