from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class InputLayout(BoxLayout):
    user_input = StringProperty()

    def submit_input(self):
        self.ids.output_label.text = self.user_input

class MyApp(App):
    def build(self):
        return InputLayout()

if __name__ == '__main__':
    MyApp().run()
