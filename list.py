from kivymd.app import MDApp
#from kivymd.uix.screen import Screen
#from kivymd.uix.list import MDList, OneLineListItem,TwoLineListItem,TwoLineIconListItem
#from kivy.uix.scrollview import ScrollView
#from kivymd.uix.list import IconLeftWidget,TwoLineAvatarListItem,ImageLeftWidget
from kivy.lang import Builder
from kivymd.uix.list import  OneLineListItem,TwoLineAvatarListItem,ImageLeftWidget
list_helper="""
Screen:
    ScrollView:
        MDList:
            id:container


"""
class DemoApp(MDApp):
    def build(self):
        #screen=Screen()
        #scroll=ScrollView()
        #list_view=MDList()
        screen=Builder.load_string(list_helper)
        #for i in range(20):
         #   hi=ImageLeftWidget(source=r"C:\Users\sachi\Music\i.png")
          #  items =TwoLineAvatarListItem(text='Item '+str(i),secondary_text='hi')
           # items.add_widget(hi)
            #list_view.add_widget(items)

        #scroll.add_widget(list_view)
        #screen.add_widget(scroll)
        return screen

    def on_start(self):
        for i in range(20):
            hi=ImageLeftWidget(source=r"C:\Users\sachi\Music\i.png")
            items =TwoLineAvatarListItem(text='Recipe '+str(i),secondary_text='breakfast')
            items.add_widget(hi)
            self.root.ids.container.add_widget(items)


DemoApp().run()
