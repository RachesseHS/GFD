#author: VO Thanh Cong

import numpy as np
import os
import matplotlib.pyplot as plt

def get_vector(path):
    try:
        img = open(path, 'r').readlines()
        vector = np.array([float(x.strip()) for x in img])
    except IOError:  # Message d'erreur si lu un fichier d'erreur.
        vector = np.array([])
        print('Read file error!')
    return vector


def get_dist_2vector(vector1, vector2):  # Calculer la distance entre 2 vecteurs.
    vector = vector1 - vector2
    dist = np.linalg.norm(vector.tolist())  # via Euclid
    return dist


# def get_similarity_ratio(vector1, vector2):
#     min_arr = [min(vector1[i], vector2[i]) for i in range(len(vector1))]
#     max_arr = [max(vector1[i], vector2[i]) for i in range(len(vector1))]
#     return sum(min_arr) / sum(max_arr)

def compare_2image(img1, img2):  # Fonction de comparaison 2 images.
    dist = get_dist_2vector(img1, img2)  # Calculer la distance Euclid entre 2 images. Plus la image est la même, plus la distance est petite.
    simi_percent = 100 * (1 - dist)
    return simi_percent

def compare_2vector(vector1, vector2):
    vector = vector1 / vector2
    simi = np.average(vector) * 100
    return simi
#
IMAGES_PATH = './=GFD/'
# Lire les fichiers du répertoire.
filenames = os.listdir(IMAGES_PATH)
# Convertir tous fichiers en vecteur.
vectors = {}
for name in filenames:
    vector = get_vector(IMAGES_PATH + name)
    vectors[name] = vector

# Comparer l'image 1 avec le reste et tracez un graphique.
percents = []
for x in filenames:
    percents.append(compare_2vector(vectors['s01n001.gfd'], vectors[x]))
plt.plot([_ for _ in range(len(percents))], percents, 'bx')
plt.xlabel('Images')
plt.ylabel('Percents')
plt.show()

# # dist est un tableau (array) à 2 dimensions : [distance, 0/1] : 0 est identique, 1 est différent.
dists = []
for x in filenames:
     for y in filenames:
         if x[0:3] == y[0:3]:
             if x != y:
                 dists.append([get_dist_2vector(vectors[x], vectors[y]), 0])
         else:
             dists.append([get_dist_2vector(vectors[x], vectors[y]), 1])
#
dists = np.array(dists)
y = dists[:, -1]
#
# # simi est un tableau des mêmes éléments, diff est un tableau des éléments différents.
simi = dists[y == 0]
diff = dists[y == 1]
#
# # Tracer 600 échantillons en premier.
RANGE = 600
plt.plot(simi[:RANGE, 0], 'bx')
plt.plot(diff[:RANGE, 0], 'rx')
plt.show()

THRESHOLD = 0.4
#img1 = input("Image 1: ")  # Input file .gfd.
#img2 = input("Image 2: ")
img1 = "s02n001.gfd"
img2 = "s02n011.gfd"
vec1 = get_vector(IMAGES_PATH + img1)  # Obtenir un verteur basé sur image 1
vec2 = get_vector(IMAGES_PATH + img2)

dist = get_dist_2vector(vec1, vec2)
simi_percent = compare_2image(vec1, vec2)  # Ressemblance
if dist < THRESHOLD:
    print("Two image is same class")
else:
    print("Two image isn't same class")
print("The similarity of " + img1 + " and " + img2 + " is: " + str(round(simi_percent, 2)) + "%")