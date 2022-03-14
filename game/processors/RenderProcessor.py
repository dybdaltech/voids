import esper
import pygame

from game.components.drawable_component import Drawable
from game.helpers.drawable_forms import Forms

class RenderProcessor(esper.Processor):
    def __init__(self, window, clear_color=(0, 0, 0)):
        super().__init__()
        self.window = window
        self.clear_color = clear_color
        self.font = pygame.font.SysFont(None, 48)

    def process(self):
        # Clear the window:
        self.window.fill(self.clear_color)
        # This will iterate over every Entity that has this Component, and blit it:
        for ent, rend in self.world.get_component(Drawable):
            if rend.form.FormType == Forms.RECTANGLE:
                item = pygame.Rect(rend.x, rend.y, rend.w, rend.h)
                pygame.draw.rect(self.window, rend.form.FormColor.value, item)
            elif rend.form.FormType == Forms.TEXT:
                text = self.font.render(rend.form.text, True, rend.form.FormColor.value)
                self.window.blit(text, (rend.x, rend.y))

            else:
                return
        
        #TODO: Dirty text render:
        

        

        # Flip the framebuffers
        pygame.display.flip()