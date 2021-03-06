# -*- coding: utf-8 -*-

#
# Created: Fri Nov 13 14:07:26 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import hashlib
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

##
# StoreTab2
#     This class is the GUI for a user's store.
class storeTab2(QtGui.QWidget):

    ##
    # Constructor
    #     Creates a users store for viewing.
    #     @param store: holds store data representation
    def __init__(self, merchant_representation):
        super(storeTab2, self).__init__()
        self.setObjectName(_fromUtf8("Form"))
        self.resize(1038, 686)
        self.label_11 = QtGui.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(540, 6, 231, 211))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(0, 460, 111, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))

        ##
        # Set up table of user contracts and headers
        self.contractTable = QtGui.QTableWidget(self)
        self.contractTable.setGeometry(QtCore.QRect(0, 480, 1031, 201))
        self.contractTable.setObjectName(_fromUtf8("contractTable"))
        self.contractTable.setColumnCount(4)

        item = QtGui.QTableWidgetItem()
        item.setText("Item Name")
        self.contractTable.setHorizontalHeaderItem(0, item)


        item = QtGui.QTableWidgetItem()
        item.setText("Price")
        self.contractTable.setHorizontalHeaderItem(1, item)

        item = QtGui.QTableWidgetItem()
        item.setText("Expiry")
        self.contractTable.setHorizontalHeaderItem(2, item)

        item = QtGui.QTableWidgetItem()
        item.setText("Description")
        self.contractTable.setHorizontalHeaderItem(3, item)
        self.contractTable.itemClicked.connect(self.contract_clicked)

        ##
        # Add listings to table of contracts
        for count, listing in enumerate(merchant_representation.get_listings()):
            trade_info = listing.get_module('trade')
            metadata = listing.get_module('metadata')
            ##
            # Set row label to contract hash
            self.contractTable.setRowCount(count + 1)
            item = QtGui.QTableWidgetItem()
            item.setText(str(listing.contract_hash()))
            item.setData(QtCore.Qt.UserRole, listing)
            self.contractTable.setVerticalHeaderItem(count, item)

            item = QtGui.QTableWidgetItem()
            item.setText(trade_info['name'])
            item.setData(QtCore.Qt.UserRole, listing)
            self.contractTable.setItem(count, 0, item)

            item = QtGui.QTableWidgetItem()
            item.setText(trade_info['price'])
            item.setData(QtCore.Qt.UserRole, listing)
            self.contractTable.setItem(count, 1, item)

            item = QtGui.QTableWidgetItem()
            item.setText(metadata['expiry'])
            item.setData(QtCore.Qt.UserRole, listing)
            self.contractTable.setItem(count, 2, item)

            item = QtGui.QTableWidgetItem()
            item.setText(trade_info['description'])
            item.setData(QtCore.Qt.UserRole, listing)
            self.contractTable.setItem(count, 3, item)

        self.gridLayoutWidget = QtGui.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 771, 406))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.publicKey = QtGui.QTextEdit(self.gridLayoutWidget)
        self.publicKey.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.publicKey.setObjectName(_fromUtf8("publicKey"))
        self.gridLayout.addWidget(self.publicKey, 3, 1, 1, 1)
        self.GUID = QtGui.QTextEdit(self.gridLayoutWidget)
        self.GUID.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.GUID.setObjectName(_fromUtf8("GUID"))
        self.gridLayout.addWidget(self.GUID, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.storeEmail = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.storeEmail.setFont(font)
        self.storeEmail.setText(_fromUtf8(""))
        self.storeEmail.setObjectName(_fromUtf8("storeEmail"))
        self.gridLayout.addWidget(self.storeEmail, 1, 1, 1, 1)
        self.storeName = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.storeName.setFont(font)
        self.storeName.setText(_fromUtf8(""))
        self.storeName.setObjectName(_fromUtf8("storeName"))
        self.gridLayout.addWidget(self.storeName, 0, 1, 1, 1)
        self.bitcoinReceivingAddress = QtGui.QTextEdit(self.gridLayoutWidget)
        self.bitcoinReceivingAddress.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.bitcoinReceivingAddress.setObjectName(_fromUtf8("bitcoinReceivingAddress"))
        self.gridLayout.addWidget(self.bitcoinReceivingAddress, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.storeDescription = QtGui.QTextEdit(self.gridLayoutWidget)
        self.storeDescription.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.storeDescription.setObjectName(_fromUtf8("storeDescription"))
        self.gridLayout.addWidget(self.storeDescription, 5, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.avatar_label = QtGui.QLabel(self)
        self.avatar_label.setGeometry(QtCore.QRect(800, 20, 221, 211))
        self.avatar_label.setText(_fromUtf8(""))
        self.avatar_label.setObjectName(_fromUtf8("label_8"))

        self.setWindowTitle(_translate("Form", "Form", None))
        self.label_12.setText(_translate("Form", "My Listings:", None))
        self.label.setText(_translate("Form", "User Name:", None))
        self.label_3.setText(_translate("Form", "GUID:", None))
        self.label_2.setText(_translate("Form", "User Email:", None))
        self.label_5.setText(_translate("Form", "Bitcoin Receiving Address:", None))
        self.label_6.setText(_translate("Form", "Store Description", None))
        self.label_4.setText(_translate("Form", "Public Key:", None))

        ##
        # Set values in this tab
        self.storeName.setText(merchant_representation.get_name())
        self.storeEmail.setText(merchant_representation.get_email())
        self.storeDescription.setText(merchant_representation.get_description())
        self.bitcoinReceivingAddress.setText(merchant_representation.get_bitcoin_address())
        self.GUID.setText(merchant_representation.get_guid())
        self.publicKey.setText(merchant_representation.get_key())

        self.avatar_label.setPixmap(merchant_representation.get_avatar().get_repr().toqpixmap())
        self.avatar_label.setScaledContents(True)

    ##
    # This method describes the action to be taken when a contract hash is clicked
    def contract_clicked(self, item):
        ##
        # Try to get contract data from item
        try:
            ric_repr = item.data(QtCore.Qt.UserRole).toPyObject()
        except:
            print 'exception'
            return
        scroll_area = QtGui.QScrollArea()
        scroll_area.setWidget(contractView_Tab(ric_repr))
        self.window().add_tab(scroll_area, ric_repr.get_itemname())



##
# Settings_Ui2
#     This class is the GUI for the settings tab
#     @param settings_dict: holds all the current user settings for drawing on the widget
class Settings_Ui2(QtGui.QWidget):
    def __init__(self, settings_dict):
        super(Settings_Ui2, self).__init__()

        self.setObjectName(_fromUtf8("Settings_Ui2"))
        self.resize(800, 1300)

        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 1201))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.email_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.email_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))
        self.gridLayout_5.addWidget(self.email_lineEdit, 1, 1, 1, 1)
        self.email_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setObjectName(_fromUtf8("email_label"))
        self.gridLayout_5.addWidget(self.email_label, 1, 0, 1, 1)
        self.communication_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.communication_label.setFont(font)
        self.communication_label.setObjectName(_fromUtf8("communication_label"))
        self.gridLayout_5.addWidget(self.communication_label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.bitcoin_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.bitcoin_lineEdit.setObjectName(_fromUtf8("bitcoin_lineEdit"))
        self.gridLayout.addWidget(self.bitcoin_lineEdit, 2, 1, 1, 1)
        self.store_desc_edit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.store_desc_edit.setObjectName(_fromUtf8("store_desc_edit"))
        self.gridLayout.addWidget(self.store_desc_edit, 3, 1, 1, 1)
        self.nickname_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nickname_label.setFont(font)
        self.nickname_label.setObjectName(_fromUtf8("nickname_label"))
        self.gridLayout.addWidget(self.nickname_label, 1, 0, 1, 1)
        self.nickname_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.gridLayout.addWidget(self.nickname_lineEdit, 1, 1, 1, 1)
        self.bitcoin_address_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bitcoin_address_label.setFont(font)
        self.bitcoin_address_label.setObjectName(_fromUtf8("bitcoin_address_label"))
        self.gridLayout.addWidget(self.bitcoin_address_label, 2, 0, 1, 1)
        self.store_details_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.store_details_label.setFont(font)
        self.store_details_label.setObjectName(_fromUtf8("store_details_label"))
        self.gridLayout.addWidget(self.store_details_label, 0, 0, 1, 1)
        self.store_desc_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.store_desc_label.setFont(font)
        self.store_desc_label.setObjectName(_fromUtf8("store_desc_label"))
        self.gridLayout.addWidget(self.store_desc_label, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.add_notary_label = QtGui.QPushButton(self.verticalLayoutWidget)
        self.add_notary_label.setObjectName(_fromUtf8("add_notary_label"))
        self.gridLayout_3.addWidget(self.add_notary_label, 4, 1, 1, 1)
        self.known_notaries_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.known_notaries_label.setObjectName(_fromUtf8("known_notaries_label"))
        self.gridLayout_3.addWidget(self.known_notaries_label, 3, 0, 1, 1)
        self.trusted_notaries_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.trusted_notaries_label.setFont(font)
        self.trusted_notaries_label.setObjectName(_fromUtf8("trusted_notaries_label"))
        self.gridLayout_3.addWidget(self.trusted_notaries_label, 1, 0, 1, 1)
        self.add_notary_line = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.add_notary_line.setObjectName(_fromUtf8("add_notary_line"))
        self.gridLayout_3.addWidget(self.add_notary_line, 4, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.bitcoin_pubkey_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bitcoin_pubkey_label.setFont(font)
        self.bitcoin_pubkey_label.setObjectName(_fromUtf8("bitcoin_pubkey_label"))
        self.gridLayout_4.addWidget(self.bitcoin_pubkey_label, 1, 0, 1, 1)
        self.keys_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.keys_label.setFont(font)
        self.keys_label.setObjectName(_fromUtf8("keys_label"))
        self.gridLayout_4.addWidget(self.keys_label, 0, 0, 1, 1)
        self.guid_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.guid_label.setFont(font)
        self.guid_label.setObjectName(_fromUtf8("guid_label"))
        self.gridLayout_4.addWidget(self.guid_label, 2, 0, 1, 1)
        self.gpg_pubkey_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gpg_pubkey_label.setFont(font)
        self.gpg_pubkey_label.setObjectName(_fromUtf8("gpg_pubkey_label"))
        self.gridLayout_4.addWidget(self.gpg_pubkey_label, 3, 0, 1, 1)
        self.guid_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.guid_lineEdit.setObjectName(_fromUtf8("guid_lineEdit"))
        self.gridLayout_4.addWidget(self.guid_lineEdit, 2, 1, 1, 1)
        self.pubkey_textedit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.pubkey_textedit.setObjectName(_fromUtf8("pubkey_textedit"))
        self.gridLayout_4.addWidget(self.pubkey_textedit, 3, 1, 1, 1)
        self.bitcoin_pubkey_textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.bitcoin_pubkey_textEdit.setObjectName(_fromUtf8("bitcoin_pubkey_textEdit"))
        self.gridLayout_4.addWidget(self.bitcoin_pubkey_textEdit, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.notary_details_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.notary_details_label.setFont(font)
        self.notary_details_label.setObjectName(_fromUtf8("notary_details_label"))
        self.gridLayout_2.addWidget(self.notary_details_label, 0, 0, 1, 1)
        self.notary_percent_about_label = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.notary_percent_about_label.setAutoFillBackground(False)
        self.notary_percent_about_label.setObjectName(_fromUtf8("notary_percent_about_label"))
        self.gridLayout_2.addWidget(self.notary_percent_about_label, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.No|QtGui.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.percent_comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.percent_comboBox.setObjectName(_fromUtf8("percent_comboBox"))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.percent_comboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.percent_comboBox, 3, 1, 1, 1)
        self.make_notary_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.make_notary_label.setFont(font)
        self.make_notary_label.setObjectName(_fromUtf8("make_notary_label"))
        self.gridLayout_2.addWidget(self.make_notary_label, 1, 0, 1, 1)
        self.percent_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.percent_label.setFont(font)
        self.percent_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.percent_label.setObjectName(_fromUtf8("percent_label"))
        self.gridLayout_2.addWidget(self.percent_label, 3, 0, 1, 1)
        self.service_description_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.service_description_label.setFont(font)
        self.service_description_label.setObjectName(_fromUtf8("service_description_label"))
        self.gridLayout_2.addWidget(self.service_description_label, 4, 0, 1, 1)
        self.notary_servicedesc_textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.notary_servicedesc_textEdit.setObjectName(_fromUtf8("notary_servicedesc_textEdit"))
        self.gridLayout_2.addWidget(self.notary_servicedesc_textEdit, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.shipping_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.shipping_label.setFont(font)
        self.shipping_label.setObjectName(_fromUtf8("shipping_label"))
        self.gridLayout_6.addWidget(self.shipping_label, 0, 0, 1, 1)
        self.city_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.city_label.setFont(font)
        self.city_label.setObjectName(_fromUtf8("city_label"))
        self.gridLayout_6.addWidget(self.city_label, 5, 0, 1, 1)
        self.recipient_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.recipient_label.setFont(font)
        self.recipient_label.setObjectName(_fromUtf8("recipient_label"))
        self.gridLayout_6.addWidget(self.recipient_label, 2, 0, 1, 1)
        self.recipient_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.recipient_lineEdit.setObjectName(_fromUtf8("recipient_lineEdit"))
        self.gridLayout_6.addWidget(self.recipient_lineEdit, 2, 1, 1, 1)
        self.province_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.province_label.setFont(font)
        self.province_label.setObjectName(_fromUtf8("province_label"))
        self.gridLayout_6.addWidget(self.province_label, 6, 0, 1, 1)
        self.zip_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zip_label.setFont(font)
        self.zip_label.setObjectName(_fromUtf8("zip_label"))
        self.gridLayout_6.addWidget(self.zip_label, 7, 0, 1, 1)
        self.street1_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.street1_label.setFont(font)
        self.street1_label.setObjectName(_fromUtf8("street1_label"))
        self.gridLayout_6.addWidget(self.street1_label, 3, 0, 1, 1)
        self.street2_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.street2_label.setFont(font)
        self.street2_label.setObjectName(_fromUtf8("street2_label"))
        self.gridLayout_6.addWidget(self.street2_label, 4, 0, 1, 1)
        self.country_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.country_label.setFont(font)
        self.country_label.setObjectName(_fromUtf8("country_label"))
        self.gridLayout_6.addWidget(self.country_label, 8, 0, 1, 1)
        self.street1_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.gridLayout_6.addWidget(self.street1_lineEdit, 3, 1, 1, 1)
        self.street2_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.street2_lineEdit.setObjectName(_fromUtf8("street2_lineEdit"))
        self.gridLayout_6.addWidget(self.street2_lineEdit, 4, 1, 1, 1)
        self.city_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.city_lineEdit.setObjectName(_fromUtf8("city_lineEdit"))
        self.gridLayout_6.addWidget(self.city_lineEdit, 5, 1, 1, 1)
        self.province_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.province_lineEdit.setObjectName(_fromUtf8("province_lineEdit"))
        self.gridLayout_6.addWidget(self.province_lineEdit, 6, 1, 1, 1)
        self.zip_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.zip_lineEdit.setObjectName(_fromUtf8("zip_lineEdit"))
        self.gridLayout_6.addWidget(self.zip_lineEdit, 7, 1, 1, 1)
        self.country_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.country_lineEdit.setObjectName(_fromUtf8("country_lineEdit"))
        self.gridLayout_6.addWidget(self.country_lineEdit, 8, 1, 1, 1)
        self.encryption_message = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.encryption_message.setObjectName(_fromUtf8("encryption_message"))
        self.gridLayout_6.addWidget(self.encryption_message, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.save_button = QtGui.QPushButton(self)
        self.save_button.setGeometry(QtCore.QRect(680, 1220, 98, 27))
        self.save_button.setObjectName(_fromUtf8("save_button"))

        self.setWindowTitle(_translate("Form", "Form", None))
        self.email_label.setText(_translate("Form", "Email", None))
        self.communication_label.setText(_translate("Form", "Communication Info", None))
        self.bitcoin_lineEdit.setText(_translate("Form", "Bitcoin address to send all incoming fees or refunds to", None))
        self.store_desc_edit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter a short description about your store</p></body></html>", None))
        self.nickname_label.setText(_translate("Form", "Nickname", None))
        self.bitcoin_address_label.setText(_translate("Form", "Bitcoin Receiving Address", None))
        self.store_details_label.setText(_translate("Form", "Store Details", None))
        self.store_desc_label.setText(_translate("Form", "Store Description", None))
        self.add_notary_label.setText(_translate("Form", "Add", None))
        self.known_notaries_label.setText(_translate("Form", "The addresses below are notaries used during transactions.", None))
        self.trusted_notaries_label.setText(_translate("Form", "Trusted Notaries", None))
        self.add_notary_line.setText(_translate("Form", "Enter a notary\'s OB guid", None))
        self.bitcoin_pubkey_label.setText(_translate("Form", "Bitcoin Public Key (Uncompressed)", None))
        self.keys_label.setText(_translate("Form", "OpenBazaar Keys", None))
        self.guid_label.setText(_translate("Form", "OpenBazaar GUID", None))
        self.gpg_pubkey_label.setText(_translate("Form", "PGP Public Key", None))
        self.notary_details_label.setText(_translate("Form", "Notary Details", None))
        self.notary_percent_about_label.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Fees</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If your services are needed during a dispute, a fee can be requested from the participants of the transaction you are involved with. What percentage of each transaction would you like to request for your services?</p></body></html>", None))
        self.percent_comboBox.setItemText(0, _translate("Form", "0", None))
        self.percent_comboBox.setItemText(1, _translate("Form", "1", None))
        self.percent_comboBox.setItemText(2, _translate("Form", "2", None))
        self.percent_comboBox.setItemText(3, _translate("Form", "3", None))
        self.percent_comboBox.setItemText(4, _translate("Form", "4", None))
        self.percent_comboBox.setItemText(5, _translate("Form", "5", None))
        self.percent_comboBox.setItemText(6, _translate("Form", "6", None))
        self.percent_comboBox.setItemText(7, _translate("Form", "7", None))
        self.percent_comboBox.setItemText(8, _translate("Form", "8", None))
        self.percent_comboBox.setItemText(9, _translate("Form", "9", None))
        self.percent_comboBox.setItemText(10, _translate("Form", "10", None))
        self.make_notary_label.setText(_translate("Form", "Make me a notary", None))
        self.percent_label.setText(_translate("Form", "%", None))
        self.service_description_label.setText(_translate("Form", "Description of your services", None))
        self.shipping_label.setText(_translate("Form", "Shipping Information", None))
        self.city_label.setText(_translate("Form", "City", None))
        self.recipient_label.setText(_translate("Form", "Recipient Name", None))
        self.recipient_lineEdit.setText(_translate("Form", "Name visible on your package", None))
        self.province_label.setText(_translate("Form", "Province/Region", None))
        self.zip_label.setText(_translate("Form", "Zip", None))
        self.street1_label.setText(_translate("Form", "Street 1", None))
        self.street2_label.setText(_translate("Form", "Street 2", None))
        self.country_label.setText(_translate("Form", "Country", None))
        self.encryption_message.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note: This information will be encrypted and only be sent to your seller when you have marked your order for payment.</p></body></html>""", None))
        self.save_button.setText(_translate("Form", "Save Changes", None))


        ##
        # Fill in existing user settings
        #
        self.email_lineEdit.setText(settings_dict['email'])
        self.nickname_lineEdit.setText(settings_dict['nickname'])
        self.bitcoin_lineEdit.setText(settings_dict['bitcoinReceivingAddress'])
        self.store_desc_edit.setText(settings_dict['storeDescription'])
        self.pubkey_textedit.setText(settings_dict['pubkey'])
        self.notary_servicedesc_textEdit.setText(settings_dict['description'])
        self.percent_comboBox.setCurrentIndex(int(settings_dict['percentage']))
        self.recipient_lineEdit.setText(settings_dict['shippingInformation']['recipient'])
        self.street1_lineEdit.setText(settings_dict['shippingInformation']['street1'])
        self.street2_lineEdit.setText(settings_dict['shippingInformation']['street2'])
        self.city_lineEdit.setText(settings_dict['shippingInformation']['city'])
        self.province_lineEdit.setText(settings_dict['shippingInformation']['province/state/region'])
        self.zip_lineEdit.setText(settings_dict['shippingInformation']['postal/zip'])
        self.country_lineEdit.setText(settings_dict['shippingInformation']['country'])
        self.guid_lineEdit.setText(settings_dict['guid'].encode('hex'))

        self.save_button.clicked.connect(self.saveChanges)


    ##
    # saveChanges(self)
    #     Collects all filled in user data and sends to settings for saving
    def saveChanges(self):
        ret = dict()
        ret['nickname'] = self.nickname_lineEdit.text()
        ret['email'] = self.email_lineEdit.text()
        ret['bitcoinReceivingAddress'] = self.bitcoin_lineEdit.text()
        ret['storeDescription'] = self.store_desc_edit.toPlainText()
        ret['percentage'] = str(self.percent_comboBox.currentIndex())
        ret['description'] = self.notary_servicedesc_textEdit.toPlainText()
        shipping = dict()
        shipping['recipient'] = self.recipient_lineEdit.text()
        shipping['street1'] = self.street1_lineEdit.text()
        shipping['street2'] = self.street2_lineEdit.text()
        shipping['city'] = self.city_lineEdit.text()
        shipping['province/state/region'] = self.province_lineEdit.text()
        shipping['postal/zip'] = self.zip_lineEdit.text()
        shipping['country'] = self.country_lineEdit.text()
        ret['shippingInformation'] = shipping
        ret['avatarURL'] = ""
        ret['myMerchants'] = ""
        ret['isNotary'] = ""
        self.window().id_module.set_settings(ret)
        self.window().redraw()

##
# This class contains the UI for the "Send a message" tab
#
class SendMessage_Ui2(QtGui.QWidget):

    ##
    # Constructor
    #     Creates the "Send Message" tab
    def __init__(self):
        super(SendMessage_Ui2, self).__init__()

        self.setObjectName(_fromUtf8("Form"))
        self.resize(400, 413)
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 391))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.send_message_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.send_message_label.setFont(font)
        self.send_message_label.setObjectName(_fromUtf8("keys_label"))
        self.verticalLayout.addWidget(self.send_message_label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("store_details_label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("nickname_lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.message_subject_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.message_subject_lineEdit.setObjectName(_fromUtf8("bitcoin_lineEdit"))
        self.verticalLayout.addWidget(self.message_subject_lineEdit)
        self.message_body_textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.message_body_textEdit.setObjectName(_fromUtf8("store_desc_edit"))
        self.verticalLayout.addWidget(self.message_body_textEdit)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cancel_button.setObjectName(_fromUtf8("add_notary_label"))
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.send_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.send_button.setAutoFillBackground(False)
        self.send_button.setObjectName(_fromUtf8("save_button"))
        self.horizontalLayout_2.addWidget(self.send_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.setWindowTitle(_translate("Form", "Form", None))
        self.send_message_label.setText(_translate("Form", "Send Message", None))
        self.label.setText(_translate("Form", "To:", None))
        self.message_subject_lineEdit.setText(_translate("Form", "Enter a subject line", None))
        self.message_body_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter a message</p></body></html>", None))
        self.cancel_button.setText(_translate("Form", "Cancel", None))
        self.send_button.setText(_translate("Form", "Send", None))


##
# This class contains the UI for the "My Orders" menu
#
class Ui_OrdersMenu(object):


    ##
    #
    def setupUi(self, OrdersMenu):
        OrdersMenu.setObjectName(_fromUtf8("OrdersMenu"))
        OrdersMenu.resize(400, 300)
        self.verticalLayoutWidget = QtGui.QWidget(OrdersMenu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.OrderLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.OrderLabel.setObjectName(_fromUtf8("OrderLabel"))
        self.verticalLayout.addWidget(self.OrderLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.seller = QtGui.QListView(self.verticalLayoutWidget)
        self.seller.setObjectName(_fromUtf8("seller"))
        self.horizontalLayout.addWidget(self.seller)
        self.sellerBar = QtGui.QScrollBar(self.verticalLayoutWidget)
        self.sellerBar.setOrientation(QtCore.Qt.Vertical)
        self.sellerBar.setObjectName(_fromUtf8("sellerBar"))
        self.horizontalLayout.addWidget(self.sellerBar)
        self.buyerBar = QtGui.QScrollBar(self.verticalLayoutWidget)
        self.buyerBar.setOrientation(QtCore.Qt.Vertical)
        self.buyerBar.setObjectName(_fromUtf8("buyerBar"))
        self.horizontalLayout.addWidget(self.buyerBar)
        self.buyer = QtGui.QListView(self.verticalLayoutWidget)
        self.buyer.setObjectName(_fromUtf8("buyer"))
        self.horizontalLayout.addWidget(self.buyer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(OrdersMenu)
        QtCore.QMetaObject.connectSlotsByName(OrdersMenu)

    def retranslateUi(self, OrdersMenu):
        OrdersMenu.setWindowTitle(_translate("OrdersMenu", "Form", None))
        self.OrderLabel.setText(_translate("OrdersMenu", "Orders", None))


##
# ContractGenUi2
#     This class holds the UI for the contract generator
class ContractGenUi2(QtGui.QWidget):

    ##
    # Constructor
    #     Draws the layout of the "New Contract" tab
    def __init__(self):
        super(ContractGenUi2, self).__init__()
        self.setObjectName(_fromUtf8("Form"))
        self.resize(788, 376)
        self.setAutoFillBackground(False)
        self.gridLayoutWidget = QtGui.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 671, 235))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("store_details_label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.bitcoin_address_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.bitcoin_address_lineEdit.setObjectName(_fromUtf8("bitcoin_lineEdit"))
        self.gridLayout.addWidget(self.bitcoin_address_lineEdit, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("nickname_label"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.price_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.price_lineEdit.setObjectName(_fromUtf8("guid_lineEdit"))
        self.gridLayout.addWidget(self.price_lineEdit, 5, 1, 1, 1)
        self.expiry_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.expiry_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))
        self.gridLayout.addWidget(self.expiry_lineEdit, 6, 1, 1, 1)
        self.item_name_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.item_name_lineEdit.setObjectName(_fromUtf8("add_notary_line"))
        self.gridLayout.addWidget(self.item_name_lineEdit, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("trusted_notaries_label"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("notary_details_label"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("shipping_label"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("keys_label"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.generate_contract_button = QtGui.QPushButton(self)
        self.generate_contract_button.setGeometry(QtCore.QRect(520, 260, 161, 27))
        self.generate_contract_button.setObjectName(_fromUtf8("add_notary_label"))

        ##
        # Add keywords
        self.keywords_label = QtGui.QLabel(self.gridLayoutWidget)
        self.keywords_label.setText("Add keywords")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.keywords_label.setFont(font)
        self.keywords_lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.keywords_lineEdit.setText("Separate keywords by comma (ie word1,word2,word3,...,wordn)")
        self.gridLayout.addWidget(self.keywords_label)
        self.gridLayout.addWidget(self.keywords_lineEdit)

        ##
        # Add pictures
        self.browse_images_label = QtGui.QLabel(self.gridLayoutWidget)
        self.browse_images_label.setText("Add images (max 3):")
        self.browse_images_label.setFont(font)
        self.images_button = QtGui.QPushButton(self.gridLayoutWidget)
        self.images_button.setText("Browse...")
        self.gridLayout.addWidget(self.browse_images_label)
        self.gridLayout.addWidget(self.images_button)
        self.images = list()

        ##
        # Add a description
        self.description_label = QtGui.QLabel(self.gridLayoutWidget)
        self.description_label.setText("Item Description:")
        self.description_label.setFont(font)
        self.gridLayout.addWidget(self.description_label)

        self.description_box = QtGui.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.description_box)

        ##
        # On clicked, generate the new contract data
        # On clicked, find pictures
        self.generate_contract_button.clicked.connect(self.generate_from_input)
        self.images_button.clicked.connect(self.find_images)


        self.label.setText(_translate("Form", "Contract Generator", None))
        self.label_7.setText(_translate("Form", "Offer expiry date", None))
        self.label_6.setText(_translate("Form", "Price (in BTC) of item to sell", None))
        self.label_4.setText(_translate("Form", "Your Bitcoin address", None))
        self.label_5.setText(_translate("Form", "Name of item to sell", None))
        self.label_2.setText(_translate("Form", "Contract", None))
        self.generate_contract_button.setText(_translate("Form", "Generate Contract", None))


    ##
    # Creates a new contract using the fields in the UI
    def generate_from_input(self):
        contract = dict()
        contract['expiry'] = str(self.expiry_lineEdit.text())
        contract['price'] = str(self.price_lineEdit.text())
        contract['bitcoin_address'] = str(self.bitcoin_address_lineEdit.text())
        contract['item_name'] = str(self.item_name_lineEdit.text())
        contract['keywords'] = str(self.keywords_lineEdit.text().split(','))
        contract['description'] = str(self.description_box.text())
        contract['images'] = self.images
        self.window().id_module.new_contract(contract)
        self.window().redraw()

    ##
    # Browse and add images
    # Saves the first three selected image paths to self.images (list)
    def find_images(self):
        self.images = QtGui.QFileDialog.getOpenFileNames(self, 'Add Images', '', '')[0:3]
        if len(self.images) != 0:
            self.images_button.setText(str(len(self.images)) + " selected")
        else:
            self.images_button.setText("Browse...")


##
# This class holds the UI for the Contract View Tab
class contractView_Tab(QtGui.QWidget):
    ##
    # Constructor
    # Creates the contract view tab
    #     @param ricardian_contract: ricardian contract being viewed in the tab
    def __init__(self, ricardian_contract):
        super(contractView_Tab, self).__init__()

        self.contract_obj = ricardian_contract

        self.setObjectName(_fromUtf8("Form"))
        self.resize(1199, 1250)
        self.gridLayoutWidget = QtGui.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 570, 801, 231))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.descriptionTextBrowser = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.descriptionTextBrowser.setObjectName(_fromUtf8("descriptionTextBrowser"))
        self.gridLayout.addWidget(self.descriptionTextBrowser, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 161, 181))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(160, 0, 641, 181))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.itemName = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.itemName.setFont(font)
        self.itemName.setText(_fromUtf8(""))
        self.itemName.setObjectName(_fromUtf8("itemName"))
        self.verticalLayout_3.addWidget(self.itemName)
        self.price = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.price.setFont(font)
        self.price.setText(_fromUtf8(""))
        self.price.setObjectName(_fromUtf8("price"))
        self.verticalLayout_3.addWidget(self.price)
        self.dateUploaded = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.dateUploaded.setText(_fromUtf8(""))
        self.dateUploaded.setObjectName(_fromUtf8("dateUploaded"))
        self.verticalLayout_3.addWidget(self.dateUploaded)
        self.expires = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.expires.setText(_fromUtf8(""))
        self.expires.setObjectName(_fromUtf8("expires"))
        self.verticalLayout_3.addWidget(self.expires)
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(0, 540, 91, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayoutWidget = QtGui.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 850, 801, 271))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pictureOne = QtGui.QLabel(self.horizontalLayoutWidget)
        self.pictureOne.setText(_fromUtf8(""))
        self.pictureOne.setObjectName(_fromUtf8("pictureOne"))
        self.horizontalLayout.addWidget(self.pictureOne)
        self.pictureTwo = QtGui.QLabel(self.horizontalLayoutWidget)
        self.pictureTwo.setText(_fromUtf8(""))
        self.pictureTwo.setObjectName(_fromUtf8("pictureTwo"))
        self.horizontalLayout.addWidget(self.pictureTwo)
        self.pictureThree = QtGui.QLabel(self.horizontalLayoutWidget)
        self.pictureThree.setText(_fromUtf8(""))
        self.pictureThree.setObjectName(_fromUtf8("pictureThree"))
        self.horizontalLayout.addWidget(self.pictureThree)
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(0, 820, 66, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(40, 1210, 121, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.desiredQuantitySpinBox = QtGui.QSpinBox(self)
        self.desiredQuantitySpinBox.setGeometry(QtCore.QRect(170, 1200, 71, 31))
        self.desiredQuantitySpinBox.setObjectName(_fromUtf8("desiredQuantitySpinBox"))
        self.label_9 = QtGui.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(250, 1210, 131, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.noteForMerchantLineEdit = QtGui.QLineEdit(self)
        self.noteForMerchantLineEdit.setGeometry(QtCore.QRect(400, 1210, 321, 27))
        self.noteForMerchantLineEdit.setObjectName(_fromUtf8("noteForMerchantLineEdit"))
        self.purchaseButton = QtGui.QPushButton(self)
        self.purchaseButton.setGeometry(QtCore.QRect(730, 1210, 98, 27))
        self.purchaseButton.setObjectName(_fromUtf8("purchaseButton"))
        self.sellerAvatar = QtGui.QLabel(self)
        self.sellerAvatar.setGeometry(QtCore.QRect(990, 10, 201, 181))
        self.sellerAvatar.setText(_fromUtf8(""))
        self.sellerAvatar.setObjectName(_fromUtf8("sellerAvatar"))
        self.label_15 = QtGui.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(310, 1170, 81, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.keywords = QtGui.QLineEdit(self)
        self.keywords.setGeometry(QtCore.QRect(400, 1170, 321, 27))
        self.keywords.setObjectName(_fromUtf8("keywords"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 190, 801, 322))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sellerName = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.sellerName.setFont(font)
        self.sellerName.setText(_fromUtf8(""))
        self.sellerName.setObjectName(_fromUtf8("sellerName"))
        self.gridLayout_2.addWidget(self.sellerName, 0, 1, 1, 1)
        self.bitcoinReceivingAddress = QtGui.QTextBrowser(self.gridLayoutWidget_2)
        self.bitcoinReceivingAddress.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.bitcoinReceivingAddress.setObjectName(_fromUtf8("bitcoinReceivingAddress"))
        self.gridLayout_2.addWidget(self.bitcoinReceivingAddress, 3, 1, 1, 1)
        self.guid = QtGui.QTextBrowser(self.gridLayoutWidget_2)
        self.guid.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.guid.setObjectName(_fromUtf8("guid"))
        self.gridLayout_2.addWidget(self.guid, 2, 1, 1, 1)
        self.sellerEmail = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sellerEmail.setFont(font)
        self.sellerEmail.setText(_fromUtf8(""))
        self.sellerEmail.setObjectName(_fromUtf8("sellerEmail"))
        self.gridLayout_2.addWidget(self.sellerEmail, 1, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)
        self.publicKey = QtGui.QTextBrowser(self.gridLayoutWidget_2)
        self.publicKey.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.publicKey.setObjectName(_fromUtf8("publicKey"))
        self.gridLayout_2.addWidget(self.publicKey, 4, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(330, 1130, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ledger = QtGui.QLineEdit(self)
        self.ledger.setGeometry(QtCore.QRect(400, 1130, 321, 27))
        self.ledger.setObjectName(_fromUtf8("ledger"))

        
        self.label.setText(_translate("Form", "Item Name:", None))
        self.label_2.setText(_translate("Form", "Price:", None))
        self.label_3.setText(_translate("Form", "Date Uploaded:", None))
        self.label_4.setText(_translate("Form", "Expires:", None))
        self.label_6.setText(_translate("Form", "Description: ", None))
        self.label_7.setText(_translate("Form", "Pictures:", None))
        self.label_8.setText(_translate("Form", "Desired Quantity:", None))
        self.label_9.setText(_translate("Form", "Note for Merchant:", None))
        self.purchaseButton.setText(_translate("Form", "Purchase", None))
        self.label_15.setText(_translate("Form", "Keywords:", None))
        self.bitcoinReceivingAddress.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdfsdddddddddddddddddddddddddddddddddddddddddddddddddasdfasdfasdfasdfasdfasdfasdffdasdf</p></body></html>", None))
        self.guid.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdfsddddddddddddddddddddddddddddddddddddddddddddddddd</p></body></html>", None))
        self.label_13.setText(_translate("Form", "GUID:", None))
        self.publicKey.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdfsddddddddddddddddddddddddddddddddddddddddddddddddd</p></body></html>", None))
        self.label_11.setText(_translate("Form", "Seller Email:", None))
        self.label_10.setText(_translate("Form", "Seller Name:", None))
        self.label_12.setText(_translate("Form", "Bitcoin Receiving Address:", None))
        self.label_14.setText(_translate("Form", "Public Key:", None))
        self.label_5.setText(_translate("Form", "Ledger:", None))

        meta = ricardian_contract.get_module('metadata')
        id = ricardian_contract.get_module('id')
        trade = ricardian_contract.get_module('trade')
        ledger = ricardian_contract.get_module('ledger')

        ##
        # Set values from the trade module
        self.itemName.setText(trade['name'])
        self.price.setText(trade['price'])
        self.descriptionTextBrowser.setText(trade['description'])
        self.keywords.setText(', '.join(trade['keywords']))
        for count, image_store in enumerate(trade['images']):
            if count == 0:
                self.pictureOne.setPixmap(image_store.get_repr().toqpixmap())
                self.pictureOne.setScaledContents(True)
            elif count == 1:
                self.pictureTwo.setPixmap(image_store.get_repr().toqpixmap())
                self.pictureTwo.setScaledContents(True)
            elif count == 2:
                self.pictureThree.setPixmap(image_store.get_repr().toqpixmap())
                self.pictureThree.setScaledContents(True)

        ##
        # Set values from the metadata module
        self.dateUploaded.setText(meta['date'])
        self.expires.setText(meta['expiry'])

        ##
        # Set values from the seller module
        #self.bitcoinRecevingAddress.setText(id['seller']['bitcoinReceivingAddress'])
        self.sellerName.setText(id['seller']['nickname'])
        self.sellerEmail.setText(id['seller']['email'])
        self.guid.setText(id['seller']['guid'])
        self.publicKey.setText(id['seller']['pubkey'])
        avatar_pm = id['seller']['avatar'].get_repr().toqpixmap()
        self.sellerAvatar.setPixmap(avatar_pm)
        self.sellerAvatar.setScaledContents(True)

        self.purchaseButton.clicked.connect(self.purchase_contract)

    ##
    # Defines action to be taken when purchaseButton is clicked
    def purchase_contract(self):
        self.window().id_module.make_purchase(self.contract_obj)
        self.window().redraw()

##
# This class holds the view for a notary
class notaryViewTab(QtGui.QWidget):

    ##
    # Constructor
    # Creates the Notary View Tab
    def __init__(self, notary_repr_obj):
        super(notaryViewTab, self).__init__()
        self.setObjectName(_fromUtf8("Form"))
        self.resize(941, 527)
        self.label_11 = QtGui.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(540, 6, 231, 211))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayoutWidget = QtGui.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 771, 452))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.GUID = QtGui.QTextEdit(self.gridLayoutWidget)
        self.GUID.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.GUID.setObjectName(_fromUtf8("GUID"))
        self.gridLayout.addWidget(self.GUID, 2, 1, 1, 1)
        self.publicKey = QtGui.QTextEdit(self.gridLayoutWidget)
        self.publicKey.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.publicKey.setObjectName(_fromUtf8("publicKey"))
        self.gridLayout.addWidget(self.publicKey, 3, 1, 1, 1)
        self.bitcoinReceivingAddress = QtGui.QTextEdit(self.gridLayoutWidget)
        self.bitcoinReceivingAddress.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.bitcoinReceivingAddress.setObjectName(_fromUtf8("bitcoinReceivingAddress"))
        self.gridLayout.addWidget(self.bitcoinReceivingAddress, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.storeEmail = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.storeEmail.setFont(font)
        self.storeEmail.setText(_fromUtf8(""))
        self.storeEmail.setObjectName(_fromUtf8("storeEmail"))
        self.gridLayout.addWidget(self.storeEmail, 1, 1, 1, 1)
        self.storeName = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.storeName.setFont(font)
        self.storeName.setText(_fromUtf8(""))
        self.storeName.setObjectName(_fromUtf8("storeName"))
        self.gridLayout.addWidget(self.storeName, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.fee = QtGui.QLabel(self.gridLayoutWidget)
        self.fee.setText(_fromUtf8(""))
        self.fee.setObjectName(_fromUtf8("fee"))
        self.gridLayout.addWidget(self.fee, 5, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.description = QtGui.QTextEdit(self.gridLayoutWidget)
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout.addWidget(self.description, 6, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(800, 20, 221, 211))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.avatar = QtGui.QLabel(self)
        self.avatar.setGeometry(QtCore.QRect(780, 20, 151, 141))
        self.avatar.setText(_fromUtf8(""))
        self.avatar.setObjectName(_fromUtf8("avatar"))

        self.setWindowTitle(_translate("Form", "Form", None))
        self.GUID.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdfasdfasdfasdfasdfasdfasdfasdfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffasddfasdasdfasdfasdfasdffasdf</p></body></html>", None))
        self.publicKey.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdasdfadfasdfasdfasdfasdfasdfasdffsdsdfffffffffffffffffffffffasdasdfasdfasdfasdfasdfasdfasdfasdasdf</p></body></html>", None))
        self.bitcoinReceivingAddress.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdfadsfadfasdfasdfasdfasfasdfasfdfsdadsfsdfdfsafdsadfsdfsadsfdafsadfsdasdasdfadsfasdfasdfasdfasdassadfasdfasdfasdfasdfasfdasdfdsaf</p></body></html>", None))
        self.label_4.setText(_translate("Form", "Public Key:", None))
        self.label_7.setText(_translate("Form", "Fee (%):", None))
        self.label.setText(_translate("Form", "User Name:", None))
        self.label_3.setText(_translate("Form", "GUID:", None))
        self.label_5.setText(_translate("Form", "Bitcoin Receiving Address:", None))
        self.label_2.setText(_translate("Form", "User Email:", None))
        self.label_9.setText(_translate("Form", "Description", None))

        notary_repr = notary_repr_obj.get()
        self.bitcoinReceivingAddress.setText(notary_repr['bitcoinReceivingAddress'])
        self.avatar.setPixmap(notary_repr['avatar'].get_repr().toqpixmap())
        self.avatar.setScaledContents(True)
        self.description.setText(notary_repr['description'])
        self.fee.setText(notary_repr['fee'])
        self.GUID.setText(notary_repr['guid'])
        self.storeEmail.setText(notary_repr['email'])
        self.publicKey.setText(notary_repr['pubkey'])
        self.storeName.setText(notary_repr['name'])

##
# bootStrap_Tab
#     This class holds the UI for the bootstrap tab
class bootStrap_Tab(QtGui.QWidget):

    ##
    # Constructor
    #     Creates the bootstrap tab
    def __init__(self):
        super(bootStrap_Tab, self).__init__()
        self.setObjectName(_fromUtf8("OrdersMenu"))
        self.resize(400, 300)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(70, 180, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.ip_lineEdit = QtGui.QLineEdit(self)
        self.ip_lineEdit.setGeometry(QtCore.QRect(50, 70, 161, 27))
        self.ip_lineEdit.setObjectName(_fromUtf8("ip_lineEdit"))
        self.port_lineEdit = QtGui.QLineEdit(self)
        self.port_lineEdit.setGeometry(QtCore.QRect(50, 120, 161, 27))
        self.port_lineEdit.setObjectName(_fromUtf8("port_lineEdit"))
        self.setWindowTitle(_translate("OrdersMenu", "Form", None))
        self.pushButton.setText(_translate("OrdersMenu", "Bootstrap", None))
        self.ip_lineEdit.setText(_translate("OrdersMenu", "Enter IP Address", None))
        self.port_lineEdit.setText(_translate("OrdersMenu", "Enter Port Number", None))

        ##
        # On clicked, generate the bootstrap
        self.pushButton.clicked.connect(self.initiate_bootstrap)

    ##
    # Attempts to bootstrap the node module to the network using the fields in the tab
    def initiate_bootstrap(self):
        self.window().node.attempt_bootstrap(str(self.ip_lineEdit.text()), int(self.port_lineEdit.text()))

##
# This class is a view for the results of an OpenBazaar search
class SearchResultsWidget(QtGui.QWidget):
    def __init__(self, search, list_of_contracts):
        super(SearchResultsWidget, self).__init__()

        ##
        # Save the list of contracts, so when one is selected we can draw the contract
        # view using it's data
        self.contracts_found = list_of_contracts

        self.setObjectName(_fromUtf8("search_results_widget"))
        self.resize(748, 568)
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 751, 571))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.search_results_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.search_query_label = QtGui.QLabel(self.verticalLayoutWidget)
        header_font = QtGui.QFont()
        header_font.setFamily(_fromUtf8("Latin Modern Sans"))
        header_font.setPointSize(36)
        self.search_query_label.setFont(header_font)
        header_font.setUnderline(True)
        self.search_results_label.setFont(header_font)
        self.search_results_label.setObjectName(_fromUtf8("search_results_label"))
        self.verticalLayout.addWidget(self.search_results_label)
        self.verticalLayout.addWidget(self.search_query_label)
        self.results_list = QtGui.QListWidget(self.verticalLayoutWidget)
        self.results_list.setObjectName(_fromUtf8("results_list"))


        ##
        # Add all search results to the list
        #
        item_font = QtGui.QFont()
        item_font.setPointSize(16)
        for contract in self.contracts_found:
            item = QtGui.QListWidgetItem()
            item.setFont(item_font)
            item.setText(contract.get_itemname())
            item.setData(QtCore.Qt.UserRole, contract)
            self.results_list.addItem(item)

        self.results_list.itemClicked.connect(self.result_clicked)

        self.verticalLayout.addWidget(self.results_list)

        self.setWindowTitle(_translate("search_results_widget", "Search Results", None))
        self.search_results_label.setText(_translate("search_results_widget", "Search Results", None))
        self.search_query_label.setText(_translate("search_results_widget", "Queried: " + search, None))
        self.results_list.setSortingEnabled(False)

    ##
    # Defines action to be taken on item result click.
    def result_clicked(self, list_item):
        ##
        # Try to get contract data from item
        try:
            ric_repr = list_item.data(QtCore.Qt.UserRole).toPyObject()
        except:
            print 'exception'
            return
        scroll_area = QtGui.QScrollArea()
        scroll_area.setWidget(contractView_Tab(ric_repr))
        self.window().add_tab(scroll_area, ric_repr.get_itemname())
