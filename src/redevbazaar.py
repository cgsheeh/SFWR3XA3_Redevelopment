import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText


class WelcomeScreen(BaseWidget):
    def __init__(self):
        super(WelcomeScreen, self).__init__("TEST1")
        self.testText = ControlText("some stuff")
        self.name = 'TestUsername'

        self.mainmenu = [
            {self.name: [
                {'My Listings': self.__getlistingsevent},
                {'My Orders': self.__getordersevent},
                {'Settings': self.__getsettingsevent}
            ]
            },

            {'Messages': [
                {'Compose': self.__getinboxevent},
                {'Inbox': self.__sendmessageevent},
                {'Sent': self.__getoutboxevent}
            ]
            },

            {
                'Contracts': [
                    {'Purchased': self.__purchasedcontractsevent},
                    {'Sold': self.__soldcontractsevent},
                    {'Active': self.__activecontractsevent}
                ]
            },

            {
                'Stores': [
                    {'Create new store': self.__createstoreevent},
                    {'View stores': self.__viewstoreevent},
                    {'Find stores': self.__searchstoreevent}
                ]
            },

            {
                'Notaries': [
                    {'Become a notary': self.__becomenotaryevent},
                    {'Find notaries': self.__findnotaryevent},
                    {'Notary help': self.__helpnotaryevent}
                ]
            },

            {'Search': [{'Search': self.__searchevent}]}
        ]

    def __getlistingsevent(self):
        print "hey"

    def __getordersevent(self):
        print "hey"

    def __getsettingsevent(self):
        print "hey"

    def __getinboxevent(self):
        print "hey"

    def __sendmessageevent(self):
        print "hey"

    def __getoutboxevent(self):
        print "hey"

    def __activecontractsevent(self):
        print "hey"

    def __soldcontractsevent(self):
        print "hey"

    def __purchasedcontractsevent(self):
        print "hey"

    def __createstoreevent(self):
        print "hey"

    def __viewstoreevent(self):
        print "view store"

    def __searchstoreevent(self):
        print "search store"

    def __becomenotaryevent(self):
        print "become a notary"

    def __findnotaryevent(self):
        print "find a notary"

    def __helpnotaryevent(self):
        print "help a notary"

    def __searchevent(self):
        print "Search event"


if __name__ == "__main__":
    pyforms.startApp(WelcomeScreen)
