from game import Game
import logging

logging.basicConfig(filename="game_debug.log", level=logging.DEBUG)
logger = logging.getLogger("game_debug")
t_out = logging.StreamHandler()

logger.setLevel(logging.INFO)
t_out.setLevel(logging.INFO)

logger.addHandler(t_out)
logger.info(f"[MAIN] Started logger")

if __name__ == '__main__':
    g = Game()

    while g.running:
        g.events()
        g.process()