from random import sample
from string import ascii_lowercase
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class LoginScreen(Screen):

    def goToGeristrationScreen(self):
        pass


class RegistrationScreen(Screen):
    pass


class DialogScreen(Screen):
    pass


# class ScreenManagement(ScreenManager):
sm = ScreenManager()

sm.add_widget(Screen(name='LoginScreen'))
sm.add_widget(Screen(name='RegistrationScreen'))
sm.add_widget(Screen(name='DialogScreen'))

sm.current = 'LoginScreen'


Builder.load_file("messenger.kv")


class MainApp(App):
    def build(self):
        return sm


MainApp().run()
