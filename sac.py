from kivymd.app import MDApp
from kivymd.uix.screeen import Screen
from kivymd.uix.datatable import MDDAtatable
class DemoApp(MDApp):
    def build(self):
        screen=Screen()
        table=MDDatatale(colomn_data=[("food",dp(30)),("calories",dp(30))])
        screen.add_widget(table)
        return screen

DemoApp()Run()