
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.storage.jsonstore import JsonStore
helpstr="""     
    WelcomeScreen:
    UsernameScreen:
    
<WelcomeScreen>:
    name:'WelcomeScreen'
<UsernameScreen>:
    name:'UsernameScreen'
    
"""
class WelcomeScreen(Screen):
    pass
class UsernameScreen(Screen):
    pass
sm=ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(UsernameScreen(name='usernamescreen'))
class DemoApp(MDApp):
    def build(self):
        self.strng=Builder.load_string(helpstr)
        return self.strng