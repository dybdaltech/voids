from shutil import move
import pygame, logging
import esper
from game.components.drawable_component import Drawable
from game.components.Velocity_component import Velocity
from game.components.void_component import VoidComponent, VoidType
from game.components.Clock_component import ClockComponent

from game.processors.RenderProcessor import RenderProcessor
from game.processors.MovementProcessor import MovementProcessor
from game.processors.VoidProcessor import VoidProcessor
from game.processors.ClockProcessor import ClockProcessor
from game.helpers.drawable_forms import Rectangle, Forms, FormColor, TextForm

from random import randint

logger = logging.getLogger("game_debug")

FPS = 100
RESOLUTION = 1280, 840

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Voids Esper")
        self.pygame_clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 1)

        #init world
        self.world = esper.World()

        self.boids = []
        self.hoiks = []

        for i in range(0, 10):
            enemy = self.world.create_entity()
            _form = Rectangle
            _form.width = 10
            _form.height = 10
            _form.FormType = Forms.SQUARE
            _form.FormColor = FormColor.BLUE
            
            pos_x = randint(0, RESOLUTION[0])
            pos_y = randint(0, RESOLUTION[1])
            self.world.add_component(enemy, Drawable(form=_form, posx=pos_x, posy=pos_y)) 
            self.world.add_component(enemy, Velocity(0, 0))   
            self.world.add_component(enemy, VoidComponent(void_type=VoidType.BOID, ttl=randint(1, 1000), x=pos_x, y=pos_y))
            self.world.add_component(enemy, ClockComponent(pygame.time.Clock()))
            self.boids.append(enemy)
            logger.debug(f"[INIT] Enemy: {enemy} | {i} | {_form.FormType}")
            hoik = self.world.create_entity()
            form = Rectangle
            form.width = 5
            form.height = 5
            form.FormType = Forms.RECTANGLE
            form.FormColor = FormColor.GREEN
            print(hoik)
            print(enemy)
            pos_x = randint(0, RESOLUTION[0])
            pos_y = randint(0, RESOLUTION[1])
            self.world.add_component(hoik, Drawable(form=form, posx=pos_x, posy=pos_y)) 
            self.world.add_component(hoik, Velocity(0, 0))   
            self.world.add_component(hoik, VoidComponent(void_type=VoidType.HOIK, ttl=randint(1, 1000), x=pos_x, y=pos_y))
            self.world.add_component(hoik, ClockComponent(pygame.time.Clock()))
            self.hoiks.append(hoik)
            logger.debug(f"[INIT] Friend: {hoik} | {i} | {form.FormType}")
            #TODO: Add TTL to each voidling
            
        #for y in range(0, 10):
        #    pass
        #    #TODO: Add TTL to each voidling
        
        self.text_display = self.world.create_entity()
        textform = TextForm
        textform.text = ""
        textform.FormColor = FormColor.WHITE
        textform.FormType = Forms.TEXT
        self.world.add_component(self.text_display, Drawable(form=textform, posx=0, posy=20))

        self.clock = self.world.create_entity()
        self.world.add_component(self.clock, ClockComponent(pygame.time.Clock()))


        render_processor = RenderProcessor(self.window)
        movement_processor = MovementProcessor(minx=0, maxx=RESOLUTION[0], miny=0, maxy=RESOLUTION[1])
        void_processor = VoidProcessor()
        clock_processor = ClockProcessor()

        self.world.add_processor(void_processor)
        self.world.add_processor(render_processor)
        self.world.add_processor(movement_processor)
        self.world.add_processor(clock_processor)
        logger.debug(f"[INIT] After Processor - all hoiks: {self.hoiks}")
        self.running = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def process(self):
        self.world.process()
        t = self.world.component_for_entity(self.clock, ClockComponent).clock
        self.world.component_for_entity(self.text_display, Drawable).form.text = f"FPS: {t.get_fps():2.0f} | voids alive: {len(self.boids)} | t: {t.get_time()}"


