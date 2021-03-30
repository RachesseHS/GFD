# Author :  Oganezov Alexandre
# assisted by: Alexandre Braure; Hengsheng ZHAO; Thanh Cong Vo
#code généré à l'aide de PYQTdesigner



from PyQt5 import QtCore, QtGui, QtWidgets
from MenuAide import Ui_Aide
import CalculateGFD
import retrieval
import compare_2images_bis
import matrice_de_confusion

class Ui_MenuMethode(object):
    def openGFP(self):
        CalculateGFD.FunctionGfd()

    def openRetrieval(self):
        retrieval.FunctionRetrieval()

    def openCompare(self):
        compare_2images_bis.FunctionCompare()

    def openMatrice(self):
        matrice_de_confusion.FunctionMatrice()

    def openAide(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Aide()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MenuMethode):
        MenuMethode.setObjectName("MenuMethode")
        MenuMethode.resize(380, 371)
        MenuMethode.setMinimumSize(QtCore.QSize(380, 371))
        MenuMethode.setMaximumSize(QtCore.QSize(380, 371))
        MenuMethode.setWindowTitle("Application GFD - Menu méthodes")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logoApp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MenuMethode.setWindowIcon(icon)
        MenuMethode.setStyleSheet("background-color: rgb(57, 64, 65);")

        self.Btn_GFD = QtWidgets.QPushButton(MenuMethode)
        self.Btn_GFD.setGeometry(QtCore.QRect(110, 20, 161, 61))
        self.Btn_GFD.setStyleSheet("background-color: rgb(142, 204, 204);\n""font: 9pt \"Roboto\";")
        self.Btn_GFD.setObjectName("Btn_GFD")
        self.Btn_GFD.clicked.connect(self.openGFP)


        self.Btn_Comparaison = QtWidgets.QPushButton(MenuMethode)
        self.Btn_Comparaison.setGeometry(QtCore.QRect(110, 110, 161, 61))
        self.Btn_Comparaison.setStyleSheet("background-color: rgb(142, 204, 204);\n""font: 9pt \"Roboto\";")
        self.Btn_Comparaison.setObjectName("Btn_Comparaison")
        self.Btn_Comparaison.clicked.connect(self.openCompare)

        self.Btn_Retrieval = QtWidgets.QPushButton(MenuMethode)
        self.Btn_Retrieval.setGeometry(QtCore.QRect(110, 200, 161, 61))
        self.Btn_Retrieval.setStyleSheet("background-color: rgb(142, 204, 204);\n""font: 9pt \"Roboto\";")
        self.Btn_Retrieval.setObjectName("Btn_Retrieval")
        self.Btn_Retrieval.clicked.connect(self.openRetrieval)


        self.Btn_Matrice = QtWidgets.QPushButton(MenuMethode)
        self.Btn_Matrice.setGeometry(QtCore.QRect(110, 290, 161, 61))
        self.Btn_Matrice.setStyleSheet("background-color: rgb(142, 204, 204);\n""font: 9pt \"Roboto\";")
        self.Btn_Matrice.setObjectName("Btn_Matrice")
        self.Btn_Matrice.clicked.connect(self.openMatrice)


        self.btn_Aide = QtWidgets.QPushButton(MenuMethode)
        self.btn_Aide.setGeometry(QtCore.QRect(300, 330, 71, 28))
        self.btn_Aide.setStyleSheet("background-color: rgb(80, 113, 123);\n""font: 8pt \"Roboto\";")
        self.btn_Aide.setObjectName("btn_Aide")
        self.btn_Aide.clicked.connect(self.openAide)


        self.retranslateUi(MenuMethode)
        QtCore.QMetaObject.connectSlotsByName(MenuMethode)

    def retranslateUi(self, MenuMethode):
        _translate = QtCore.QCoreApplication.translate
        self.Btn_GFD.setText(_translate("MenuMethode", "GFD"))
        self.Btn_Comparaison.setText(_translate("MenuMethode", "Comparaison d\'images"))
        self.Btn_Retrieval.setText(_translate("MenuMethode", "Retrieval"))
        self.Btn_Matrice.setText(_translate("MenuMethode", "Matrice de confusion"))
        self.btn_Aide.setText(_translate("MenuMethode", "Aide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuMethode = QtWidgets.QWidget()
    ui = Ui_MenuMethode()
    ui.setupUi(MenuMethode)
    MenuMethode.show()
    sys.exit(app.exec_())
