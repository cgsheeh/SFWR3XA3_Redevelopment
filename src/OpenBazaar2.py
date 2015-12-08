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

        ##
        # If the '--load-demo' argument was passed on the command line, load demo data
        try:
            if sys.argv[1] == '--load-demo':
                demo_data = DemoData()
                notary_data = demo_data.get_notary_data()
                merchant_data = demo_data.get_merchant_data()

                for merchant in merchant_data:
                    self.id_module.new_merchant(merchant)

                for notary in notary_data:
                    self.id_module.new_notary(notary)
        except IndexError:
            pass

        ##
        # This would have been where we create the node module.
        #self.node = pickle.load(open(Node.OBNodeStrings.obnode_pickle, 'rb'))
        #self.node.start_node(12345)

        ##
        # Do initial draw of GUI. Can call this function to redraw at any time
        #
        self.redraw()

        ##
        # Set current tab to Welcome screen
        self.tabMenu.setCurrentIndex(0)

        self.show()

    ##
    # Redraw command to be called
    def redraw(self):
        try:
            tab_index = self.tabMenu.currentIndex()
        except AttributeError:
            tab_index = 0
        settings = self.id_module.get_settings()



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
            item.setData(QtCore.Qt.UserRole, notary)
            self.myNotariesList.addItem(item)
        self.myNotariesList.itemClicked.connect(self.notary_clicked)
        self.gridLayout.addWidget(self.myNotariesList, 7, 4, 1, 3)

        ##
        # Add main tab menu
        #
        self.tabMenu = QtGui.QTabWidget(self.centralwidget)
        self.tabMenu.setObjectName(_fromUtf8("tabMenu"))
        self.tabMenu.setTabsClosable(True)
        self.tabMenu.tabCloseRequested.connect(self.close_clicked_tab)

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
            item.setData(QtCore.Qt.UserRole, merchant)
            self.merchantsList.addItem(item)
        self.merchantsList.itemClicked.connect(self.merchant_clicked)


        ##
        # Add recent transactions table and label
        #
        self.recentTransactionsTable = QtGui.QTableWidget(self.centralwidget)
        self.recentTransactionsTable.setObjectName(_fromUtf8("recentTransactionsTable"))
        self.recentTransactionsTable.setColumnCount(2)
        item = QtGui.QTableWidgetItem()
        item.setText("Name")
        self.recentTransactionsTable.setHorizontalHeaderItem(0, item)

        item = QtGui.QTableWidgetItem()
        item.setText("Seller")
        self.recentTransactionsTable.setHorizontalHeaderItem(1, item)

        for count, contract in enumerate(self.id_module.settings.contracts.getOnGoingContracts()):
            self.recentTransactionsTable.setRowCount(count + 1)
            item = QtGui.QTableWidgetItem()
            item.setText(contract.get_itemname())
            item.setData(QtCore.Qt.UserRole, contract)
            self.recentTransactionsTable.setItem(count, 0, item)

            item = QtGui.QTableWidgetItem()
            item.setText(contract.get_sellername())
            item.setData(QtCore.Qt.UserRole, contract)
            self.recentTransactionsTable.setItem(count, 1, item)

        self.recentTransactionsTable.itemClicked.connect(self.display_contract)

        self.gridLayout.addWidget(self.recentTransactionsTable, 7, 0, 1, 2)
        self.recentTransactionsLabel = QtGui.QLabel(self.centralwidget)
        self.recentTransactionsLabel.setObjectName(_fromUtf8("recentTransactionsLabel"))
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
        # Set tab menu index.
        self.tabMenu.setCurrentIndex(tab_index)

    ##
    # Action to be taken on tab close
    #     @param index: index of tab to close
    def close_clicked_tab(self, index):
        widget = self.tabMenu.widget(index)
        if widget is not None:
            widget.deleteLater()

        self.tabMenu.removeTab(index)

    ##
    # Add a new tab
    def add_tab(self, tab, name):
        self.tabMenu.addTab(tab, name)

    ##
    # Display the store view for this store
    def merchant_clicked(self, item):
        data_obj = item.data(QtCore.Qt.UserRole).toPyObject()
        merchant_scroll = QtGui.QScrollArea()
        merchant_view = storeTab2(data_obj)
        merchant_scroll.setWidget(merchant_view)
        self.add_tab(merchant_scroll, data_obj.get_name())
        #self.redraw()

    ##
    # Displays the contract in the recent transactions sidebar
    def display_contract(self, item):
        contract = item.data(QtCore.Qt.UserRole).toPyObject()
        contract_scroll = QtGui.QScrollArea()
        contract_view = contractView_Tab(contract)
        contract_scroll.setWidget(contract_view)
        self.tabMenu.addTab(contract_scroll, contract.get_itemname())

    ##
    # Display the notary view for this notary
    def notary_clicked(self, item):
        data_obj = item.data(QtCore.Qt.UserRole).toPyObject()
        notary_scroll = QtGui.QScrollArea()
        notary_view = notaryViewTab(data_obj)
        notary_scroll.setWidget(notary_view)
        self.add_Tab(notary_scroll, data_obj.get()['name'])
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
