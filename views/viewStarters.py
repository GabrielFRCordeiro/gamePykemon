from flet import (UserControl, Image, Text, ResponsiveRow, Column,
                  alignment, MainAxisAlignment, Row, CrossAxisAlignment)


class ViewStarters(UserControl):
    def __init__(self):
        super().__init__()
        self.img_logo = Image('img_logo.png')
        self.text = Text('Choose your Pykemon!')
        self.img_icon_bulbasaur = Image('img_icon_bulbasaur.png')
        self.img_icon_charmander = Image('img_icon_charmander.png')
        self.img_icon_squirtle = Image('img_icon_squirtle.png')

    def build(self):
        layout = ResponsiveRow(
            height=640,
            controls=[
                Column(col={},
                       controls=[
                           Column(col={},
                                  controls=[self.img_logo],
                                  alignment=alignment.center),
                           Column(col={},
                                  controls=[self.text],
                                  alignment=MainAxisAlignment.CENTER),
                           Row(col={},
                               controls=[
                                   self.img_icon_bulbasaur,
                                   self.img_icon_charmander,
                                   self.img_icon_squirtle
                               ],
                               alignment=MainAxisAlignment.SPACE_AROUND)
                       ],
                       alignment=MainAxisAlignment.SPACE_AROUND,
                       horizontal_alignment=CrossAxisAlignment.CENTER)  # end of main Column
            ]
        )  # end of ResponsiveRow

        return layout
