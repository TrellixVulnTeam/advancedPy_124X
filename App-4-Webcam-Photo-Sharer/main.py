from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from filesharer import FileSharer

Builder.load_file("frontend.kv")


class CameraScree():
    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


class


class ImageScreen():
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
