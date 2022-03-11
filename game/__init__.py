from shutil import move
import pygame
import esper
from game.components.drawable_component import Drawable
from game.components.Velocity_component import Velocity
from game.processors.RenderProcessor import RenderProcessor
from game.processors.MovementProcessor import MovementProcessor



FPS = 60
RESOLUTION = 720, 480

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Voids Esper")
        print(self.window)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 1)

        #init world
        self.world = esper.World()
        self.entity = self.world.create_entity()
        self.world.add_component(self.entity, Velocity(0, 0))
        self.world.add_component(self.entity, Drawable(draw_form="rect", posx=100, posy=100))

        self.enemy = self.world.create_entity()
        self.world.add_component(self.enemy, Drawable(draw_form="image", image=pygame.image.load("bluesquare.png"), posx=10, posy=100))


        render_processor = RenderProcessor(self.window)
        movement_processor = MovementProcessor(minx=0, maxx=RESOLUTION[0], miny=0, maxy=RESOLUTION[1])

        self.world.add_processor(render_processor)
        self.world.add_processor(movement_processor)

        self.running = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def process(self):
        self.world.process()
        self.clock.tick(FPS)

