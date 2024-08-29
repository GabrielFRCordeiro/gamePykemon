from views.viewStarters import ViewStarters
from controller.controllerStarters import ControllerStarters


def constructorStarters():
    startersScreen = ViewStarters()
    controllerStarters = ControllerStarters(startersScreen)

    return startersScreen
