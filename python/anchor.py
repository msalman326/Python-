from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.button import Button


class demoApp(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x = 'left', anchor_y ='bottom'
        )
        btn1 = Button(
            text = 'anchor layout demo',
            size_hint = (.2,.2),
            background_color = (0.0,25.58,1.0),
            color = (0,0,0,1)
        )
        layout.add_widget(btn1)
        return layout

demoApp().run()