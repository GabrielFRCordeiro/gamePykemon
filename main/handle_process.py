from flet import Page, View
from main.constructor.constructorStarters import constructorStarters
from pygame import mixer
from time import sleep


def start(page: Page):
    page.title = 'Pykemon'
    page.fonts = {
        'PressStart2P': 'fonts/PressStart2P-Regular.ttf'
    }

    def changeRoute(route):
        page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[
                    constructorStarters()
                ]
            )
        )

        page.update()
        mixer.init()
        mixer.Sound('assets/soundtrack_starters.mp3').play()
        while mixer.get_busy():
            sleep(1)

    page.on_route_change = changeRoute
    page.go(page.route)
