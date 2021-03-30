# Author :  Oganezov Alexandre
# assisted by: Alexandre Braure; Hengsheng ZHAO; Thanh Cong Vo
#code généré à l'aide de PYQTdesigner

from PyQt5 import QtCore, QtGui, QtWidgets
from InfoAuteursFinale import Ui_NousContacter
from InfoLegaleFinale import Ui_InfoLegale
from InfoGeneraleFinale import Ui_InfoGenerale

class Ui_InfoMenu(object):

    # créations de différente fonctions
    #ces fonctions seront utilisé pour faire appel a d'autres fichier.py
    def openNousContacter(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NousContacter()
        self.ui.setupUiNousContacter(self.window)
        self.window.show()

    def openInfoLegale(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InfoLegale()
        self.ui.setupUiLegale(self.window)
        self.window.show()

    def openInfoGenerale(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InfoGenerale()
        self.ui.setupUiGenerale(self.window)
        self.window.show()

    #fonction permetant la création de la fenêtre
    def setupUi(self, InfoMenu):
        InfoMenu.setObjectName("InfoMenu")
        InfoMenu.setEnabled(True)
        InfoMenu.resize(430, 340)
        InfoMenu.setMinimumSize(QtCore.QSize(430, 340))
        InfoMenu.setMaximumSize(QtCore.QSize(430, 340))
        InfoMenu.setWindowTitle("Application GFD - Informations")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logoApp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)#chemin du logo de la fenêtre
        InfoMenu.setWindowIcon(icon)
        InfoMenu.setToolTip("")
        InfoMenu.setStatusTip("")
        InfoMenu.setWhatsThis("")
        InfoMenu.setStyleSheet("background-color: rgb(57, 64, 65);")
        InfoMenu.setWindowFilePath("")

        #paramétre du bouton "Mentions légales"
        self.btnInfoLegale = QtWidgets.QPushButton(InfoMenu)
        self.btnInfoLegale.setGeometry(QtCore.QRect(140, 250, 151, 71))
        # choix de la police
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btnInfoLegale.setFont(font)
        self.btnInfoLegale.setStyleSheet("background-color: rgb(142, 204, 204);")
        self.btnInfoLegale.setObjectName("btnInfoLegale")
        self.btnInfoLegale.clicked.connect(self.openInfoLegale)#fait appel a la fonction openInfoLegale

        #paramétre du bouton "Informations générales"
        self.btnInfoGenerale = QtWidgets.QPushButton(InfoMenu)
        self.btnInfoGenerale.setGeometry(QtCore.QRect(140, 140, 151, 71))
        # choix de la police
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.btnInfoGenerale.setFont(font)
        self.btnInfoGenerale.setStyleSheet("background-color: rgb(142, 204, 204);")
        self.btnInfoGenerale.setObjectName("btnInfoGenerale")
        self.btnInfoGenerale.clicked.connect(self.openInfoGenerale)#fait appel a la fonction openInfoGenerale

        #paramétre du bouton "Nous contacter"
        self.btnNousContacter = QtWidgets.QPushButton(InfoMenu)
        self.btnNousContacter.setGeometry(QtCore.QRect(140, 30, 151, 71))
        #choix de la police
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.btnNousContacter.setFont(font)
        self.btnNousContacter.setStyleSheet("background-color: rgb(142, 204, 204);")
        self.btnNousContacter.setObjectName("btnNousContacter")
        self.btnNousContacter.clicked.connect(self.openNousContacter)#fait appel a la fonction openNousContacter


        self.retranslateUi(InfoMenu)
        QtCore.QMetaObject.connectSlotsByName(InfoMenu)

    def retranslateUi(self, InfoMenu):
        _translate = QtCore.QCoreApplication.translate
        self.btnInfoLegale.setText(_translate("InfoMenu", "Mentions légales"))
        self.btnInfoGenerale.setText(_translate("InfoMenu", "Informations générales"))
        self.btnNousContacter.setText(_translate("InfoMenu", "Nous contacter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoMenu = QtWidgets.QWidget()
    ui = Ui_InfoMenu()
    ui.setupUi(InfoMenu)
    InfoMenu.show()
    sys.exit(app.exec_())
