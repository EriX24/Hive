import pygame
import os


class Vars:
    # Consts
    FPS: int = 60
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    X_SCREEN_SHIFT: int = SCREEN_WIDTH / 2
    Y_SCREEN_SHIFT: int = SCREEN_HEIGHT / 2
    CAMERA_SHIFT: int = 390

    PLAYER_DIR = 0
    PIXEL_SIZE = 2
    S = 1000

    # TODO: Implement the map
    MAP_WIDTH = 0
    MAP_HEIGHT = 0

    # Vars
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame = pygame

    player_img_link: str = os.path.join("source", "assets", "../assets/player.png")
    player_speed: int = 5
    camera_shift_x: int = 0
    camera_shift_y: int = 0
    bullet_dmg: int | float = 5
    bullet_spam_count: int = 0
