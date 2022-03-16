import esper

from game.components.Clock_component import ClockComponent

class ClockProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, clock in self.world.get_component(ClockComponent):
            clock.clock.tick(3)