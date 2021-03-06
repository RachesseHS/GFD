# Author :  Braure Alexandre

import easygui as gui
import math
import os.path
import numpy as np
import array
from tkinter import *

def FunctionRetrieval():
	def Init():
		# Initialisation des variables
		img=[]
		distance=[]
		resultat=[]
		d=[]
		path = gui.diropenbox("choisir le dossier de résultats GFD")
		directory = os.listdir(path) # Chemin du répertoire de résultats "GFD"
		link = gui.fileopenbox("Choisir l'image de référence")
		img_ref = os.path.splitext(os.path.basename(link))[0] # Récupère le nom de l'image de référence
		nb_img = gui.integerbox("Entrer le nombre d'images que vous voulez afficher en résultat de requête (18 au maximum)", "int ", 10, 1, 20)
		dir_img = os.path.dirname(link) # Chemin vers le répertoire d'images
		for file in directory:  # Parcour le répertoire choisi  #O(n)
			fic = path + '/' + file
			if os.path.isdir(fic):  # Si le choix n'est pas un répertoire
				continue
			else:
				nom_fic = os.path.splitext(os.path.basename(fic))[0]

				if(img_ref==nom_fic):# Pour ne pas que l'image de référence ce compare a elle même
					continue
				else:
					img.append(nom_fic+".pgm") # Liste des signatures
					distance.append(distances(gfd(nom_fic), gfd(img_ref))) # Liste des distances

		res = plus_proches_k(img, distance)
		resultat = res[0:nb_img]
		distance.sort()
		d = distance
		affichage(resultat, dir_img, d)


	def gfd(nom_fic): # Récupère les valeurs des fichiers ".gfd" ligne par ligne dans un vecteur
		with open("GFD/"+nom_fic+".gfd", "r") as fichier:
			lignes = fichier.read().splitlines()
			v = np.asarray(lignes, float)
		return v # Retourne le vecteur


	def distances(vector1, vector2): # Calcule la distance entre deux vecteurs
		dist = ((np.sum(abs(vector1 - vector2)))/len(vector1))
		return dist


	def plus_proches_k(img, distance):
		d = dict(zip(img, distance)) # Associe les signatures des images à leur distance avec un dictionaire
		return [k for k, v in sorted(d.items(), key=lambda x: x[1])] # Retourne la liste triée par ordre croissant (des keys (signatures) associées aux distances)

	def affichage(resultat, dir_img, d):
		a=0
		img=[]
		root = Tk()
		root.title("Les images les plus proches de l'image choisi avec leur distance à celle-ci")
		can = Canvas(root, width=1275, height=700, bg="#50717b") # Configuration de la fenêtre
		can.pack()
		os.chdir(dir_img) # Change le répertoire courant de l'utilisateur pour le chemin du répertoire d'images
		for i in range(0, len(resultat)): # Affichage itératif des images avec leur distance dans la fenêtre
			if(i==0):
				img.append(PhotoImage(file=resultat[i]))
				can.create_image(100,150, image=img[i])
				can.create_text(80,250, text="distance : ")
				can.create_text(150,250, text=round(d[i],5))
				can.create_text(160,270, text=str(round((d[i]*100),5))+"%")
			elif(i==6):
				a=0
				img.append(PhotoImage(file=resultat[i]))
				can.create_image(100,350, image=img[i])
				can.create_text(80,450, text="distance : ")
				can.create_text(150,450, text=round(d[i],5))
				can.create_text(160,470, text=str(round((d[i]*100),5))+"%")
			elif(i==12):
				a=0
				img.append(PhotoImage(file=resultat[i]))
				can.create_image(100,550, image=img[i])
				can.create_text(80,650, text="distance : ")
				can.create_text(150,650, text=round(d[i],5))
				can.create_text(160,670, text=str(round((d[i]*100),5))+"%")
			elif((i>6)and(i<12)):
				a+=1
				img.append(PhotoImage(file=resultat[i]))
				can.create_image(100+(a*210),350, image=img[i])
				can.create_text(80+(a*210),450, text="distance : ")
				can.create_text(150+(a*210),450, text=round(d[i],5))
				can.create_text(150+(a*210),470, text=str(round((d[i]*100),5))+"%")
			elif(i>12):
				a+=1
				img.append(PhotoImage(file=resultat[i]))
				can.create_image(100+(a*210),550, image=img[i])
				can.create_text(80+(a*210),650, text="distance : ")
				can.create_text(150+(a*210),650, text=round(d[i],5))
				can.create_text(150+(a*210),670, text=str(round((d[i]*100),5))+"%")
			else:
				a+=1
				img.append(PhotoImage(file=resultat[i]))
				can.create_image(100+(a*210),150, image=img[i])
				can.create_text(80+(a*210),250, text="distance : ")
				can.create_text(150+(a*210),250, text=round(d[i],5))
				can.create_text(150+(a*210),270, text=str(round((d[i]*100),5))+"%")
		root.mainloop()
	Init()

