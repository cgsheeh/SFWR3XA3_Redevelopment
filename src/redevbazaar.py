__author__ = 'the fair traders'

import sys
from PyQt4 import QtGui, QtCore


class BazaarMain(QtGui.QMainWindow):
    def __init__(self):
        super(BazaarMain, self).__init__()

        #  Create window, add title and window logo
        self.setWindowTitle("RedevBazaar")
        self.setWindowIcon(QtGui.QIcon('images/small_logo.jpeg'))

        self.statusBar()

        #  Set up main menu bars
        self.mainMenu = self.menuBar()
        self.homeMenu = self.mainMenu.addMenu('&Home')
        self.messagesMenu = self.mainMenu.addMenu('&Messages')
        self.contractMenu = self.mainMenu.addMenu('&Contract')
        self.storesMenu = self.mainMenu.addMenu('S&tores')
        self.notaryMenu = self.mainMenu.addMenu('&Notaries')

        #  Define home menu functionality
        listings = QtGui.QAction("My Listings", self)
        listings.triggered.connect(self.tempfxn)

        orders = QtGui.QAction("My Orders", self)
        orders.triggered.connect(self.tempfxn)

        settings = QtGui.QAction("My Settings", self)
        settings.triggered.connect(self.tempfxn)

        self.homeMenu.addAction(listings)
        self.homeMenu.addAction(orders)
        self.homeMenu.addAction(settings)

        #
        #  Define messages menu functionality
        #
        inbox = QtGui.QAction("Inbox", self)
        inbox.triggered.connect(self.tempfxn)

        send_message = QtGui.QAction("Send Message", self)
        send_message.triggered.connect(self.tempfxn)

        sent = QtGui.QAction("Sent Messages", self)
        sent.triggered.connect(self.tempfxn)

        self.messagesMenu.addAction(inbox)
        self.messagesMenu.addAction(send_message)
        self.messagesMenu.addAction(sent)

        ##
        #  Define Contracts menu functionality
        #
        purchased = QtGui.QAction("Purchased", self)
        purchased.triggered.connect(self.tempfxn)

        sold = QtGui.QAction("Sold", self)
        sold.triggered.connect(self.tempfxn)

        active = QtGui.QAction("Active", self)
        active.triggered.connect(self.tempfxn)

        self.contractMenu.addAction(purchased)
        self.contractMenu.addAction(sold)
        self.contractMenu.addAction(active)

        #  Define stores menu
        create = QtGui.QAction("Create", self)
        create.triggered.connect(self.tempfxn)

        view = QtGui.QAction("View", self)
        view.triggered.connect(self.tempfxn)

        find = QtGui.QAction("Find", self)
        find.triggered.connect(self.tempfxn)

        self.storesMenu.addAction(create)
        self.storesMenu.addAction(view)
        self.storesMenu.addAction(find)

        #   Define Notary menu
        #   Become, find, help
        become = QtGui.QAction("Become a notary", self)
        become.triggered.connect(self.tempfxn)

        notary_find = QtGui.QAction("Find a notary", self)
        notary_find.triggered.connect(self.tempfxn)

        notary_help = QtGui.QAction("Help with notaries", self)
        notary_help.triggered.connect(self.tempfxn)

        self.notaryMenu.addAction(become)
        self.notaryMenu.addAction(notary_find)
        self.notaryMenu.addAction(notary_help)

        self.show()

    def tempfxn(self):
        print "word"
        sys.exit()


app = QtGui.QApplication(sys.argv)
GUI = BazaarMain()
sys.exit(app.exec_())
