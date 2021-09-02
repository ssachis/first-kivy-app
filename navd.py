from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (300, 500)
navigation_helper = """
Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"
                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height: avatar.height

                    Image:
                        id: avatar
                        size_hint: None,None
                        size: "56dp", "56dp"
                        source: "C:/Users/sachi/Music/i.png"    
       

                MDLabel:
                    text: ' sachi'
                    font_style: 'Button'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: ' singhsachi.pratap1166@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            IconLeftWidget:
                                icon:'face-profile-woman'
                                theme_text_color: "Custom": "Cyan"
                        OneLineIconListItem:
                            text:'Upload'
                            IconLeftWidget:
                                icon:'file-upload'
                        OneLineIconListItem:
                            text:'Logout'
                            IconLeftWidget:
                                icon:'logout'
    
                     

"""

class ContentNavigationDrawer(BoxLayout):
    pass
class DemoApp(MDApp):

    def build(self):
        screen= Builder.load_string(navigation_helper)
        return screen


DemoApp().run()