from dataclasses import dataclass
import pygame

@dataclass
class ClockComponent:
    clock: pygame.time.Clock