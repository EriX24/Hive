# Internal
from source.script.game_vars import Vars
from source.script.player import Player
from source.script.var_claculator import *

# External
import sys

pygame = Vars.pygame

player = pygame.sprite.GroupSingle(Player())
enemy_group = pygame.sprite.Group()
# TODO: Add the enemy group


def loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Fill the screen
    Vars.screen.fill("black")

    # Calculate new value for the vars'
    calc_camera_shift()

    # Player stuff
    player_loc = player.update()

    # TODO: Also update the enemies

    # Pygame stuff
    Vars.clock.tick(Vars.FPS)
    pygame.display.update()
