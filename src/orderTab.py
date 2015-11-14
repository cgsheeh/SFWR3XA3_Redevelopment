# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orderTab.ui'
#
# Created: Sat Nov 14 00:48:57 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_OrdersMenu(object):
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

