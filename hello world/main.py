
# pip install -r requirements.txt

'''
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='My Name is Vicks.')

TestApp().run()
'''

import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')

class MyFirstKivyApp(App):
    def build(self):
        return Label(text="Hello World !")

MyFirstKivyApp().run()
