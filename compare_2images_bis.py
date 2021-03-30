#Author: Thanh Cong VO
# # Assisted by: Alexandre Oganezov, Braure Alexandre, Hengsheng ZHAO.

import easygui as gui
import os.path
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame

def FunctionCompare():

    IMAGES_PATH = './GFD/'
    THRESHOLD = 0.4


    def Init():
        img1_path = gui.fileopenbox("Choose image1 in .gfd format to compare")    # Sélectionne le chemin d'une image1(au format .gfd).
        img2_path = gui.fileopenbox("Choose image2 in .gfd format to compare")   # Sélectionne le chemin d'une image2(au format .gfd).
        img1_name = os.path.splitext(os.path.basename(img1_path))[0]  # Récupère le nom de l'image1 de référence.
        img2_name = os.path.splitext(os.path.basename(img2_path))[0]  # Récupère le nom de l'image2 de référence.

        # img1_name = 's01n005'
        # img2_name = 's08n004'

        vec1 = get_Image(IMAGES_PATH + img1_name + '.gfd')   # Accède au répertoire "IMAGES_PATH" pour obtenir le vecteur vec1 (en fonction du nom de l'image1 sélectionnée).
        vec2 = get_Image(IMAGES_PATH + img2_name + '.gfd')  # Accède au répertoire "IMAGES_PATH" pour obtenir le vecteur vec2.

        data2 = {'Length': [i for i in range(len(vec1))], 'Image1': vec1, 'Image2': vec2}  # Groupe des vecteurs vec1, vec2 en 1 objet.
        df2 = DataFrame(data2, columns=['Length', 'Image1', 'Image2'])  # Convertis les données de l'objet data2 en DataFrame pour pratique de tracer un histogramme.

        root = tk.Tk()    # root pour utiliser tkinter.

        # Construction d'un histogramme.
        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)   # Créer une zone pour tracer un histogramme.
        line2 = FigureCanvasTkAgg(figure2, root)   # Utilise FigureCanvasTkAgg pour afficher le histogramme sur root.
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2.plot(kind='line', x='Length', y='Image1', legend=True, ax=ax2, color='r', fontsize=10)   # Trace le histogramme du vecteur 1.
        df2.plot(kind='line', x='Length', y='Image2', legend=True, ax=ax2, color='b', fontsize=10)   # Trace le histogramme du vecteur 2.
        ax2.set_title('Histogram')  # Ajoute le titre du histogramme.

        # Affichage le résultat.
        t = tk.Text(root)   # Insére un texte sur root.
        t.pack()
        dist = get_dist_2Image(vec1, vec2)   # Calcule la distance entre 2 vecteurs vec1 et vec2. Grâce à une fonction get_dist_2Image ci-dessous.
        simi_percent = compare_2image(vec1, vec2)   # Calcul un pourcentage similaire.
        if dist < THRESHOLD:
            txt_result = "Result: Two image is same class\n"
        else:
            txt_result = "Result: Two image isn't same class\n"
        txt_similar = "The similarity of " + img1_name + " and " + img2_name + " is: " + str(round(simi_percent,2)) + "%\n "

        # Utilise une fonction t.insert() pour réprésenter le résultat (par un text) sur root.
        t.insert(tk.END, "Distance: " + str(round(dist, 2)) + "\n")  # Représentation le résultat de la distance.
        t.insert(tk.END, txt_similar)    # Repésentation la pourcentage de la similitude entre 2 images.
        t.insert(tk.END, txt_result)   # Conclusion 2 images de même classe ou non.

        root.mainloop()


    def get_Image(path):
        try:
            img = open(path, 'r').readlines()
            Image = np.array([float(x.strip()) for x in img])
        except IOError:   # Donne un message d'erreur en cas d'erreur de lecture du fichier.
            Image = np.array([])
            print('Read file error!')
        return Image


    def get_dist_2Image(Image1, Image2):  # Le calcul de la distance entre 2 vecteurs.
        Image = Image1 - Image2
        dist = np.linalg.norm(Image.tolist())  # via Euclid
        return dist


    def compare_2image(img1, img2):  # La fonction de comparaison entre 2 images.
        dist = get_dist_2Image(img1, img2)  # Calcule la distance Euclid entre 2 images. Plus une image est la même, plus la distance est petite.
        simi_percent = 100 * (1 - dist)
        return simi_percent


    Init()