from views.viewStarters import ViewStarters
from controller.controllerStarters import ControllerStarters


def constructor_starters():
    starters_screen = ViewStarters()
    controller_starters = ControllerStarters(starters_screen)

    return starters_screen
