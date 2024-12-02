from source.script.game_vars import Vars
from source.script.var_claculator import kelvin_nise

pygame = Vars.pygame


class Bullet:
    def __init__(self, x_vel, y_vel, source_loc, dmg=Vars.bullet_dmg):
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.loc = source_loc
        self.dmg = kelvin_nise(dmg - Vars.bullet_spam_count / 5) + 1
        self.expiry_ms = pygame.time.get_ticks() + 5 * Vars.S

    def update(self, player_loc):
        self.show(player_loc)
        self.move()

        return self.expire()

    def move(self):
        self.loc[0] += self.x_vel * 10
        self.loc[1] += self.y_vel * 10

    def show(self, player_loc):
        draw_x = (self.loc[0] - player_loc[0]) + Vars.camera_shift_x + Vars.X_SCREEN_SHIFT
        draw_y = (self.loc[1] - player_loc[1]) + Vars.camera_shift_y + Vars.Y_SCREEN_SHIFT

        pygame.draw.circle(Vars.screen, "white", [draw_x, draw_y], 3)

    def expire(self):
        if self.expiry_ms < pygame.time.get_ticks():
            return True
        else:
            return False
