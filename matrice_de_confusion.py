# Author :  Braure Alexandre
# Assisted by: Alexandre Oganezov; Thanh Cong Vo; Hengsheng ZHAO
import easygui as gui
import math
import os.path
import numpy as np
import array
from tkinter import *

def FunctionMatrice():
	def Init():
		# Initialisation des variables
		distance=[]
		img=[]
		a = 0
		link = gui.diropenbox("Choisir le répertoire d'images")
		repertoire_img = os.listdir(link)
		nb_classes = int(len(repertoire_img)/11)
		nb_elmat = nb_classes*nb_classes
		matrice=[0 for j in range(0,nb_elmat)]
		repertoire_img.sort() # Tri la liste des fichiers des dossier d'images
		path = gui.diropenbox("choisir le dossier de résultats GFD")
		directory = os.listdir(path)
		for i in range(0,len(repertoire_img)): # Parcours le répertoire d'images
			imgc = repertoire_img[i]
			imgr = imgc[0:7] # Nom de l'image sans l'extension
			imgr2 = imgc[0:3] # Classe de l'image
			for file in directory:  # Parcours le répertoire choisi
				fic = path + '/' + file
				if os.path.isdir(fic):  # Si le choix n'est pas un répertoire
					continue
				else:
					nom_fic = os.path.splitext(os.path.basename(fic))[0]

				if(imgr==nom_fic):# Pour ne pas que l'image de référence ce compare a elle même
						continue
				else:

					img.append(nom_fic[0:3]) # Liste des signatures
					distance.append(distances(gfd(nom_fic), gfd(imgr))) # Liste des distances
			res = plus_proches(img, distance) # liste des images les plus proches

			imgp = res[0]
			imgp2 = int(imgp[2]) # Récupère le numéro de la classe de l'image la plus proches
			if(i%11==0 and a<nb_classes-1 and i != 0):
				a+=1
			if(i>=11):
				matrice[a*nb_classes+imgp2-1]+=1
			else:
				matrice[imgp2-1]+=1

		taux = taux_reco_classe(matrice, nb_classes) # liste des taux de reconnaissance par classes
		taux_g = str(taux_reco(matrice, nb_classes, repertoire_img)) # Taux de reconnaissance de la base
		affichage(matrice, img, taux, taux_g, repertoire_img)

	def gfd(nom_fic): # Récupère les valeurs des fichiers ".GFD" dans un vecteur
		with open("GFD/"+nom_fic+".gfd", "r") as fichier:
			lignes = fichier.read().splitlines()
			v = np.asarray(lignes, float)
		return v


	def distances(vector1, vector2):  # Calcule la distance entre deux vecteurs
		dist = ((np.sum(abs(vector1 - vector2)))/len(vector1))
		return dist


	def plus_proches(img, distance):
		d = dict(zip(img, distance)) # Associe les signatures des images à leur distance avec un dictionaire
		return [k for k, v in sorted(d.items(), key=lambda x: x[1])] # Retourne la liste triée par ordre croissant (des keys (signatures) associées aux distances)

	def taux_reco_classe(matrice, nb_classes): # Calcule le taux de reconnaissance par classes
		l=[]
		for i in range(0, nb_classes):
			if(i==9):
				l.append(round((matrice[(i*9)-1]/11)*100,3))
			else:
				l.append(round((matrice[(i*9)+i]/11)*100,3))
		return l

	def taux_reco(matrice, nb_classes, repertoire_img): # Calcule le taux de reconnaissance de la base d'images
		a=0
		for i in range(0, nb_classes):
			if(i==9):
				a+=matrice[(i*9)-1]
			else:
				a+=matrice[(i*9)+i]
		return round((a/len(repertoire_img))*100,3)

	def affichage(matrice, img, taux, taux_g, repertoire_img):
		x=0
		y=0
		a=0
		l=img[0:len(repertoire_img)]
		l.sort()
		root = Tk()
		root.title("Evaluation de la méthode utilisée : Matrice de confusion au premier plus proche voisin")
		can = Canvas(root, width=1275, height=700, bg="#50717b") # Configuration de la fenêtre
		can.pack()
		if(len(repertoire_img)==99): # Affichage pour la base de référence (sharvit1) de 99 images
			can.create_line(430,160,430,440)
			can.create_line(430,160,440,160)
			can.create_line(430,440,440,440)
			can.create_line(830,160,830,440)
			can.create_line(830,160,820,160)
			can.create_line(830,440,820,440)
			can.create_text(200,300, text="MATRICE (classe/classe) :")
			can.create_text(965,135, text="Taux de reconaissance par classe :")
			can.create_text(360,550, text="Taux de reconaissance des images (de la base) par la méthode des déscripteurs de Fourier génériques : ")
			can.create_text(740,550, text=taux_g+" %")
			for i in range(0, len(matrice)): # Affichage itératif des valeurs de la matrice
				if(i==0):
					y+=1
					can.create_text(450,150+(y*30), text=matrice[i])
				elif(y*9==i):
					x=0
					y+=1
					can.create_text(450,150+(y*30), text=matrice[i])
				else:
					x+=1
					can.create_text(450+(x*45),150+(y*30), text=matrice[i])
			y=0
			for i in range(0, len(taux)): # Affichage itératif des classes et des taux de reconnaissance
				y+=1
				can.create_text(890,150+(y*30), text=str(taux[i])+" %")
				can.create_text(400,150+(y*30), text=l[i*12])
				can.create_text(450+(a*45),135, text=l[i*12])
				a+=1
		else: # Affichage pour n'importe quelle base d'images
			can.create_text(360,650, text="Taux de reconaissance des images (de la base) par la méthode des déscripteurs de Fourier génériques : ")
			can.create_text(740,650, text=taux_g+" %")
			for i in range(0, len(matrice)): # Affichage itératif des valeurs de la matrice
				if(i==0):
					y+=1
					can.create_text(450,150+(y*30), text=matrice[i])
				elif(y*9==i):
					x=0
					y+=1
					can.create_text(450,150+(y*30), text=matrice[i])
				else:
					x+=1
					can.create_text(450+(x*45),150+(y*30), text=matrice[i])
		root.mainloop()
	Init()
