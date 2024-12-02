from source.script.game_vars import Vars
import random


class Hive:
    def __init__(self):
        self.score = 0

    # TODO: Make the spawn function's type_ param pick out of the list in enemy_ids.json
    def spawn(self, x=random.randint(-int(Vars.MAP_WIDTH / 2), int(Vars.MAP_WIDTH / 2)),
              y=random.randint(-int(Vars.MAP_HEIGHT / 2), int(Vars.MAP_HEIGHT / 2)), type_=random.randint(1, 10)):
        pass
