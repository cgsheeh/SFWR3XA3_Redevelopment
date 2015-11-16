# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenBazaar.ui'
#
# Created: Fri Nov 13 14:25:15 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from TabWidgets import *
from PyQt4 import QtCore, QtGui

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


class Ui_OpenBazaar(object):

    def setupUi(self, OpenBazaar):

        ##
        # Set object name and initial size
        #
        OpenBazaar.setObjectName(_fromUtf8("OpenBazaar"))
        OpenBazaar.resize(1163, 867)

        ##
        # Set tray logo
        #
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/small_logo.jpeg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OpenBazaar.setWindowIcon(icon)

        ##
        # Create center widget, main grid layout
        #
        self.centralwidget = QtGui.QWidget(OpenBazaar)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))


        ##
        # Add currency conversion options
        #
        self.currencySelector = QtGui.QComboBox(self.centralwidget)
        self.currencySelector.setObjectName(_fromUtf8("currencySelector"))
        self.currencySelector.addItem(_fromUtf8(""))
        self.currencySelector.addItem(_fromUtf8(""))
        self.currencySelector.addItem(_fromUtf8(""))
        self.currencySelector.addItem(_fromUtf8(""))
        self.currencySelector.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.currencySelector, 2, 1, 1, 1)

        ##
        # Add display picture for user
        #
        self.displayPicture = QtGui.QLabel(self.centralwidget)
        self.displayPicture.setText(_fromUtf8(""))
        self.displayPicture.setPixmap(QtGui.QPixmap(_fromUtf8("images/default-avatar.png")))
        self.displayPicture.setObjectName(_fromUtf8("displayPicture"))
        self.gridLayout.addWidget(self.displayPicture, 0, 0, 2, 2)

        ##
        # Add merchant label
        #
        self.myMerchantsLabel = QtGui.QLabel(self.centralwidget)
        self.myMerchantsLabel.setObjectName(_fromUtf8("myMerchantsLabel"))
        self.gridLayout.addWidget(self.myMerchantsLabel, 0, 5, 1, 2)

        ##
        # Add "add store" button
        #
        self.addStoreButton = QtGui.QPushButton(self.centralwidget)
        self.addStoreButton.setObjectName(_fromUtf8("addStoreButton"))
        self.gridLayout.addWidget(self.addStoreButton, 5, 6, 1, 1)

        ##
        # Add "My Notaries" label
        self.myNotariesLabel = QtGui.QLabel(self.centralwidget)
        self.myNotariesLabel.setObjectName(_fromUtf8("myNotariesLabel"))
        self.gridLayout.addWidget(self.myNotariesLabel, 6, 5, 1, 2)

        ##
        # Add "My Notary" line edit
        #
        self.addNotaryText = QtGui.QLineEdit(self.centralwidget)
        self.addNotaryText.setObjectName(_fromUtf8("addNotaryText"))
        self.gridLayout.addWidget(self.addNotaryText, 8, 4, 1, 2)
        self.addNotaryButton = QtGui.QPushButton(self.centralwidget)
        self.addNotaryButton.setObjectName(_fromUtf8("addNotaryButton"))
        self.gridLayout.addWidget(self.addNotaryButton, 8, 6, 1, 1)

        ##
        # Add balance label
        self.bitcoin_balance_label = QtGui.QLabel(self.centralwidget)
        self.bitcoin_balance_label.setObjectName(_fromUtf8("bitcoin_balance_label"))
        self.gridLayout.addWidget(self.bitcoin_balance_label, 2, 0, 1, 1)

        ##
        # Add 'add store' text
        #
        self.addStoreText = QtGui.QLineEdit(self.centralwidget)
        self.addStoreText.setObjectName(_fromUtf8("addStoreText"))
        self.gridLayout.addWidget(self.addStoreText, 5, 4, 1, 2)

        ##
        # Add list of notaries and fill with 3 empty entries
        self.myNotariesList = QtGui.QListWidget(self.centralwidget)
        self.myNotariesList.setObjectName(_fromUtf8("myNotariesList"))
        item = QtGui.QListWidgetItem()
        self.myNotariesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.myNotariesList.addItem(item)
        item = QtGui.QListWidgetItem()
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
        self.tabMenu.addTab(self.tab, _fromUtf8("Welcome"))



        self.gridLayout.addWidget(self.tabMenu, 7, 2, 1, 1)
        self.merchantsList = QtGui.QListWidget(self.centralwidget)
        self.merchantsList.setObjectName(_fromUtf8("merchantsList"))
        item = QtGui.QListWidgetItem()
        self.merchantsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.merchantsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.merchantsList.addItem(item)
        self.gridLayout.addWidget(self.merchantsList, 1, 4, 4, 3)
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
        self.gridLayout.addWidget(self.recentTransactionsLabel, 6, 0, 1, 1)
        self.main_logo_label = QtGui.QLabel(self.centralwidget)
        self.main_logo_label.setText(_fromUtf8(""))
        self.main_logo_label.setPixmap(QtGui.QPixmap(_fromUtf8("images/banner.png")))
        self.main_logo_label.setObjectName(_fromUtf8("main_logo_label"))
        self.gridLayout.addWidget(self.main_logo_label, 0, 2, 2, 1)
        self.searchBarText = QtGui.QLineEdit(self.centralwidget)
        self.searchBarText.setObjectName(_fromUtf8("searchBarText"))
        self.gridLayout.addWidget(self.searchBarText, 4, 2, 1, 1)
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout.addWidget(self.searchButton, 4, 3, 1, 1)

        ##
        # Create "New Contract" Tab
        #
        self.newContractTab_scroll = QtGui.QScrollArea()
        self.newContractTab = QtGui.QWidget()
        self.newContractUi = ContractGenUi()
        self.newContractUi.setupUi(self.newContractTab)
        self.newContractTab_scroll.setWidget(self.newContractTab)
        self.tabMenu.addTab(self.newContractTab_scroll, "New Contract")

        ##
        # Create a blank store tab
        #
        self.exampleStoreTab = QtGui.QWidget()
        self.exampleStoreUi = storeTab()
        self.exampleStoreUi.setupUi(self.exampleStoreTab)
        self.tabMenu.addTab(self.exampleStoreTab, "Someone's Store")

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
        self.new_message_tab = QtGui.QWidget()
        self.new_message_ui = SendMessage_Ui()
        self.new_message_ui.setupUi(self.new_message_tab)
        self.new_message_scroll.setWidget(self.new_message_tab)
        self.tabMenu.addTab(self.new_message_scroll, "Send Message")

        ##
        # Create settings tab
        #
        self.settings_scroll = QtGui.QScrollArea()
        self.settings_tab = QtGui.QWidget()
        self.settings_tab_ui = Settings_Ui()
        self.settings_tab_ui.setupUi(self.settings_tab)
        self.settings_scroll.setWidget(self.settings_tab)
        self.tabMenu.addTab(self.settings_scroll, "Settings")

        ##
        # Set grid layout as central widget
        #
        OpenBazaar.setCentralWidget(self.centralwidget)

        ##
        # Create menu bar for application
        #
        self.menubar = QtGui.QMenuBar(OpenBazaar)
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
        OpenBazaar.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(OpenBazaar)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        OpenBazaar.setStatusBar(self.statusbar)

        ##
        # Define action for clicking menu bar items
        #
        self.actionMy_Listings = QtGui.QAction(OpenBazaar)
        self.actionMy_Listings.setObjectName(_fromUtf8("actionMy_Listings"))
        self.actionMy_Orders = QtGui.QAction(OpenBazaar)
        self.actionMy_Orders.setObjectName(_fromUtf8("actionMy_Orders"))
        self.actionMy_Orders.triggered.connect(lambda x: self.tabMenu.setCurrentIndex(self.tabMenu.indexOf(self.orders_tab)))
        self.actionMy_Settings = QtGui.QAction(OpenBazaar)
        self.actionMy_Settings.setObjectName(_fromUtf8("actionMy_Settings"))
        self.actionMy_Settings.triggered.connect(lambda x: self.tabMenu.setCurrentIndex(self.tabMenu.indexOf(self.settings_scroll)))
        self.actionSend_a_Message = QtGui.QAction(OpenBazaar)
        self.actionSend_a_Message.setObjectName(_fromUtf8("actionSend_a_Message"))
        self.actionSend_a_Message.triggered.connect(lambda x: self.tabMenu.setCurrentIndex(self.tabMenu.indexOf(self.new_message_tab)))
        self.actionInbo = QtGui.QAction(OpenBazaar)
        self.actionInbo.setObjectName(_fromUtf8("actionInbo"))
        self.actionOutbox = QtGui.QAction(OpenBazaar)
        self.actionOutbox.setObjectName(_fromUtf8("actionOutbox"))
        self.actionOutbox.triggered.connect(lambda x: self.tabMenu.setCurrentIndex(self.tabMenu.indexOf(self.new_message_tab)))
        self.actionPurchased = QtGui.QAction(OpenBazaar)
        self.actionPurchased.setObjectName(_fromUtf8("actionPurchased"))
        self.actionNewContract = QtGui.QAction(OpenBazaar)
        self.actionNewContract.setObjectName(_fromUtf8("actionNewContract"))
        self.actionNewContract.triggered.connect(lambda x: self.tabMenu.setCurrentIndex(self.tabMenu.indexOf(self.newContractTab)))
        self.actionSold = QtGui.QAction(OpenBazaar)
        self.actionSold.setObjectName(_fromUtf8("actionSold"))
        self.actionActive = QtGui.QAction(OpenBazaar)
        self.actionActive.setObjectName(_fromUtf8("actionActive"))
        self.actionCreate_a_Store = QtGui.QAction(OpenBazaar)
        self.actionCreate_a_Store.setObjectName(_fromUtf8("actionCreate_a_Store"))
        self.actionView_a_Store = QtGui.QAction(OpenBazaar)
        self.actionView_a_Store.setObjectName(_fromUtf8("actionView_a_Store"))
        self.actionFind = QtGui.QAction(OpenBazaar)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionBecome_a_Notary = QtGui.QAction(OpenBazaar)
        self.actionBecome_a_Notary.setObjectName(_fromUtf8("actionBecome_a_Notary"))
        self.actionFind_a_Notary = QtGui.QAction(OpenBazaar)
        self.actionFind_a_Notary.setObjectName(_fromUtf8("actionFind_a_Notary"))
        self.actionHelp_with_Notaries = QtGui.QAction(OpenBazaar)
        self.actionHelp_with_Notaries.setObjectName(_fromUtf8("actionHelp_with_Notaries"))
        self.actionGet_Help_Online = QtGui.QAction(OpenBazaar)
        self.actionGet_Help_Online.setObjectName(_fromUtf8("actionGet_Help_Online"))
        self.actionUser_Guide = QtGui.QAction(OpenBazaar)
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

        self.retranslateUi(OpenBazaar)
        self.tabMenu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OpenBazaar)

    def retranslateUi(self, OpenBazaar):
        OpenBazaar.setWindowTitle(_translate("OpenBazaar", "OpenBazaar", None))
        self.currencySelector.setItemText(0, _translate("OpenBazaar", "CAD", None))
        self.currencySelector.setItemText(1, _translate("OpenBazaar", "MBTC", None))
        self.currencySelector.setItemText(2, _translate("OpenBazaar", "BTC", None))
        self.currencySelector.setItemText(3, _translate("OpenBazaar", "USD", None))
        self.currencySelector.setItemText(4, _translate("OpenBazaar", "EUR", None))
        self.myMerchantsLabel.setText(_translate("OpenBazaar", "My Merchants", None))
        self.addStoreButton.setText(_translate("OpenBazaar", "Add Store", None))
        self.myNotariesLabel.setText(_translate("OpenBazaar", "My Notaries", None))
        self.addNotaryText.setText(_translate("OpenBazaar", "Enter Notary GUID", None))
        self.addNotaryButton.setText(_translate("OpenBazaar", "Add Notary", None))
        self.bitcoin_balance_label.setText(_translate("OpenBazaar", "$14,092", None))
        self.addStoreText.setText(_translate("OpenBazaar", "Enter Store GUID", None))
        __sortingEnabled = self.myNotariesList.isSortingEnabled()
        self.myNotariesList.setSortingEnabled(False)
        item = self.myNotariesList.item(0)
        item.setText(_translate("OpenBazaar", "Notary 1", None))
        item = self.myNotariesList.item(1)
        item.setText(_translate("OpenBazaar", "Notary 2", None))
        item = self.myNotariesList.item(2)
        item.setText(_translate("OpenBazaar", "Notary 3", None))
        self.myNotariesList.setSortingEnabled(__sortingEnabled)
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

        __sortingEnabled = self.merchantsList.isSortingEnabled()
        self.merchantsList.setSortingEnabled(False)
        item = self.merchantsList.item(0)
        item.setText(_translate("OpenBazaar", "Merchant 1", None))
        item = self.merchantsList.item(1)
        item.setText(_translate("OpenBazaar", "Merchant 2", None))
        item = self.merchantsList.item(2)
        item.setText(_translate("OpenBazaar", "Merchant 3", None))
        self.merchantsList.setSortingEnabled(__sortingEnabled)
        item = self.recentTransactionsTable.verticalHeaderItem(0)
        item.setText(_translate("OpenBazaar", "Fake Transaction 1", None))
        item = self.recentTransactionsTable.verticalHeaderItem(1)
        item.setText(_translate("OpenBazaar", "Fake Transaction 2", None))
        item = self.recentTransactionsTable.horizontalHeaderItem(0)
        item.setText(_translate("OpenBazaar", "Date", None))
        item = self.recentTransactionsTable.horizontalHeaderItem(1)
        item.setText(_translate("OpenBazaar", "Price", None))
        self.recentTransactionsLabel.setText(_translate("OpenBazaar", "Recent Transactions", None))
        self.searchBarText.setText(_translate("OpenBazaar", "Search the OpenBazaar!", None))
        self.searchButton.setText(_translate("OpenBazaar", "Search", None))
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


    ##
    # Create a tab with the new contract menu
    #
    #def create_contract_tab(self):


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    OpenBazaar = QtGui.QMainWindow()
    ui = Ui_OpenBazaar()
    ui.setupUi(OpenBazaar)
    OpenBazaar.show()
    sys.exit(app.exec_())

