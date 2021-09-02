from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
class DemoApp(MDApp):
    def build(self):
        screen=Screen()
        table=MDDataTable(pos_hint={'center_x':0.5,'center_y':0.5},
        size_hint=(0.9,0.6),check=True,rows_num=13,
        column_data=[("No.",dp(20)),("calories",dp(20)),("food",dp(20))],
        row_data=[("1","Burger","300"),("2","pizza","300"),("3","Burger","300"),
        ("4","Burger","300"),("5","pizza","300"),("6","Burger","300"),
        ("7","Burger","300"),("8","pizza","300"),("9","Burger","300"),
        ("10","Burger","300"),("11","pizza","300"),("12","Burger","300"),
        ])
        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)
        screen.add_widget(table)
        return screen
    def check_press(self,instance_table,current_row):
        print(instance_table,current_row)
    def row_press(self,instance_table,current_row):
        print(instance_table,current_row)

DemoApp().run()