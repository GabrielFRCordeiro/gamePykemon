from flet import Page, View
from main.constructor.constructorStarters import constructor_starters
from main.constructor.constructorVsCharmander import constructorVsCharmander
from main.constructor.constructorVsSquirtle import constructorVsSquirtle
from main.constructor.constructorVsBulbasaur import constructorVsBulbasaur


def start(page: Page):
    page.title = 'Pykemon'

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

        if page.route == '/vs-charmander':
            page.views.append(
                View(
                    route='/vs-charmander',
                    controls=[
                        constructorVsCharmander(),
                    ]
                )
            )

        if page.route == '/vs-squirtle':
            page.views.append(
                View(
                    route='/vs-squirtle',
                    controls=[
                        constructorVsSquirtle(),
                    ]
                )
            )

        if page.route == '/vs-bulbasaur':
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
