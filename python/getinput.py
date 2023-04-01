import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.image import Image

class GetInput(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 3


        self.img = Image(
            source= "profile.jpg"
        )
        self.add_widget(self.img)


        self.lbl1 =Label(
            text ="Enter your 1st Name"
        )
        self.add_widget(self.lbl1)
        
        self.fld1 =TextInput(
            text ="first name"
        )
        self.add_widget(self.fld1)

        self.lbl2 =Label(
            text ="Enter your 2nd Name"
        )
        self.add_widget(self.lbl2)

        self.fld2 =TextInput(
            text ="second name"
        )
        self.add_widget(self.fld2)
        
        self.btn1 =Button(
            text ="Submit"
        )
        self.btn1.bind(on_press = self.btnFun)
        self.add_widget(self.btn1)


        self.pop = Popup(
            title = 'Poped Up ',
            size = (400,400),
            content = Label(
                text = ""
            )
        )

    def btnFun(self, elem):
        print("First name:" + self.fld1.text )
        print("Last name:" + self.fld2.text )
        # self.fld2 =Label(
        #     text =self.fld1.text + '\n' + self.fld2.text,
        # )
        self.pop.content.text = self.fld1.text + '\n' + self.fld2.text
        self.pop.open()





class mainApp(App):
    def build(self):
        return GetInput()


mainApp().run()
