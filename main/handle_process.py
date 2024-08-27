from flet import Page, View
from main.constructor.constructorStarters import constructorStarters


def start(page: Page):
    page.title = 'Pykemon'

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

    page.on_route_change = changeRoute
    page.go(page.route)
