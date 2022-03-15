import esper
import pygame
import logging

logger = logging.getLogger("game_debug")

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
                col = self.world.component_for_entity(ent, Drawable).form.FormColor
                pygame.draw.rect(self.window, col, item)
                logger.debug(f"[Render Processor] {ent} | {col} | {rend}")
                #pygame.draw.rect(self.window, ent.form.FormColor.value, item)
            elif rend.form.FormType == Forms.TEXT:
                text = self.font.render(rend.form.text, True, rend.form.FormColor)
                self.window.blit(text, (rend.x, rend.y))

            else:
                return
        
        #TODO: Dirty text render:
        

        

        # Flip the framebuffers
        pygame.display.flip()