from views.viewStarters import ViewStarters


class ControllerStarters:
    def __init__(self, starters_screen: ViewStarters) -> None:
        self.starters_screen = starters_screen
        self.img_icon_bulbasaur = starters_screen.img_icon_bulbasaur
        self.img_icon_charmander = starters_screen.img_icon_charmander
        self.img_icon_squirtle = starters_screen.img_icon_squirtle
        self.img_icon_bulbasaur.on_hover = self.change_icon_bulbasaur
        self.img_icon_charmander.on_hover = self.change_icon_charmander
        self.img_icon_squirtle.on_hover = self.change_icon_squirtle
        self.img_icon_bulbasaur.on_click = self.battle_charmander
        self.img_icon_charmander.on_click = self.battle_squirtle
        self.img_icon_squirtle.on_click = self.battle_bulbasaur

    def change_icon_bulbasaur(self, e):
        if self.img_icon_bulbasaur.content.src == 'img_icon_bulbasaur.png':
            self.img_icon_bulbasaur.content.src = 'img_icon_bulbasaur-hover.png'
            self.img_icon_bulbasaur.update()
        else:
            self.img_icon_bulbasaur.content.src = 'img_icon_bulbasaur.png'
            self.img_icon_bulbasaur.update()

    def change_icon_charmander(self, e):
        if self.img_icon_charmander.content.src == 'img_icon_charmander.png':
            self.img_icon_charmander.content.src = 'img_icon_charmander-hover.png'
            self.img_icon_charmander.update()
        else:
            self.img_icon_charmander.content.src = 'img_icon_charmander.png'
            self.img_icon_charmander.update()

    def change_icon_squirtle(self, e):
        if self.img_icon_squirtle.content.src == 'img_icon_squirtle.png':
            self.img_icon_squirtle.content.src = 'img_icon_squirtle-hover.png'
            self.img_icon_squirtle.update()
        else:
            self.img_icon_squirtle.content.src = 'img_icon_squirtle.png'
            self.img_icon_squirtle.update()

    def battle_charmander(self, e):
        self.starters_screen.page.go('/vs-charmander')

    def battle_squirtle(self, e):
        self.starters_screen.page.go('/vs-squirtle')

    def battle_bulbasaur(self, e):
        self.starters_screen.page.go('/vs-bulbasaur')
