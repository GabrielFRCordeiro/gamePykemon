from flet import Page, View, Audio
from main.constructor.constructorStarters import constructor_starters
from main.constructor.constructorVsCharmander import constructorVsCharmander
from main.constructor.constructorVsSquirtle import constructorVsSquirtle
from main.constructor.constructorVsBulbasaur import constructorVsBulbasaur


def start(page: Page):
    page.title = 'Pykemon'
    page.fonts = {
        'PressStart2P': 'fonts/PressStart2P-Regular.ttf'
    }
    soundtrack_starters = Audio('assets/soundtrack_starters.mp3', autoplay=True)

    def change_route(route):
        page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[
                    constructor_starters()
                ]
            )
        )

        if page.route == '/':
            page.overlay.append(soundtrack_starters)

        if page.route == '/vs-charmander':
            soundtrack_starters.pause()
            page.views.append(
                View(
                    route='/vs-charmander',
                    controls=[
                        constructorVsCharmander(),
                    ]
                )
            )

        if page.route == '/vs-squirtle':
            soundtrack_starters.pause()
            page.views.append(
                View(
                    route='/vs-squirtle',
                    controls=[
                        constructorVsSquirtle(),
                    ]
                )
            )

        if page.route == '/vs-bulbasaur':
            soundtrack_starters.pause()
            page.views.append(
                View(
                    route='/vs-bulbasaur',
                    controls=[
                        constructorVsBulbasaur(),
                    ]
                )
            )

        page.update()

    page.on_route_change = change_route
    page.go(page.route)
