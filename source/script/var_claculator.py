from source.script.game_vars import Vars

pygame = Vars.pygame


def kelvin_nise(num):
    return {True: 0, False: num}[num < 0]


def calc_camera_shift():
    mouse_pos = list(pygame.mouse.get_pos())

    # Check if the mouse is not on screen, if so, modify the values
    if mouse_pos[0] < 0:
        mouse_pos[0] = 0
    elif mouse_pos[0] > Vars.SCREEN_WIDTH:
        mouse_pos[0] = Vars.SCREEN_WIDTH

    if mouse_pos[1] < 0:
        mouse_pos[1] = 0
    elif mouse_pos[1] > Vars.SCREEN_HEIGHT:
        mouse_pos[1] = Vars.SCREEN_HEIGHT

    Vars.camera_shift_x = -(mouse_pos[0] - Vars.X_SCREEN_SHIFT) / 5
    Vars.camera_shift_y = -(mouse_pos[1] - Vars.Y_SCREEN_SHIFT) / 5
