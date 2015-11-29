# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notaryView.ui'
#
# Created: Sat Nov 28 19:09:31 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(778, 390)
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(540, 6, 231, 211))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 771, 368))
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
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
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
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.reputationPledge = QtGui.QLabel(self.gridLayoutWidget)
        self.reputationPledge.setText(_fromUtf8(""))
        self.reputationPledge.setObjectName(_fromUtf8("reputationPledge"))
        self.gridLayout.addWidget(self.reputationPledge, 5, 1, 1, 1)
        self.fee = QtGui.QLabel(self.gridLayoutWidget)
        self.fee.setText(_fromUtf8(""))
        self.fee.setObjectName(_fromUtf8("fee"))
        self.gridLayout.addWidget(self.fee, 6, 1, 1, 1)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(800, 20, 221, 211))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.publicKey.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdasdfadfasdfasdfasdfasdfasdfasdffsdsdfffffffffffffffffffffffasdasdfasdfasdfasdfasdfasdfasdfasdasdf</p></body></html>", None))
        self.GUID.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdfasdfasdfasdfasdfasdfasdfasdfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffasddfasdasdfasdfasdfasdffasdf</p></body></html>", None))
        self.label_4.setText(_translate("Form", "Public Key:", None))
        self.label_7.setText(_translate("Form", "Fee (%):", None))
        self.bitcoinReceivingAddress.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asdfadsfadfasdfasdfasdfasfasdfasfdfsdadsfsdfdfsafdsadfsdfsadsfdafsadfsdasdasdfadsfasdfasdfasdfasdassadfasdfasdfasdfasdfasfdasdfdsaf</p></body></html>", None))
        self.label.setText(_translate("Form", "User Name:", None))
        self.label_3.setText(_translate("Form", "GUID:", None))
        self.label_5.setText(_translate("Form", "Bitcoin Receiving Address:", None))
        self.label_6.setText(_translate("Form", "Reputation Pledge:", None))
        self.label_2.setText(_translate("Form", "User Email:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

