import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText

class WelcomeScreen(BaseWidget):
	def __init__(self):
		super(WelcomeScreen, self).__init__("TEST1")
		self.testText = ControlText("WHERE IS THIS") 	
		
		
		self.mainmenu = [
			{ 'Home': [
					{'My Listings': self.__getlistingsEvent},
					'-',
					{'My Orders': self.__getordersEvent},
					{'Settings': self.__getsettingsEvent}
				]
			},
			{ 'Messages': [
					{'Inbox': self.__getinboxEvent},
					{'Send a message': self.__sendmessageEvent},
					{'Sent Messages': self.__getoutboxEvent}
				]
			}
	    ]
		
	def __getlistingsEvent(self):
		print "hey"
		
	def __getordersEvent(self):
		print "hey"
		
	def __getsettingsEvent(self):
		print "hey"
		
	def __getinboxEvent(self):
		print "hey"
		
	def __sendmessageEvent(self):
		print "hey"
		
	def __getoutboxEvent(self):
		print "hey"
		
		
if __name__ == "__main__":
	pyforms.startApp(WelcomeScreen)