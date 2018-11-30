from random import sample
from string import ascii_lowercase
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class LoginScreen(Screen):
    pass


class RegistrationScreen(Screen):
    pass


class DialogScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("messenger.kv")


class MainApp(App):
    def build(self):
        return presentation


MainApp().run()
