# Author :  Oganezov Alexandre
# assisted by: Alexandre Braure; Hengsheng ZHAO; Thanh Cong Vo
#code généré à l'aide de PYQTdesigner
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

from InfoMenuFinale import Ui_InfoMenu
from MenuMethodeFinaleV2 import Ui_MenuMethode

class Ui_AppGFD(object):

    # créations de différente fonctions
    # ces fonctions seront utilisé pour faire appel a d'autres fichier.py

    #fonction pour ouvrir le menu d'informations
    def openInfo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InfoMenu()
        self.ui.setupUi(self.window)
        self.window.show()

    #fonction pour ouvrir le menu des méthodes
    def openMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MenuMethode()
        self.ui.setupUi(self.window)
        self.window.show()
    #création de la fênetre
    def setupUi(self, AppGFD):
        AppGFD.setObjectName("AppGFD")
        AppGFD.setEnabled(True)
        AppGFD.resize(435, 340)
        AppGFD.setMinimumSize(QtCore.QSize(435, 340))
        AppGFD.setMaximumSize(QtCore.QSize(435, 340))
        font = QtGui.QFont()
        font.setPointSize(9)
        AppGFD.setFont(font)
        AppGFD.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        AppGFD.setWindowTitle("Application GFD")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logoApp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AppGFD.setWindowIcon(icon)
        AppGFD.setStyleSheet("background-color: rgb(57, 64, 65);")
        AppGFD.setWindowFilePath("")

        #paramétre d'affichage du bouton "commencer"
        self.Btn_begin = QtWidgets.QPushButton(AppGFD)
        self.Btn_begin.setGeometry(QtCore.QRect(120, 50, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Btn_begin.setFont(font)
        self.Btn_begin.setStyleSheet("background-color: rgb(142, 204, 204);")
        self.Btn_begin.setObjectName("Btn_begin")
        self.Btn_begin.clicked.connect(self.openMenu)

        #paramétre d'affichage du bouton "quitter"
        self.Btn_exit = QtWidgets.QPushButton(AppGFD)
        self.Btn_exit.setGeometry(QtCore.QRect(120, 190, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Btn_exit.setFont(font)
        self.Btn_exit.setStyleSheet("background-color: rgb(142, 204, 204);")
        self.Btn_exit.setObjectName("Btn_exit")
        self.Btn_exit.clicked.connect(QApplication.instance().quit)

        # paramétre d'affichage du bouton "informations"
        self.Btn_info = QtWidgets.QPushButton(AppGFD)
        self.Btn_info.setGeometry(QtCore.QRect(300, 310, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.Btn_info.setFont(font)
        self.Btn_info.setStyleSheet("background-color: rgb(80, 113, 123);")
        self.Btn_info.setObjectName("Btn_info")
        self.Btn_info.clicked.connect(self.openInfo)

        self.retranslateUi(AppGFD)
        QtCore.QMetaObject.connectSlotsByName(AppGFD)

    def retranslateUi(self, AppGFD):
        _translate = QtCore.QCoreApplication.translate
        self.Btn_begin.setText(_translate("AppGFD", "Démarrer"))
        self.Btn_exit.setText(_translate("AppGFD", "Quitter"))
        self.Btn_info.setText(_translate("AppGFD", "Informations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AppGFD = QtWidgets.QWidget()
    ui = Ui_AppGFD()
    ui.setupUi(AppGFD)
    AppGFD.show()
    sys.exit(app.exec_())
