from kivymd.app import MDApp
from neuwidget import InsetNeuWidget
from kivy.core.window import Window


class App(MDApp):
    def build(self):
        Window.bind(clearcolor=lambda *_: setattr(Window, 'clearcolor', "#cccccc"))
        return InsetNeuWidget(
            size_hint=(None, None),
            size=(200, 200), 
            pos_hint={'center_x': .5,'center_y': .5}
        )
    

App().run()