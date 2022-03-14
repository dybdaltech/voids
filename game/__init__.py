from shutil import move
import pygame
import esper
from game.components.drawable_component import Drawable
from game.components.Velocity_component import Velocity
from game.components.void_component import VoidComponent, VoidType
from game.components.Text_component import TextComponent

from game.processors.RenderProcessor import RenderProcessor
from game.processors.MovementProcessor import MovementProcessor
from game.processors.VoidProcessor import VoidProcessor
from game.helpers.drawable_forms import Rectangle, Forms, FormColor, TextForm

from random import randint


FPS = 100
RESOLUTION = 720, 480

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Voids Esper")
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 1)

        #init world
        self.world = esper.World()

        self.boids = []
        for i in range(0, 1000):
            enemy = self.world.create_entity()
            form = Rectangle
            form.width = 5
            form.height = 5
            form.FormType = Forms.RECTANGLE
            form.FormColor = FormColor.BLUE
            
            pos_x = randint(0, RESOLUTION[0])
            pos_y = randint(0, RESOLUTION[1])
            self.world.add_component(enemy, Drawable(form=form, posx=pos_x, posy=pos_y)) 
            self.world.add_component(enemy, Velocity(0, 0))   
            self.world.add_component(enemy, VoidComponent(void_type=VoidType.BOID, x=pos_x, y=pos_y))
            self.boids.append(enemy)
            #TODO: Add TTL to each voidling
        self.text_display = self.world.create_entity()
        textform = TextForm
        textform.text = ""
        print(self.clock.get_fps())
        textform.FormColor = FormColor.WHITE
        textform.FormType = Forms.TEXT
        self.world.add_component(self.text_display, Drawable(form=textform, posx=0, posy=20))



        render_processor = RenderProcessor(self.window)
        movement_processor = MovementProcessor(minx=0, maxx=RESOLUTION[0], miny=0, maxy=RESOLUTION[1])
        void_processor = VoidProcessor()
        self.world.add_processor(void_processor)
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
        self.world.component_for_entity(self.text_display, Drawable).form.text = f"FPS: {self.clock.get_fps():2.0f} | voids alive: {len(self.boids)}"


