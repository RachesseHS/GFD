# Author :  Oganezov Alexandre
# assisted by: Alexandre Braure; Hengsheng ZHAO; Thanh Cong Vo
#code généré à l'aide de PYQTdesigner


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Aide(object):
    def setupUi(self, Aide):
        Aide.setObjectName("Aide")
        Aide.resize(721, 511)
        Aide.setMinimumSize(QtCore.QSize(721, 511))
        Aide.setMaximumSize(QtCore.QSize(721, 511))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logoApp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Aide.setWindowIcon(icon)
        Aide.setStyleSheet("background-color: rgb(57, 64, 65);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser = QtWidgets.QTextBrowser(Aide)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 701, 491))
        self.textBrowser.setMinimumSize(QtCore.QSize(530, 0))
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Aide)
        QtCore.QMetaObject.connectSlotsByName(Aide)

    def retranslateUi(self, Aide):
        _translate = QtCore.QCoreApplication.translate
        Aide.setWindowTitle(_translate("Aide", "Application GFD - Aide"))
        self.textBrowser.setHtml(_translate("Aide", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Ce programme est composé de 4 différentes méthodes:</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">1)  GFD : Cette méthode doit être lancée impérativement en première, sinon aucune autre méthode ne pourra être utilisé. Une fois lancée l\'utilisateur devra choisir une base d’images “.pgm” , ensuite il devra entrer les valeurs de Rho et Thêta, qui définirons le nombre de valeurs associées à l’image. Cette tâche risque de durer un certain temps, un message &quot;completed&quot; devra apparaître une fois le calcul du GFD fini.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">2)  Comparaison d’images : Prend en entrées deux fichier “.gfd” du répertoire de résultat “GFD”, décrivants leur image respective. Affiche l\'histogramme des deux images superposées dans un repère ainsi que le taux de similarité et la distance entre les deux images.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">3)  Retrieval :Prend en entrées les résultats contenus dans le dossier “GFD”,  une image à sélectionner dans la base d’images et le nombre d’images à afficher dans la fenêtre de résultat.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">  4)  Matrice de confusion : Prend en entrées le répertoire d’images ainsi que le répertoire de résultat “GFD” associé. Teste le taux de reconnaissance des images avec une matrice de confusion. on a en diagonale de la matrice le nombre d’images reconnue par classe, sur le côté droit de la matrice, le taux de reconnaissance par classes en pourcentage. Et en dessous de la matrice, le taux de reconnaissance globale de la méthode GFD.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Aide = QtWidgets.QWidget()
    ui = Ui_Aide()
    ui.setupUi(Aide)
    Aide.show()
    sys.exit(app.exec_())
