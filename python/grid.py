from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button  import Button
from kivy.uix.label import Label


class Grid_layout_Demo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 2


        self.l1 = Label(
            text ='enter your Firstname'
        )
        self.add_widget(self.l1)

        self.l2 = Label(
            text ='enter your Lastname',
            
        )
        self.add_widget(self.l2)

        self.b1 = Button(
            text ='click here',
            background_color = (0,24,67,1),
            color = (0,0,0,1)
        )
        self.add_widget(self.b1)



class demoApp(App):
    def build(self):
        return Grid_layout_Demo()




demoApp().run()        