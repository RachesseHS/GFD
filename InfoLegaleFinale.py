# Author :  Oganezov Alexandre
# assisted by: Alexandre Braure; Hengsheng ZHAO; Thanh Cong Vo
#code généré à l'aide de PYQTdesigner

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoLegale(object):
    def setupUiLegale(self, InfoLegale):
        InfoLegale.setObjectName("InfoLegale")
        InfoLegale.resize(450, 360)
        InfoLegale.setMinimumSize(QtCore.QSize(450, 360))
        InfoLegale.setMaximumSize(QtCore.QSize(450, 360))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logoApp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InfoLegale.setWindowIcon(icon)
        InfoLegale.setStyleSheet("background-color: rgb(57, 64, 65);")
        self.textBrowser = QtWidgets.QTextBrowser(InfoLegale)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 431, 341))
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(InfoLegale)
        QtCore.QMetaObject.connectSlotsByName(InfoLegale)

    def retranslateUi(self, InfoLegale):
        _translate = QtCore.QCoreApplication.translate
        InfoLegale.setWindowTitle(_translate("InfoLegale", "Application GFD - Mentions légales"))
        self.textBrowser.setHtml(_translate("InfoLegale", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">Application GFD is free software. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">You may use it for any personal, commercial, institutional or educational purpose,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">including installing it on as many different computers as you wish.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">You may also copy, distribute, modify, and/or resell application GFD,under the terms of </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">the GNU General Public License (GPL) as published by the Free Software Foundation – </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">either version 2 of the License, or (at your option) any later version. In granting you this right, the GPL requires that the source code you distribute is itself available under the GPL.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoLegale = QtWidgets.QWidget()
    ui = Ui_InfoLegale()
    ui.setupUiLegale(InfoLegale)
    InfoLegale.show()
    sys.exit(app.exec_())
