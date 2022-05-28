
# Program to Show how to use textinput (UX widget) in kivy

# import kivy module	
import kivy
	
# base Class of your App inherits from the App class.	
# app:always refers to the instance of your application
from kivy.app import App
	
# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')
	
# The Label widget is for rendering text.
from kivy.uix.label import Label
	
# module consist the floatlayout
# to work with FloatLayout first
# you have to import it
from kivy.uix.floatlayout import FloatLayout

# Scatter is used to build interactive
# widgets that can be translated,
# rotated and scaled with two or more
# fingers on a multitouch system.
from kivy.uix.scatter import Scatter

# The TextInput widget provides a
# box for editable plain text
from kivy.uix.textinput import TextInput

# BoxLayout arranges widgets in either
# in vertical fashion that
# is one on top of another or in
# horizontal fashion that is one after another.
from kivy.uix.boxlayout import BoxLayout

# Create the App class
class TutorialApp(App):
	
	def build(self):

		b = BoxLayout(orientation ='vertical')

		# Adding the text input
		t = TextInput(font_size = 50,
					size_hint_y = None,
					height = 100)
		
		f = FloatLayout()

		# By this you are able to move the
		# Text on the screen to anywhere you want
		s = Scatter()

		l = Label(text ="Hello !",
				font_size = 50)

		f.add_widget(s)
		s.add_widget(l)

		b.add_widget(t)
		b.add_widget(f)

		# Binding it with the label
		t.bind(text = l.setter('text'))

		
		return b

# Run the App
if __name__ == "__main__":
	TutorialApp().run()
