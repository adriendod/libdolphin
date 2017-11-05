import yaml
import libdolphin
import os

with open(os.path.dirname(__file__) + "/data/character_select.yaml", "r") as f:
    menu_data = yaml.load(f.read())

# THIS IS A HACK AND NEEDS TO BE CHANGED TO MAKE IT PERMANENT, BUT IT MAKES IT
# EASIER TO TEST IF IT EXISTS AS A HACK FOR NOW
def select_character(game, controller, character, player):
    x = menu_data[character]['x']
    y = menu_data[character]['y']
    x_diff = x - game.global_data['p2_cursor_x']
    y_diff = y - game.global_data['p2_cursor_y']

    if abs(x_diff) >= 1.24:
        if x_diff > 0:
            x_vel = 1
        elif x_diff < 0:
            x_vel = 0
    else:
        x_vel = 0.5

    if abs(y_diff) >= 1.24:
        if y_diff < 0:
            y_vel = 0
        elif y_diff > 0:
            y_vel = 1
    else:
        y_vel = 0.5

    if abs(x_diff) >= 1.24 or abs(y_diff) >=1.24:
        controller.set_stick(libdolphin.controller.Buttons.main_stick.value,
                x_vel, y_vel, 1)

    else:
        controller.set_stick(libdolphin.controller.Buttons.main_stick.value,
                x_vel, y_vel, 1)

        controller.press_button(libdolphin.controller.Buttons.A.value,
                libdolphin.controller.Buttons.press.value, 0)
        controller.press_button(libdolphin.controller.Buttons.A.value,
                libdolphin.controller.Buttons.release.value, 60)