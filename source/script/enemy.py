from source.script.game_vars import Vars

import random
import json
import os

pygame = Vars.pygame
enemy_image_prefix = pygame.image.load(os.path.join("source", "assets", "enemy_img"))
enemy_id_path = os.path.join("source", "assets", "enemy_ids.json")

with open(enemy_id_path, 'r') as file:
    data = json.load(file)


class Enemy:
    def __init__(self, id_):
        self.image = os.path.join(enemy_image_prefix, id_)

    def dot_0(self):
        pass


class EnemySprite(pygame.sprite.Sprite, Enemy):
    def __init__(self):
        super().__init__(data["idList"])

        # Define vars for sprite
        # TODO: Create the image for the enemies
        self.id = random.randint(0, 1)  # 1 to 1
        self.rect = self.img.get_rect(center=(Vars.X_SCREEN_SHIFT, Vars.Y_SCREEN_SHIFT))
        self.mask = pygame.mask.from_surface(self.img)

        # Define other vars
        self.x: int = random.randint(0, 450)
        self.y: int = round(500 / self.x)

        print(self.x, self.y)
