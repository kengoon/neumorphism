from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

Builder.load_file("neuwidget/neuwidget.kv")

__all__ = ("NeuWidget",)

class NeuWidget(MDBoxLayout):
    ...