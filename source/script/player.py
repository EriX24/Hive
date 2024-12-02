from source.script.game_vars import Vars
from source.script.bullet import Bullet
from source.script.var_claculator import kelvin_nise

import math

pygame = Vars.pygame


# TODO: Show the spam number


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Init the super
        super().__init__()

        # Define vars for sprite
        self.image: pygame.image = pygame.transform.smoothscale(pygame.image.load(Vars.player_img_link).convert_alpha(),
                                                                (15 * Vars.PIXEL_SIZE, 15 * Vars.PIXEL_SIZE))
        self.image = pygame.transform.rotate(self.image, Vars.PLAYER_DIR)

        self.rect = self.image.get_rect(center=(Vars.X_SCREEN_SHIFT, Vars.Y_SCREEN_SHIFT))
        self.mask = pygame.mask.from_surface(self.image)

        # Define other vars
        self.dir: int = 0
        self.x: int = 0
        self.y: int = 0
        self.shot = []
        self.shooting = False

    def update(self):
        self.point()
        self.shoot()
        self.movement()
        self.bullet_movement()
        self.show()

        return self.x, self.y

    def point(self):
        mouse_pos = pygame.mouse.get_pos()

        self.dir = (360 - math.atan2(mouse_pos[1] - Vars.Y_SCREEN_SHIFT + Vars.camera_shift_y,
                                     mouse_pos[0] - Vars.X_SCREEN_SHIFT + Vars.camera_shift_x) * 180 / math.pi)
        self.mask = pygame.mask.from_surface(self.image)

    def show(self):
        # self.image = pygame.transform.rotate(self.image, 0)
        blit_img = pygame.transform.rotate(self.image, self.dir)
        self.rect = self.image.get_rect(center=(Vars.X_SCREEN_SHIFT + Vars.camera_shift_x,
                                                Vars.Y_SCREEN_SHIFT + Vars.camera_shift_y))

        Vars.screen.blit(blit_img, self.rect)

    def movement(self):
        # Get the keys that affect the x and y
        x_keys = [pygame.key.get_pressed()[pygame.K_a], pygame.key.get_pressed()[pygame.K_d]]
        y_keys = [pygame.key.get_pressed()[pygame.K_w], pygame.key.get_pressed()[pygame.K_s]]
        true_pressed = 0

        # Get how much the movement should be divided by
        if x_keys != [True, True]:
            true_pressed += x_keys.count(True)

        if y_keys != [True, True]:
            true_pressed += y_keys.count(True)

        player_speed = 0
        if true_pressed == 1:
            player_speed = 1
        elif true_pressed == 2:
            player_speed = math.sqrt(2) / 2

        if x_keys[0]:
            self.x -= player_speed * Vars.player_speed
        if x_keys[1]:
            self.x += player_speed * Vars.player_speed

        if y_keys[0]:
            self.y -= player_speed * Vars.player_speed
        if y_keys[1]:
            self.y += player_speed * Vars.player_speed

    def shoot(self):
        if self.shooting:
            Vars.bullet_spam_count += 1
            self.shooting = False
        else:
            Vars.bullet_spam_count -= 5

        Vars.bullet_spam_count = kelvin_nise(Vars.bullet_spam_count)

        if pygame.mouse.get_pressed()[0]:
            self.shooting = True

            mouse_pos = pygame.mouse.get_pos()
            x_vel = -((Vars.X_SCREEN_SHIFT + Vars.camera_shift_x) - mouse_pos[0])
            y_vel = -((Vars.Y_SCREEN_SHIFT + Vars.camera_shift_y) - mouse_pos[1])

            hypotenuse = math.sqrt(x_vel ** 2 + y_vel ** 2)
            x_vel /= hypotenuse
            y_vel /= hypotenuse

            spawn_x = self.x + x_vel * 20
            spawn_y = self.y + y_vel * 20

            self.shot.append(Bullet(x_vel, y_vel, [spawn_x, spawn_y]))

    def bullet_movement(self):
        del_idx_list = []
        for bullet_idx in range(len(self.shot)):
            expire = self.shot[bullet_idx].update([self.x, self.y])
            if expire:
                del_idx_list.append(bullet_idx)

        del_idx_list.sort()
        for idx in del_idx_list[::-1]:
            del self.shot[idx]
