from re import MULTILINE
from typing import Sized
import kivy
from kivy import utils
from kivy.core import text
from kivy.uix.textinput import TextInput
from forex_python.converter import CurrencyRates



kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button




class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        c = CurrencyRates()
        self.pln = c.get_rate('PLN', 'BGN')
        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text=f"{self.pln}"))
        self.top_grid.add_widget(Label(text='PLN'))
        self.bgn = TextInput(font_size= 20)
        self.top_grid.add_widget(self.bgn)
        self.top_grid.add_widget(Label(text='BGN'))

        self.add_widget(self.top_grid)
        
        self.submit = Button(text='Submit', font_size=32, size_hint_y = None, height = 50, background_color = (255,255,255, 1), color='black')
        self.submit.bind(on_press=self.calculate)
        self.add_widget(self.submit)
        
    
    def calculate(self, instance):
        result = float(self.pln) * float(self.bgn.text)
        
        self.add_widget(Label(text=f"Sum is {result:.2f}"))

        
        self.bgn.text = ''


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()