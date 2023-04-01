from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class float_layout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.b1 = Button(
            text = 'click me',
            size_hint = (.4, .4),
            pos_hint = {"x":0.3,"y":0.1},
            background_color = (0,24,67,1),
            color = (0,0,0,1)
        )
        self.add_widget(self.b1)
        self.b2 = Button(
            text = 'click me2',
            size_hint = (.4, .4),
            pos_hint = {"x":0.4,"y":0.3},
            background_color = (0,24,67,1),
            color = (0,0,0,1)
        )
        self.add_widget(self.b2)



class demoApp(App):
    def build(self):
        return float_layout()


demoApp().run()
