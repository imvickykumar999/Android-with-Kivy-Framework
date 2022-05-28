
'''
# import kivy module
import kivy

# this restricts the kivy version i.e
# below this kivy version you cannot use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# if you not import label and use it it through error
from kivy.uix.label import Label

# defining the App class
class MyLabelApp(App):
	def build(self):
		# label display the text on screen
		lbl = Label(text ="Label is Added on screen !!:):)")
		return lbl

# creating the object
label = MyLabelApp()
# run the window
label.run()
'''


from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

class Demo(MDApp):

	def build(self):
		#defining screen
		screen = Screen()

		#defining 1st label
		l=MDLabel(text="Welcome!",pos_hint={'center_x':0.8,
											'center_y':0.8},
				theme_text_color="Custom",
				text_color=(0.5,0,0.5,1),
				font_style='Caption')
		
		#defining 2nd label
		l1 = MDLabel(text="Welcome!", pos_hint={'center_x':0.8,
												'center_y':0.5},
					theme_text_color="Custom",
					text_color=(0.5, 0, 0.5, 1),
					font_style='H2')
		
		#defining 3rd label
		l2 = MDLabel(text="Welcome!", pos_hint={'center_x':0.8,
												'center_y':0.2},
					theme_text_color="Custom",
					text_color=(0.5, 0, 0.5, 1),
					font_style='H1')
		
		screen.add_widget(l)
		screen.add_widget(l1)
		screen.add_widget(l2)
		return screen

if __name__ == "__main__":
	Demo().run()
