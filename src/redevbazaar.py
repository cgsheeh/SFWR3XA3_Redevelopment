import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText

class WelcomeScreen(BaseWidget):
	def __init__(self):
		super(WelcomeScreen, self).__init__("TEST1")
		self.testText = ControlText("WHERE IS THIS") 	
		
		
if __name__ == "__main__":
	pyforms.startApp(WelcomeScreen)