# Author :  Oganezov Alexandre
# assisted by: Alexandre Braure; Hengsheng ZHAO; Thanh Cong Vo
#code généré à l'aide de PYQTdesigner

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoGenerale(object):
    def setupUiGenerale(self, InfoGenerale):
        InfoGenerale.setObjectName("InfoGenerale")
        InfoGenerale.resize(550, 590)
        InfoGenerale.setMinimumSize(QtCore.QSize(550, 590))
        InfoGenerale.setMaximumSize(QtCore.QSize(550, 590))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logoApp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InfoGenerale.setWindowIcon(icon)
        InfoGenerale.setStyleSheet("background-color: rgb(57, 64, 65);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser = QtWidgets.QTextBrowser(InfoGenerale)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 530, 571))
        self.textBrowser.setMinimumSize(QtCore.QSize(530, 500))
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(InfoGenerale)
        QtCore.QMetaObject.connectSlotsByName(InfoGenerale)

    def retranslateUi(self, InfoGenerale):
        _translate = QtCore.QCoreApplication.translate
        InfoGenerale.setWindowTitle(_translate("InfoGenerale", "Application GFD - Informations générales "))
        self.textBrowser.setHtml(_translate("InfoGenerale", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">  Ce projet se réfère à l’UE projet, de deuxième année de licence d’informatique de l’université Paris Descartes. Parmis les sujets proposés, nous avons choisis le sujet qui porte sur la reconnaissance de formes à partir des descripteurs de Fourier génériques (thèse du Dr Zhang) projet (2019-l2l1). Pour ce projet nous avons été encadrés par le docteur Wendling Laurent enseignant-chercheur à l’université Paris Descartes.Nous avons développés un logiciel scientifique qui permet de comparer des images, ainsi que des méthodes de classification et de requête. Cette approche, intégrée dans “MPEG7”, donne de très bons résultats pour la reconnaissance de Logos ou de formes pleines. Cette méthode, est relativement simple à mettre en œuvre, est fondée sur une transformée discrète polaire, pour mieux prendre en compte la rotation d’objets. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">Les étapes à suivre sont les suivantes :</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">  - Mise à niveau de gris des images</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">  - Calcul de Descripteurs de Fourier Génériques (algorithme général fourni) pour obtenir une nouvelle représentation (vecteur) </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">  -Calcul de distance (comparaison de deux images à partir de leur description) </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">  -Calcul de la distance entre une image (requête) et plusieurs images (retrieval : affichage en fonction des distances les plus proches) </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:10pt;\">  -Cette approche sera testée sur différentes bases (formes pleines, symboles)</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoGenerale = QtWidgets.QWidget()
    ui = Ui_InfoGenerale()
    ui.setupUiGenerale(InfoGenerale)
    InfoGenerale.show()
    sys.exit(app.exec_())
