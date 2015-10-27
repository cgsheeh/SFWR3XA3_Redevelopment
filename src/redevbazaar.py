import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText

class WelcomeScreen(BaseWidget):
	def __init__(self):
		super(WelcomeScreen, self).__init__("TEST1")
		self.testText = ControlText("some stuff") 	
		self.name = 'TestUsername'
		
		self.mainmenu = [
			{ self.name : [
					{'My Listings': self.__getlistingsEvent},
					{'My Orders': self.__getordersEvent},
					{'Settings': self.__getsettingsEvent}
				]
			},
			
			{ 'Messages': [
					{'Compose': self.__getinboxEvent},
					{'Inbox': self.__sendmessageEvent},
					{'Sent': self.__getoutboxEvent}
				]
			},
			
			{
				'Contracts' : [
					{'Purchased' : self.__purchasedcontractsEvent},
					{'Sold' : self.__soldcontractsEvent},
					{'Active': self.__activecontractsEvent}
				]
			},
			
			{
				'Stores' : [
					{'Create new store': self.__createstoreEvent},
					{'View stores' : self.__viewstoreEvent},
					{'Find stores' : self.__searchstoreEvent}
				]
			},
			
			{
				'Notaries' : [
					{'Become a notary' : self.__becomenotaryEvent},
					{'Find notaries': self.__findnotaryEvent},
					{'Notary help' : self.__helpnotaryEvent}
				]
			},
			
			{'Search' : [{'Search':self.__searchEvent}]}
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
		
	def __activecontractsEvent(self):
		print "hey"
		
	def __soldcontractsEvent(self):
		print "hey"
		
	def __purchasedcontractsEvent(self):
		print "hey"
		
	def __createstoreEvent(self):
		print "hey"
		
	def __viewstoreEvent(self):
		print "view store"
		
	def __searchstoreEvent(self):
		print "search store"
		
	def __becomenotaryEvent(self):
		print "become a notary"
		
	def __findnotaryEvent(self):
		print "find a notary"
		
	def __helpnotaryEvent(self):
		print "help a notary"
		
	def __searchEvent(self):
		print "Search event"
		
		
if __name__ == "__main__":
	pyforms.startApp(WelcomeScreen)