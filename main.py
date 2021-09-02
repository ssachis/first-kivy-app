from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton,MDFloatingActionButton,MDFlatButton
#from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen,ScreenManager



from pp import username_helper,password_helper
from kivy.core.window import Window


Window.size=(300,500)
class HealthApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette='Cyan'

        screen = Screen()

        self.username=Builder.load_string(username_helper)
        screen.add_widget(self.username)
        button=MDRectangleFlatButton(text='next',pos_hint={'center_x':0.5,'center_y':0.3},on_release=self.show_data)
        screen.add_widget(button)

        self.password=Builder.load_string(password_helper)
        screen.add_widget(self.password)

        return screen
    def show_data(self,obj):
        if self.password.text=="" and self.username.text == "":
            check_string = 'please enter your credentials'
        elif self.username.text is "" and self.password.text is not "":
            check_string='please enter a username'
        elif self.username.text is not "" and self.password.text is "":
            check_string = 'please enter a password'
        else:
            check_string='credentials are incorrect'
       # if self.password.text is "":
        #    check_string='please enter your password'
        #else:
         #   check_string='incorrect password'


        close_button=MDFlatButton(text='Close',on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog=MDDialog(title='login check',text=check_string,size_hint=(0.6,1),buttons=[close_button,more_button])
        self.dialog.open()

        print(self.username.text)
        print(self.password.text)

    def close_dialog(self,obj):
        self.dialog.dismiss()

       # label = MDLabel(text='hello user',halign='center',theme_text_color='Custom',
        #                text_color=(0.62,0.65,0.89,1),font_style='H2')
        #return label




        #icon_label=MDIcon(icon='language-python',halign='center')
        #return icon_label



HealthApp().run()
