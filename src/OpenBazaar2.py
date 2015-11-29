# -*- coding: utf-8 -*-
import os
import pickle
import InitializationMod
from identity import Identity, ImageStorage
from node import Node
import sys
from PyQt4 import QtCore, QtGui
from TabWidgets import *
from DemoData import DemoData



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class OpenBazaar2(QtGui.QMainWindow):

    def __init__(self):
        super(OpenBazaar2, self).__init__()



        ##
        # Before doing anything check if a user has been initialized
        # by looking for the existence of an identity pickle file
        #
        if not Identity.Identity.is_init():
            InitializationMod.BazaarInit.initialize_Bazaar(12345)


        ##
        # Create data modules (ie Identity module)
        #
        self.id_module = Identity.Identity.get_id_mod()
        try:
            if sys.argv[1] == '--load-demo':
                demo_data = DemoData()
                notary_data = demo_data.get_notary_data()
                merchant_data = demo_data.get_merchant_data()

                for merchant in merchant_data:
                    print type(merchant)
                    self.id_module.new_merchant(merchant)

                for notary in notary_data:
                    self.id_module.new_notary(notary)
        except IndexError:
            pass

        ##
        # Do initial draw of GUI. Can call this function to redraw at any time
        #
        self.redraw()

        ##
        # Set current tab to Welcome screen
        self.tabMenu.setCurrentIndex(0)

        self.show()

    def redraw(self):
        try:
            tab_index = self.tabMenu.currentIndex()
        except AttributeError:
            tab_index = 0
        settings = self.id_module.get_settings()

        #self.node = pickle.load(open(Node.OBNodeStrings.obnode_pickle, 'rb'))
        #self.node.start_node(12345)

        ##
        # Set main object name
        #
        self.setObjectName("OpenBazaar")
        self.setWindowTitle('OpenBazaar')
        self.resize(1163, 867)

        ##
        # Set tray logo
        #
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(OBStrings.traylogo)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        ##
        # Create center widget, main grid layout
        #
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))



        ##
        # Add balance label
        #
        self.bitcoin_balance_label = QtGui.QLabel(self.centralwidget)
        self.bitcoin_balance_label.setObjectName(_fromUtf8("bitcoin_balance_label"))
        self.bitcoin_balance_label.setText(settings['nickname'])
        self.gridLayout.addWidget(self.bitcoin_balance_label, 2, 0, 1, 1)

        ##
        # Add display picture for user
        #
        self.displayPicture_p = QtGui.QIcon(settings['avatar'].get_repr().toqpixmap())
        self.displayPicture_b = QtGui.QPushButton(self.centralwidget)
        self.displayPicture_b.setFlat(True)
        self.displayPicture_b.setIcon(self.displayPicture_p)
        self.displayPicture_b.setGeometry(QtCore.QRect(100, 200, 300, 300))
        self.displayPicture_b.setIconSize(self.displayPicture_b.size())
        self.displayPicture_b.clicked.connect(self.set_picture)
        self.gridLayout.addWidget(self.displayPicture_b, 0, 0, 2, 2)

        ##
        # Add merchant label
        #
        self.myMerchantsLabel = QtGui.QLabel(self.centralwidget)
        self.myMerchantsLabel.setObjectName(_fromUtf8("myMerchantsLabel"))
        self.myMerchantsLabel.setText(_translate("OpenBazaar", "My Merchants", None))
        self.gridLayout.addWidget(self.myMerchantsLabel, 0, 5, 1, 2)

        ##
        # Add "add store" button
        #
        self.addStoreButton = QtGui.QPushButton(self.centralwidget)
        self.addStoreButton.setObjectName(_fromUtf8("addStoreButton"))
        self.addStoreButton.setText(_translate("OpenBazaar", "Add Store", None))
        self.gridLayout.addWidget(self.addStoreButton, 5, 6, 1, 1)

        ##
        # Add "My Notaries" label
        self.myNotariesLabel = QtGui.QLabel(self.centralwidget)
        self.myNotariesLabel.setObjectName(_fromUtf8("myNotariesLabel"))
        self.myNotariesLabel.setText(_translate("OpenBazaar", "My Notaries", None))
        self.gridLayout.addWidget(self.myNotariesLabel, 6, 5, 1, 2)

        ##
        # Add "My Notary" line edit
        #
        self.addNotaryText = QtGui.QLineEdit(self.centralwidget)
        self.addNotaryText.setObjectName(_fromUtf8("addNotaryText"))
        self.gridLayout.addWidget(self.addNotaryText, 8, 4, 1, 2)
        self.addNotaryButton = QtGui.QPushButton(self.centralwidget)
        self.addNotaryButton.setObjectName(_fromUtf8("addNotaryButton"))
        self.addNotaryText.setText(_translate("OpenBazaar", "Enter Notary GUID", None))
        self.addNotaryButton.setText(_translate("OpenBazaar", "Add Notary", None))
        self.gridLayout.addWidget(self.addNotaryButton, 8, 6, 1, 1)


        ##
        # Add 'add store' text
        #
        self.addStoreText = QtGui.QLineEdit(self.centralwidget)
        self.addStoreText.setObjectName(_fromUtf8("addStoreText"))
        self.addStoreText.setText(_translate("OpenBazaar", "Enter Store GUID", None))
        self.gridLayout.addWidget(self.addStoreText, 5, 4, 1, 2)

        ##
        # Add list of notaries and fill with data from notary module
        #
        self.myNotariesList = QtGui.QListWidget(self.centralwidget)
        self.myNotariesList.setObjectName(_fromUtf8("myNotariesList"))

        for count, notary in enumerate(settings['notaries']):
            notary_info = notary.get()
            item = QtGui.QListWidgetItem()
            item.setText(notary_info['name'])
            self.myNotariesList.addItem(item)
        self.gridLayout.addWidget(self.myNotariesList, 7, 4, 1, 3)

        ##
        # Add main tab menu
        #
        self.tabMenu = QtGui.QTabWidget(self.centralwidget)
        self.tabMenu.setObjectName(_fromUtf8("tabMenu"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))

        ##
        # Add welcome tab
        #
        self.welcome_tab_browser = QtGui.QTextBrowser(self.tab)
        self.welcome_tab_browser.setGeometry(QtCore.QRect(-5, 1, 611, 441))
        self.welcome_tab_browser.setObjectName(_fromUtf8("welcome_tab_browser"))
        self.welcome_tab_browser.setHtml(_translate("OpenBazaar", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:20px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:x-large; font-weight:496; color:#666666;\">Getting started</span></p>\n"
"<p style=\" margin-top:20px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:large; font-weight:496; color:#666666;\">Set Up Your Store</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\">Add a Bitcoin address you own in case of refunds, be sure to hit save in </span><span style=\" font-family:\'arial\'; font-size:14px; font-weight:696; color:#666666;\">Settings</span><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\">, and make a backup of your keys in the </span><span style=\" font-family:\'arial\'; font-size:14px; font-weight:696; color:#666666;\">Backup</span><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\"> section.</span></p>\n"
"<p style=\" margin-top:20px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:large; font-weight:496; color:#666666;\">Select a Notary</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\">Notaries are a trusted third party to prevent scams. Only select a notary you trust, especially for larger transactions. For test transactions, you can use the &quot;Test Notary.&quot;</span></p>\n"
"<p style=\" margin-top:20px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:large; font-weight:496; color:#666666;\">Put an Item Up for Sale or Find an Item to Buy</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\">If selling an item, be sure to use descriptive keywords. Click on the markets you see on the right side of the screen to view their items, or use the search bar above. </span><span style=\" font-family:\'arial\'; font-size:14px; color:#666666;\"> </span><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\">You can directly contact other online users by selecting the blue Message Me button in their store front. Manage your messages in the </span><span style=\" font-family:\'arial\'; font-size:14px; font-weight:696; color:#666666;\">Messages</span><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\"> tab.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"http://i.imgur.com/jAtFHXV.gif\" style=\"vertical-align: middle;\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\">Your purchases and sales are in the </span><span style=\" font-family:\'arial\'; font-size:14px; font-weight:696; color:#666666;\">Orders</span><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\"> tab. </span><span style=\" font-family:\'arial\'; font-size:14px; color:#666666;\"> </span><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\">Please report problems to our </span><a href=\"https://github.com/OpenBazaar\"><span style=\" text-decoration: underline; color:#0000ff;\">Github</span></a><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\"> or </span><a href=\"https://www.reddit.com/r/OpenBazaar/\"><span style=\" text-decoration: underline; color:#0000ff;\">subreddit</span></a><span style=\" font-family:\'arial\'; font-size:14px; color:#666666; background-color:#ffffff;\">. Enjoy!</span></p></body></html>", None))
        self.tabMenu.addTab(self.tab, _fromUtf8("Welcome"))


        ##
        # Add tab menu to grid layout
        #
        self.gridLayout.addWidget(self.tabMenu, 7, 3, 1, 1)

        ##
        # Create merchants list widget
        #
        self.merchantsList = QtGui.QListWidget(self.centralwidget)
        self.merchantsList.setObjectName(_fromUtf8("merchantsList"))
        self.gridLayout.addWidget(self.merchantsList, 1, 4, 4, 3)

        ##
        # Fill merchants list with data from store module
        for count, merchant in enumerate(settings['myMerchants']):
            item = QtGui.QListWidgetItem()
            item.setText(merchant.get_name())
            self.merchantsList.addItem(item)



        ##
        # Add recent transactions table and label
        #
        self.recentTransactionsTable = QtGui.QTableWidget(self.centralwidget)
        self.recentTransactionsTable.setObjectName(_fromUtf8("recentTransactionsTable"))
        self.recentTransactionsTable.setColumnCount(2)
        self.recentTransactionsTable.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.recentTransactionsTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.recentTransactionsTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.recentTransactionsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.recentTransactionsTable.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.recentTransactionsTable, 7, 0, 1, 2)
        self.recentTransactionsLabel = QtGui.QLabel(self.centralwidget)
        self.recentTransactionsLabel.setObjectName(_fromUtf8("recentTransactionsLabel"))
        item = self.recentTransactionsTable.verticalHeaderItem(0)
        item.setText(_translate("OpenBazaar", "Fake Transaction 1", None))
        item = self.recentTransactionsTable.verticalHeaderItem(1)
        item.setText(_translate("OpenBazaar", "Fake Transaction 2", None))
        item = self.recentTransactionsTable.horizontalHeaderItem(0)
        item.setText(_translate("OpenBazaar", "Date", None))
        item = self.recentTransactionsTable.horizontalHeaderItem(1)
        item.setText(_translate("OpenBazaar", "Price", None))
        self.recentTransactionsLabel.setText(_translate("OpenBazaar", "Recent Transactions", None))
        self.gridLayout.addWidget(self.recentTransactionsLabel, 6, 0, 1, 1)

        ##
        # Add main logo to screen
        #
        self.main_logo_label = QtGui.QLabel(self.centralwidget)
        self.main_logo_label.setText(_fromUtf8(""))
        self.main_logo_label.setPixmap(QtGui.QPixmap(_fromUtf8(OBStrings.ob_banner)))
        self.main_logo_label.setObjectName(_fromUtf8("main_logo_label"))
        self.gridLayout.addWidget(self.main_logo_label, 0, 3, 2, 1)

        ##
        # Add search bar line and button
        #
        #spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        #self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        #spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        #self.gridLayout.addItem(spacerItem1, 7, 4, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchBarText = QtGui.QLineEdit(self.centralwidget)
        self.searchBarText.setObjectName(_fromUtf8("searchBarText"))
        self.horizontalLayout.addWidget(self.searchBarText)
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.searchButton.clicked.connect(self.search_clicked)
        self.searchButton.setText("Search")

        self.horizontalLayout.addWidget(self.searchButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 3, 1, 1)

        ##
        # Create "New Contract" Tab
        #
        self.newContractTab_scroll = QtGui.QScrollArea()
        self.newContractTab = ContractGenUi2()
        self.newContractTab_scroll.setWidget(self.newContractTab)
        self.tabMenu.addTab(self.newContractTab_scroll, "New Contract")

        ##
        # Create a blank store tab
        #
        self.my_store_scroll = QtGui.QScrollArea()
        self.myStoreTab = storeTab2(self.id_module.merchant_repr())
        self.my_store_scroll.setWidget(self.myStoreTab)
        self.tabMenu.addTab(self.my_store_scroll, "My Store")

        ##
        # Create a "My orders" tab
        #
        self.orders_tab = QtGui.QWidget()
        self.orders_tab_ui = Ui_OrdersMenu()
        self.orders_tab_ui.setupUi(self.orders_tab)
        self.tabMenu.addTab(self.orders_tab, "My Orders")

        ##
        # Create a new message tab
        #
        self.new_message_scroll = QtGui.QScrollArea()
        self.new_message_tab = SendMessage_Ui2()
        self.new_message_scroll.setWidget(self.new_message_tab)
        self.tabMenu.addTab(self.new_message_scroll, "Send Message")

        ##
        # Create settings tab
        #
        self.settings_scroll = QtGui.QScrollArea()
        self.settings_tab = Settings_Ui2(settings)
        self.settings_scroll.setWidget(self.settings_tab)
        self.tabMenu.addTab(self.settings_scroll, "Settings")

        ##
        # Create bootstrap tab
        #
        self.bootstrap_tab = bootStrap_Tab()
        self.tabMenu.addTab(self.bootstrap_tab, "Bootstrap")

        ##
        # Set central widget
        #
        self.setCentralWidget(self.centralwidget)

        ##
        # Create menu bar for application
        #
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHome = QtGui.QMenu(self.menubar)
        self.menuHome.setObjectName(_fromUtf8("menuHome"))
        self.menuMessages = QtGui.QMenu(self.menubar)
        self.menuMessages.setObjectName(_fromUtf8("menuMessages"))
        self.menuContracts = QtGui.QMenu(self.menubar)
        self.menuContracts.setObjectName(_fromUtf8("menuContracts"))
        self.menuStore = QtGui.QMenu(self.menubar)
        self.menuStore.setObjectName(_fromUtf8("menuStore"))
        self.menuNotaries = QtGui.QMenu(self.menubar)
        self.menuNotaries.setObjectName(_fromUtf8("menuNotaries"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        ##
        # Define action for clicking menu bar items
        #
        self.actionMy_Listings = QtGui.QAction(self)
        self.actionMy_Listings.setObjectName(_fromUtf8("actionMy_Listings"))
        self.actionMy_Orders = QtGui.QAction(self)
        self.actionMy_Orders.setObjectName(_fromUtf8("actionMy_Orders"))
        self.actionMy_Orders.triggered.connect(lambda x: self.tabMenu.setCurrentIndex(self.tabMenu.indexOf(self.orders_tab)))
        self.actionMy_Settings = QtGui.QAction(self)
        self.actionMy_Settings.setObjectName(_fromUtf8("actionMy_Settings"))
        self.actionMy_Settings.triggered.connect(lambda x: self.tabMenu.setCurrentIndex(self.tabMenu.indexOf(self.settings_scroll)))
        self.actionSend_a_Message = QtGui.QAction(self)
        self.actionSend_a_Message.setObjectName(_fromUtf8("actionSend_a_Message"))
        self.actionSend_a_Message.triggered.connect(lambda x: self.tabMenu.setCurrentIndex(self.tabMenu.indexOf(self.new_message_tab)))
        self.actionInbo = QtGui.QAction(self)
        self.actionInbo.setObjectName(_fromUtf8("actionInbo"))
        self.actionOutbox = QtGui.QAction(self)
        self.actionOutbox.setObjectName(_fromUtf8("actionOutbox"))
        self.actionOutbox.triggered.connect(lambda x: self.tabMenu.setCurrentIndex(self.tabMenu.indexOf(self.new_message_tab)))
        self.actionPurchased = QtGui.QAction(self)
        self.actionPurchased.setObjectName(_fromUtf8("actionPurchased"))
        self.actionNewContract = QtGui.QAction(self)
        self.actionNewContract.setObjectName(_fromUtf8("actionNewContract"))
        self.actionNewContract.triggered.connect(lambda x: self.tabMenu.setCurrentIndex(self.tabMenu.indexOf(self.newContractTab)))
        self.actionSold = QtGui.QAction(self)
        self.actionSold.setObjectName(_fromUtf8("actionSold"))
        self.actionActive = QtGui.QAction(self)
        self.actionActive.setObjectName(_fromUtf8("actionActive"))
        self.actionCreate_a_Store = QtGui.QAction(self)
        self.actionCreate_a_Store.setObjectName(_fromUtf8("actionCreate_a_Store"))
        self.actionView_a_Store = QtGui.QAction(self)
        self.actionView_a_Store.setObjectName(_fromUtf8("actionView_a_Store"))
        self.actionFind = QtGui.QAction(self)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionBecome_a_Notary = QtGui.QAction(self)
        self.actionBecome_a_Notary.setObjectName(_fromUtf8("actionBecome_a_Notary"))
        self.actionFind_a_Notary = QtGui.QAction(self)
        self.actionFind_a_Notary.setObjectName(_fromUtf8("actionFind_a_Notary"))
        self.actionHelp_with_Notaries = QtGui.QAction(self)
        self.actionHelp_with_Notaries.setObjectName(_fromUtf8("actionHelp_with_Notaries"))
        self.actionGet_Help_Online = QtGui.QAction(self)
        self.actionGet_Help_Online.setObjectName(_fromUtf8("actionGet_Help_Online"))
        self.actionUser_Guide = QtGui.QAction(self)
        self.actionUser_Guide.setObjectName(_fromUtf8("actionUser_Guide"))

        ##
        # Add actions to menu items
        #
        self.menuHome.addAction(self.actionMy_Listings)
        self.menuHome.addAction(self.actionMy_Orders)
        self.menuHome.addAction(self.actionMy_Settings)
        self.menuHome.addSeparator()
        self.menuMessages.addAction(self.actionSend_a_Message)
        self.menuMessages.addAction(self.actionInbo)
        self.menuMessages.addAction(self.actionOutbox)
        self.menuContracts.addAction(self.actionPurchased)
        self.menuContracts.addAction(self.actionNewContract)
        self.menuContracts.addAction(self.actionSold)
        self.menuContracts.addAction(self.actionActive)
        self.menuStore.addAction(self.actionCreate_a_Store)
        self.menuStore.addAction(self.actionView_a_Store)
        self.menuStore.addAction(self.actionFind)
        self.menuNotaries.addAction(self.actionBecome_a_Notary)
        self.menuNotaries.addAction(self.actionFind_a_Notary)
        self.menuNotaries.addAction(self.actionHelp_with_Notaries)
        self.menuHelp.addAction(self.actionGet_Help_Online)
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuMessages.menuAction())
        self.menubar.addAction(self.menuContracts.menuAction())
        self.menubar.addAction(self.menuStore.menuAction())
        self.menubar.addAction(self.menuNotaries.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        ##
        # Set menu option text
        #
        self.menuHome.setTitle(_translate("OpenBazaar", "Home", None))
        self.menuMessages.setTitle(_translate("OpenBazaar", "Messages", None))
        self.menuContracts.setTitle(_translate("OpenBazaar", "Contracts", None))
        self.menuStore.setTitle(_translate("OpenBazaar", "Stores", None))
        self.menuNotaries.setTitle(_translate("OpenBazaar", "Notaries", None))
        self.menuHelp.setTitle(_translate("OpenBazaar", "Help", None))
        self.actionMy_Listings.setText(_translate("OpenBazaar", "My Listings", None))
        self.actionMy_Orders.setText(_translate("OpenBazaar", "My Orders", None))
        self.actionMy_Settings.setText(_translate("OpenBazaar", "My Settings", None))
        self.actionSend_a_Message.setText(_translate("OpenBazaar", "Send a Message", None))
        self.actionInbo.setText(_translate("OpenBazaar", "Inbox", None))
        self.actionOutbox.setText(_translate("OpenBazaar", "Outbox", None))
        self.actionPurchased.setText(_translate("OpenBazaar", "Purchased", None))
        self.actionNewContract.setText(_translate("OpenBazaar", "New Contract", None))
        self.actionSold.setText(_translate("OpenBazaar", "Sold", None))
        self.actionActive.setText(_translate("OpenBazaar", "Active", None))
        self.actionCreate_a_Store.setText(_translate("OpenBazaar", "Create a Store", None))
        self.actionView_a_Store.setText(_translate("OpenBazaar", "View a Store", None))
        self.actionFind.setText(_translate("OpenBazaar", "Find a Store", None))
        self.actionBecome_a_Notary.setText(_translate("OpenBazaar", "Become a Notary", None))
        self.actionFind_a_Notary.setText(_translate("OpenBazaar", "Find a Notary", None))
        self.actionHelp_with_Notaries.setText(_translate("OpenBazaar", "Help with Notaries", None))
        self.actionGet_Help_Online.setText(_translate("OpenBazaar", "Get Help Online", None))
        self.actionUser_Guide.setText(_translate("OpenBazaar", "User Guide", None))

        self.tabMenu.setCurrentIndex(tab_index)

    ##
    # Describes what to do when the picture button is clicked
    def set_picture(self):
        ##
        # Open a dialog and get the location of the avatar.
        # Get settings before change
        avatar_path = QtGui.QFileDialog.getOpenFileName(self, 'Upload Avatar', '', '')
        avatar_image_storage = ImageStorage.ImageStorage(str(avatar_path))
        sett = self.id_module.get_settings()

        try:
            ##
            # Try and set the display picture to the specified location
            # If string is empty, set the avatar to the default
            if not avatar_path:
                pass
            else:
                av_image = avatar_image_storage.get_repr()
                self.displayPicture_p = QtGui.QIcon(av_image.toqpixmap())
                self.displayPicture_b.setIcon(self.displayPicture_p)


                ##
                # Set user settings to the new avatar location
                sett['avatar'] = avatar_image_storage
                self.id_module.set_settings(sett)

                ##
                # Redraw store view
                self.myStoreTab = storeTab2(self.id_module.merchant_repr())
                self.my_store_scroll.setWidget(self.myStoreTab)
        except Exception as e:
            ##
            # Catch some exceptions that could occur (not pixmap compatible, etc)
            print e.message

    ##
    # Defines action to be taken when search button is clicked
    def search_clicked(self):
        # Get the text in the search bar and split into words
        search_text = str(self.searchBarText.text())
        keywords = search_text.split(' ')

        # Remove trailing punctuation that could hinder search results
        for count, word in enumerate(keywords):
            keywords[count] = str(word).rstrip('?:!.,;')

        ##
        # Compile list of search results. Draw widget and add to tab menu
        search_results = self.id_module.search(keywords)
        search_scroll = QtGui.QScrollArea()
        search_tab = SearchResultsWidget(search_text, search_results)
        search_scroll.setWidget(search_tab)
        self.tabMenu.addTab(search_scroll, "Search Results")


##
# Holds string values for the OpenBazaar2 class
class OBStrings(object):
    traylogo = "images/small_logo.jpeg"
    ob_banner = "images/banner.png"



if __name__ == "__main__":
    try:
        if sys.argv[1] == '--restart':
            os.remove('node/node.p')
            os.remove('identity/id_safe')
            os.remove('identity/pubring.gpg')
            os.remove('identity/random_seed')
            os.remove('identity/secring.gpg')
            os.remove('identity/trustdb.gpg')
    except:
        pass
    app = QtGui.QApplication(sys.argv)
    OpenBazaar = OpenBazaar2()
    sys.exit(app.exec_())
