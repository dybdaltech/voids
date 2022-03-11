import esper
import pygame

from game.components.drawable_component import Drawable

class RenderProcessor(esper.Processor):
    def __init__(self, window, clear_color=(0, 0, 0)):
        super().__init__()
        self.window = window
        self.clear_color = clear_color


    def process(self):
        # Clear the window:
        self.window.fill(self.clear_color)
        # This will iterate over every Entity that has this Component, and blit it:
        for ent, rend in self.world.get_component(Drawable):
            if rend.draw_form == "rect":
                item = pygame.Rect(rend.x, rend.y, rend.w, rend.h)
                pygame.draw.rect(self.window, (255, 0,0), item)
            elif rend.draw_form == "image":

                self.window.blit(rend.image, (rend.x, rend.y))
            else:
                return
        # Flip the framebuffers
        pygame.display.flip()