**RAPPORT DE PROJET**


**Groupe L2L1: Reconnaissance de formes à partir de descripteurs de Fourier Génériques étendus**

**_Projet réalisé par_**

Alexandre Braure 

Alexandre Oganezov 

Thanh Cong Vo 

Hengsheng Zhao 

**_Projet encadré par_**

Laurent Wendling 


# I. INTRODUCTION

## **1.** Cadre du projet

Pour le quatrième semestre de la licence informatique de l’université Paris Descartes, et dans le cadre de l’UE Projet. Il nous a été demandé de réaliser un projet d’informatique. Cette UE a pour objectif de nous faire travailler, dans une situation similaire aux milieux professionnels. De nous mettre face aux différents problèmes qui peuvent être rencontrés. Comme les difficultés dû à la répartition du travail dans un groupe ou même la mise en commun de celui-ci. Nous avons également dû remettre des documents permettant de garder une trace écrite, des contraintes et fonctionnalités convenues au préalable avec les commanditaires du produit (logiciel, application, etc…), comme dans un cadre professionnel. Ainsi que les documents structurant pour un regard extérieur le travail réalisé, les moyens mis en œuvre, et le matériel nécessaire à son bon fonctionnement, tout cela dans un temps imparti. Le projet qui nous a été attribué est le projet “L2L” qui a pour titre et pour sujet “Reconnaissance de formes à partir de descripteurs de Fourier Génériques étendus”. 

La description de formes est l'un des éléments clés de la description du contenu de l'image pour le traitement d'image. Le traitement des images à commencer dès les années 1950 en physique des particules, pour détecter des trajectoires particulièrement complexes des particules à partir d’enregistrement vidéo. La plupart des descripteurs de forme existants, dépendent généralement de l'application dans laquelle ils sont utilisés, ou ne sont pas robustes (ne fonctionne que sur peu de cas), ce qui les rend indésirables pour la description de forme générique. Un descripteur de Fourier générique (GFD) est proposé pour surmonter les inconvénients des techniques de représentation de forme existantes. Cette méthode a été mise en place par la thèse du docteur Zhang. Le descripteur de forme proposé est dérivé en appliquant une transformée de Fourier bidimensionnelle sur une image de forme échantillonnée à trame polaire. Le descripteur de forme acquis est indépendant de l'application et robuste. Les résultats expérimentaux montrent que le GFD proposé surpasse les descripteurs de forme communs basés sur les contours et les régions.

## **2. L’équipe**

Notre équipe de projet est composée de personnalités complémentaires provenant du même cursus :  



Braure Alexandre

ii06383@etu.parisdescartes.fr

 

  Oganezov Alexandre

  ii09140@etu.parisdescartes.fr

##      



  

  VO Thanh Cong

   ii12348@etu.parisdescartes.fr



Zhao Hengsheng 

ik01517@etu.parisdescartes.fr

## **3. Motivation**

En tant qu’étudiants en licence d’informatique, certains projets nous ont plus interpellés que d’autres. Cela a été le cas pour ce sujet, la reconnaissance de forme est un des piliers du traitement d’images. C’est un domaine qui est important et très étudiées aussi bien par des instituts de recherches que par des entreprises, en vue de la multitude d’applications et du champs interdisciplinaire que ces méthodes apportent (reconnaissance facial, voiture intelligente, etc.). Le traitement d’images est très lié dans son développement actuel à l'intelligence artificielle, généralement en apprentissage autonome par système de récompense avec différents outils comme le deep learning. Toute l'effervescence autour de ces nouvelles technologie, nous as rendu très curieux à l’approche de ce projet de reconnaissance de formes.   



# II. OBJECTIF ET CONTRAINTES DU PROJET

## 1. Les objectifs techniques

 

Étant pour le moment dans le cadre d’un projet universitaire limité en moyens et en temps, nous avons décidés de maîtriser au maximum le sujet qui est le nôtre. Ils nous a été demandés d’appliquer une méthodes existantes, reconnue par la thèse du docteur Zhang.  Notre but est de proposer une application qui va permettre de donner de très bons résultats pour la reconnaissance de Logos ou de formes pleines. Mais également d’évaluer nos résultats et de rendre compte de la performance de notre logiciel et des différentes améliorations que l’on pourrait lui apporter dans un contexte différent. En sélectionnant les solutions à développer parmi toutes les possibilités permises. Ainsi, nous avons projeté dans un premier temps de mettre en place un environnement Python sur nos ordinateurs, car il nous a parus comme étant le langage le plus adapté au outils mathématiques qui sont utilisés pour la reconnaissance de formes. Mais également pour le développement du logiciel, pour la partie graphique. L’accord nous a été données par notre encadrant le docteur Wendling, car il travail avec des étudiant lors de thèse sur le sujet avec ce langage.

## 2. Les contraintes

Le projet a débuté le lundi 20 janvier 2020 et s’achève le lundi 18 mai 2020 avec la remise des derniers documents, soit un peu plus de quatre mois. Nous avons eu une contrainte qui n'était pas prévus par nos encadrants et qui nous à malheureusement tous affecter. Je parle bien sûr du COVID-19 et de la période de confinement qui en a découlé. En effet la mise en commun du travail en a été plus difficile. La communication au sein du groupe a été aussi plus compliqué chacun ayant plus de contraintes personnel, nos réunions manquait parfois quelques membres, mais nous ne nous sommes pas laisser abattre.

Afin de terminer ce projet ambitieux à temps, il a été important pour nous, de correctement gérer notre travail ainsi que sa répartition au sein du groupe. Pour cela nous avons utilisés les outils de gestion adéquats, pour nous tenir à jours et au courant de l’avancement de chacun. Dans cette optique, nous avons utilisés des outils autant présents dans le domaine universitaire que dans le monde du travail, et qui faisait parties des consignes à respecter. La forge qui est un espace alloué à tous les membres du groupe ou nous avons eu la possibilité, d'émettre des requêtes au uns et autres à travers des demandes. D’avoir un suivi des rendez-vous avec notre encadrant grâce aux compte-rendu hebdomadaire et donc dans le même temps de l'avancement du projet et des tâches à accomplir. Également le wiki qui contient les informations relatives aux membres du groupe. La forge est aussi un passerelle entre notre groupe et les professeurs qui s’occupe du suivi et de l’évaluation de notre projet, en effet nous y avons déposés tous les documents qui ont été nécessaire à la bonne réalisation de ce projet.

- Le cahier des charges
- Le cahier de recette 
- Le plan de développement
- La conception détaillée
- Le manuel d’installation
- Le manuel d’utilisation
- La documentation interne du code
- Le plan de tests

Mais également le SVN, c’est l'abréviation de subversion, qui est un système de contrôle de version open source qui utilise la gestion efficace du système de gestion des branches. Qui nous as également permis de travailler de façon organisée, avec un système de version pour nos codes respectifs. Le SVN comme la forge a aussi eu pour but d’être une passerelle entre nous et nos professeurs, car il y est stockée tous nos codes ainsi que la version final de notre projet qui as dû être déposée le dimanche 3 mai à minuit au plus tard. 

						# 

# **III. GESTION DU PROJET**

## **1. La planification de projet et les outils de gestion**

### **a.** Cahier des charges

Décrivant toutes les conditions attachées à l'exécution du projet, le cahier des charges nous a permis dans un premier temps, de définir le contexte, les enjeux, les objectifs techniques ainsi que les livrables et les axes de développement envisagés. En organisant nos idées, nous avons pu vérifier l'accord et la faisabilité de notre projet.

### **b. Diagramme GANTT**

Le diagramme de GANTT est un outil efficace utilisant des données brutes telles que les dates de début et de fin et les durées de chacune des tâches afin de générer une visualisation de l'avancement du projet. Il donne une vision globale des tâches à réaliser, responsabilités et ressources associées, de l’idée à la mise en service, en passant par l’analyse des besoins, l’étude des faisabilité, conception fonctionnelle, spécialisations, implémentation et enfin, tests. Il est également possible d’organiser une gestion des ressources, disponibilité, coûts, etc.

FIGURE 1 - DIAGRAMME GANTT

## 2. Organisation générale 

L'organisation du travail est la première préoccupation de toute l'équipe. Il est vrai que tout le monde ne se connait pas. Il a donc fallu se rencontrer pour la distribution. Nous avons dû nous connecter via Internet.

Ainsi, après nous être réunis, nous avons partagé nos horaires afin de trouver des moments où tous les membres du groupe pourraient se réunir et travailler ensemble.

Dès la première rencontre avec l'encadrant, les jours de l'entretien sont fixés. Ainsi, nous avions notre réunion hebdomadaire tous les lundis après-midi de 14h à 14h30. Sauf pour l'épidémie, à partir du 15 mars, nous avons changés l'heure de notre réunion à 14 heures tous les vendredis après-midi sur la plateforme skype.

Au cours des trois premières semaines, nous avons discutés des premiers et deuxièmes éléments du projet, respectivement le travail du cahier des charges et du cahier de recettes.

 La quatrième semaine est le début de la phase de développement, chaque jeudi après-midi de 17 à 19 heures et le lundi après-midi, nous nous réunissons toujours pour parler du travail qui a été fait et du travail à faire. À l'approche du premier examen, notre calendrier a été adapté pour répondre aux besoins de chacun. Cependant, tous les membres du groupe se réunissent chaque lundi pour faire un compte rendu avant et après la réunion.

Les semaines 6 à 10 étaient des semaines de développement, et en raison de l'épidémie, nous avons eu tout le temps nécessaire pour allouer du temps de développement.

En semaine 11, nous devions nous réunir les lundi, mardi, jeudi et vendredi sur Whatsapp pour générer des fichiers .exe afin d'intégrer le projet.

Enfin, le compte rendu de chaque réunion, qui documente les éléments les plus importants de chaque réunion, a été soumis à temps.

## 3. Technologies choisies

Nous pouvons choisir la technologie que nous utilisons. De plus, afin de pouvoir choisir la bonne technologie, une étude de marché a été réalisée et trois langages de programmation ont été étudiés. En votant, nous avons finalement choisi Python3.7 + PYQT5 pour travailler.

### **Python** 

Python est un langage de programmation informatique multiplateforme. Et un langage de script de haut niveau qui combine l'explication, la compréhension, l'interactivité et l'orientation objet. Conçu à l'origine pour être utilisé pour écrire des scripts d'automatisation (shells), au fur et à mesure que les versions étaient mises à jour et que de nouvelles fonctionnalités étaient ajoutées au langage, il était de plus en plus utilisé pour des projets autonomes de grande envergure.

**C/C++**

Le langage C a été introduit au début des années 1970. La langue C a été officiellement publiée en 1978 par les Laboratoires Bell de l'American Telephone and Telegraph Company (AT&T). Il est également co-auteur du célèbre livre "THE C PROGRAMMING LANGUAGE" de B.W. Kernighan et D.M. Ritchie. Souvent appelé simplement K&R, certains l'appellent aussi la norme K&R. Cependant, le K&R n'a pas défini de langage C standard complet, et l'American National Standards Institute a ensuite développé une norme de langage C basée sur celui-ci, publiée en 1983. Il est communément appelé ANSI C.

Le C++ est un héritage du langage C, qui peut être utilisé pour la programmation procédurale et la programmation basée sur des objets, ainsi que pour la programmation orientée objet, y compris l'héritage et le polymorphisme, et le C++ est bon pour la programmation orientée objet et la programmation basée sur des processus.

### PYQT5

PyQt est une implémentation en langage Python du framework Qt, développée par Riverbank Computing, et est l'une des plus puissantes bibliothèques d'interface graphique disponibles.

### Forge 

Le terme Forge fait référence à un environnement web constitué d'un ensemble d'outils de collaboration et de génie logiciel pour le développement de logiciels collaboratifs et distribués.

### SVN

SVN est l'abréviation de subversion, qui est un système de contrôle de version open source qui utilise la gestion efficace du système de gestion des branches, en bref, il est utilisé par plusieurs personnes pour développer le même projet, pour réaliser le partage des ressources, pour atteindre la gestion centralisée ultime.

## 4. Répartition des tâches

L'attribution des tâches a commencé par une planification des tâches à effectuer et nous avons commencé par une liste des modules dont nous avons eu besoin.

Ensuite, nous avons fait un diagramme de flux entre les modules. Pour avoir une perspective sur tout ce qui doit être réalisées. Enfin, nous les avons classés par ordres d'importance. Il est vrai que certains modules doivent être mis en œuvre pour qu'un autre module soit mis en œuvre afin que l'ensemble du produit fonctionne bien.

La répartition des tâches s'est effectué tout d'abord par une planification des tâches à réaliser, nous avions fait une première liste de modules dont nous avons eu besoin.

Chaque semaine, un chef de projet est désigné afin de rédiger le compte rendu de la réunion avec l’encadrant. Le chef de projet doit envoyer les documents demandés par l’encadrant au fil des semaines et doit aussi s’assurer le fonctionnement, l’efficacité et la coordination du groupe afin de bien réaliser le projet et préparer la prochaine réunion hebdomadaire. L’encadrant aide les membres du projet mais joue le rôle de client à la fois. 

En effet, il fait des remarques pertinentes lorsqu'un élément ne va pas dans le projet (codes, design, rédaction de document), sa présence et son aide sa fondamentale pour la réalisation du projet. Tous les membres du groupe ont des rôles polyvalents, il n’y a pas de “rôles” approprié à chaque personne mais plutôt une répartition de tâches qui change chaque semaine après chaque réunion.

FIGURE 2 - DIAGRAMME DE FLUX

# 

# 

FIGURE 3 - RÉPARTITION DU TRAVAIL DE DÉVELOPPEMENT



FIGURE 4 - TEMPS PASSÉ SUR CHAQUE PARTIE DU PROJET

# **Les deux graphiques ci-dessous représente le temps passée sur les différentes partis du code source, et des méthodes réalisés pour chaque membre du groupe. Ainsi que la répartitions du temps tout au long du projet. En effet ils nous a paru important de mettre ces graphiques dans notre rapport, car ils représentent de façon assez précise, l’investissement de chacun dans le projet. Et les parties qui nous ont pris plus de temps que d’autres et cela de façon assez contre intuitifs. Comme par exemple le développement qui nous as pris un moindre temps (30%), par rapport à ce que l’ont avaient pu s’imaginer.**    

# 

# I**V. DÉVELOPPEMENT DE L'APPLICATION**  

## **1. Interface**

FIGURE 5 - ARBORESCENCE DE L'APPLICATION

Après avoir lancé notre application, un affichage d’accueil apparaîtra : 2 boutons principaux sont Démarrer et Quitter. A ne pas manquer est un bouton qui permet donner des informations sur l'application ainsi que les membres de notre équipe. 

      

FIGURE 6 - MENU D’ACCUEIL 

La fenêtre d'accueil s'affiche après que l'utilisateur ait lancé l'application

Bouton **Démarrer** : Permet aux utilisateurs d'utiliser les modules de l’application.

Bouton **Quitter** : Permet à l'utilisateur de quitter l'application.

Une nouvelle fenêtre apparaîtra si le bouton sélectionné est **Démarrer.** Elle affiche une liste de modules de l’application que l’utilisateur peut utiliser.

  

FIGURE 7 - MENU MÉTHODE

                                               

Les boutons sont également les méthodes de l'application mentionnées en suite. Indispensable avec le bouton en bas à droite de l'écran, le bouton **Aide** permet d’afficher les informations nécessaires à l’utilisation de l’application.



FIGURE 8 - MENU INFORMATIONS

## 2. Calcul du GFD

Dès que l'utilisateur sélectionne cette méthode, l'application demandera à l'utilisateur de choisir un répertoire pour stocker les fichiers au format gfd une fois cette méthode terminée.

Deux requis pour saisir les valeurs de _radian et _angle_ par l'utilisateur : 

##  

FIGURE 9 - CHOIX DE L’ANGLE ET DU RADIAN                                   

Après avoir terminé cette méthode, il enregistrera automatiquement les fichiers dans le répertoire GFD.     

## 3. Comparaison d’images 

Une fenêtre d'affichage permet aux utilisateurs de sélectionner 2 fichiers au format .gfd à comparer.

## 

FIGURE 10 -RÉSULTAT DE LA COMPARAISON ENTRE 2 IMAGES

Ci-dessus, l'interface de l'application a terminé cette méthode, vous pouvez voir que sur la gauche de l'écran est un histogramme de 2 images. En outre, la droite est le résultat de la distance, la pourcentage similarité, et conclut que les deux images sélectionnées ont la même classe ou non.

## 4. Retrieval

Cette méthode, demande à l’utilisateur le choix d'une image pour effectuer la méthode du Retrieval. 

Après avoir sélectionné l'image souhaitée, l'utilisateur doit saisir le nombre d’images qu’il veut afficher en résultat de requête et une condition requise pour que la valeur saisie ne dépasse pas 18. 

## 

FIGURE 11 - CHOIX DU NOMBRE DE REQUÊTE (RETRIEVAL)

 FIGURE 12 -Résultat Retrieval

Les images jugées les plus similaires à l'image sélectionnée seront affichées sur l'interface de l’application. Les résultats indispensables de la distance et du pourcentage de différence de chaque image, seront également affichés sous l'image.

## 5. Matrice de confusion

## 

FIGURE 13 - MATRICE DE CONFUSION

La matrice de confusion nous permet d’évaluer nos résultats et la qualité de la méthode GFD pour la description des images, pour une base choisie.

## 

## 6. Aspect légale

FIGURE 14 - MENTIONS LÉGALE

Nous avons choisi pour garder une cohérence avec l’UE “droit de l’informatique”, de nous servir d’images et de polices libre de droit. Car cela nous semble important de respecter les lois en vigueur concernant le copyright et la propriété individuel. Comme par exemple le logo de notre application qui est un logo libre de droit. Ce qui as également influencer le choix de notre licence “GNU”. 

# **V. BILAN DU PROJET**

## **1.** **Apports du projet**

Toute l'effervescence autour de ces domaines liés à notre sujet, nous as d’autant plus permis de vivre ce projet, comme un apprentissage permanent, tout au long de nos recherches. 

Cela a été pour nous un excellent moyen de nous initier et de mieux appréhender la façon dont est représentée une image dans un ordinateur comme la couleur ou même les images vectorielles. Les transformations nécessaires à son traitement (mise à niveau de gris, transformées de Fourier, normalisation, linéarisation d’une matrice), les outils d'évaluation de la qualité de nos résultats comme la matrice de confusion mais nous reviendrons sur ces points par la suite. Il nous as été très.

### a. **Compétences techniques**

Ce projet nous a permis d’avoir une expérience nouvelle, nous avons appris un nouveau langage, le Python. De plus, ce même langage était notre outil pour savoir comment créer une application. Que ce soit de la conception simple à la finalisation. Nous avons également appris à utiliser un logiciel de virtualisation pour visualiser le code au fur et à mesure. Nous avons appris à effectuer des tests après l'écriture du code pour vérifier s'il n'y a pas de bugs et que tout fonctionne comme prévu. De plus, nous avons appris ce qu'est SVN et comment l'utiliser à bon escient pour mener à bien le projet.

### 

### b. **Compétences en management**	

Etant donné les nombreuses contraintes que nous avions dû faire face, nous avons appris à travailler en groupe, c’est-à-dire à travailler en coordination de façon à répartir les tâches afin d’être plus efficace. Le fait de travailler en groupe de manière coordonné nous a permis d’exploiter les capacités de chacun et de créer des liens. De ce fait, cela nous prépare de manière évidente au monde du travail car le fait de communiquer ensemble nous a donné́ un aperçu de ce qui pourrait nous attendre par la suite. Le titre de “chef de projet” a permis à chacun des membres du groupes à gérer à son tour la préparation et l’animation et animer les réunions. Il devait également coordonner le travail d’équipe dans la semaine. Travailler en groupe a permis une répartition plus équilibrée du travail, et une avancée plus rapide. Nous avons appris à nous aider les uns et les autres. Cependant nous avons rencontré́ plusieurs difficultés notamment avec l’apprentissage d’un nouveau langage. La charge de travail pour le projet est conséquente. Nous avons appris à être autonome, curieux et gérer nos problèmes nous-mêmes.

### c. **Apports personnels**

**Braure Alexandre**

Le projet que nous avons réalisé était mon troisième choix derrière les deux autres sujets sur le thème de l’image. Cela a été pour moi un réel enrichissement de me confronter à des problématiques aussi bien techniques que scientifiques. J’ai notamment ouvert les yeux sur la multitudes de solutions possible pour un problème, même si il nous paraît très spécifique, et du nombre colossale de communautés et références qui traite de ces sujets. J’ai vraiment été agréablement surpris des progrès que j’ai réalisé dans la lecture de papier scientifique comme des thèses mais surtout dans le travail et la vision que j’en avais. C’était pour moi le premier travail en groupe conséquent que j’ai eu à réaliser, et on ne peut pas dire que je sois quelqu’un de très organisé dans la vie de tous les jours. Mais le faite de travailler en groupe avec des contraintes m’a fait prendre conscience de l'efficacité et de la dynamique qu’engendre le travail d’équipe. D’autant plus avec ce groupe car j’y est vraiment constater des camarades investis et préoccupés par le groupe, ces membres, et ce que ce projet représente, tout cela malgré nos divergences de points de vue par moments.     

**Oganezov Alexandre**

Conformément à mes intérêts, l'idée de créer une application de reconnaissance de formes a immédiatement éveillé ma curiosité. Au cours de ce projet, j'ai eu l'opportunité de travailler en équipe ainsi que d'utiliser de nombreuses connaissances acquises tout au long de ma scolarité. Ce sont des points importants, car j'ai pu élargir mes connaissances dans le domaine technique, à la fois en effectuant mes tâches individuelles mais aussi grâce à l'échange en groupe. De plus, il est évident pour moi que la gestion de l'équipe était l’un des points les plus importante du projet car ce dernier a permis le développement et la production de résultats.

**VO Thanh Cong** 

Bien que ce ne soit pas le sujet que j'ai choisi depuis le début, mais quand je suis arrivé à l'heure actuelle, j'ai appris beaucoup de choses. C'est aussi mon premier projet donc au début j'ai rencontré certains de difficultés.

Je me souviens que j'avais lu un livre qui disait: “Si vous voulez devenir un vrai programmeur, vous devez essayer n'importe quel sujet dans n'importe quel domaine, même si ce n'est pas votre point fort”.

En effet, ce sujet est le premier défi que j'ai essayé. Grâce à cette UE-PROJET DE PROGRAMMATION, j'ai pu explorer de nouveaux aspecten spécialisé informatique que je n'avais jamais connus. Plus important encore, j'ai appris la façon à travailler en équipe, à résoudre les problèmes et à gérer le planning en groupe. Les membres du groupe sont très gentils et j'ai beaucoup appris d’eux.

Soit dit en passant, je voudrais remercier l'encadrant enthousiaste qui m'a aidé et les autres membres du groupe.

**Zhao Hengsheng**

Pour moi, bien que ce projet n'ait pas été mon premier choix, Mais par contre il m'a beaucoup aidé à planifier mon avenir. J'ai appris à travailler en équipe, à équilibrer la répartition des tâches, à la rechercher des informations, à lire des documents officiels. Bien que le premier projet n'ait pas été très intéressant, il y a encore beaucoup à faire, mais il nous a fait prendre conscience que nous ne sommes pas aussi bons que les autres et qu'il y a encore beaucoup à apprendre. Mais surtout, j'ai constitué un groupe de compagnons particulièrement doués qui peuvent aller de pair dans le voyage d'apprentissage à venir.

## 2. Difficultés rencontrées

La première difficulté de ce projet est que nous devons apprendre un nouveau langage. Pour Python, nous avons dû apprendre les bases, étape par étape, en cherchant des informations sur Internet. Sélectionnez différentes bibliothèques en fonction des besoins. La documentation officielle, les forums et les blogs sont les principales ressources que nous avons utilisées. Par exemple pour OpenCV nous nous sommes servis de StackOverflow, Opencv.org, YouTube, CSDN (forum informatique Chinois). Chaque bibliothèque possède son propre ensemble de choses qui peuvent rendre le développement beaucoup moins difficile.

Deuxièmement, pour des raisons de force majeure, nous connaissons en 2020 une épidémie qui n'a pas été observée depuis des décennies, c'est pourquoi le gouvernement a demandé à l’université de fermer à partir du 15 mars 2020. Nous ne pouvions donc pas discuter du projet à l'université. Mais nous avons très vite trouvés des solutions. Si un membre a des problèmes avec le code, nous utilisons le partage d'écran et du contrôle à distance sur Zoom, nous utilisons Skype si nous avons un rendez-vous avec notre encadrant, et nous discutons des petits problèmes quotidiens et sur les distributions des tâches sur WhatsApp.

# 

# **VI. RÉFÉRENCES**											

- Le cahier des charges
- Le cahier de recette
- Le manuel d’utilisation
- Le manuel d’installation
- Les comptes-rendus
- Le code source sur le _SVN_		
- Le plan des tests	
- La conception détaillée 
 	

# 

# **VII. BIBLIOGRAPHIE**		

Python. **Python 3.8.3 documentation**. [en ligne] 

Disponible sur : [https://docs.python.org/3/](https://docs.python.org/3/) (Consulté le 02/02/2020)

Python. **Introduction aux interfaces graphiques en Python avec Qt 5 et PyQt5.** [en ligne ]
Disponible sur [https://courspython.com/interfaces.html](https://courspython.com/interfaces.html) (Consulté le 17/03/2020)

Qt Designer. **Qt Designer Manual.** [en ligne]

Disponible sur [https://doc.qt.io/qt-5/qtdesigner-manual.html](https://doc.qt.io/qt-5/qtdesigner-manual.html) ( Consulté le 20/03/2020)

Freelogodesign. **L’outil de logos le plus utilisé.** [en ligne]

Disponible sur : [https://fr.freelogodesign.org/](https://fr.freelogodesign.org/) (Consulté le 10/03/2020)

Canva. **Color theory and calculator**. [en ligne] 

Disponible sur : [https://www.canva.com/colors/color-wheel/](https://www.canva.com/colors/color-wheel/) (Consulté le 12/03/2020)

Pycharm. **L'EDI Python pour développeurs professionnels.** [en ligne]

Disponible sur : [https://www.jetbrains.com/fr-fr/pycharm/](https://www.jetbrains.com/fr-fr/pycharm/) (Consulté le 15/03/2020)

                               

GNU. **Licences - Projet GNU - Free software foundation** [en ligne]

Disponible sur [https://www.gnu.org/licenses/licenses.html](https://www.gnu.org/licenses/licenses.html) (Consulté le 25/03/220)

Wikipédia . **Confusion matrix - Wikipédia** [en ligne]

Disponible sur [https://en.wikipedia.org/wiki/Confusion_matrix](https://en.wikipedia.org/wiki/Confusion_matrix) ( Consulté le 30/03/2020)

+++

# VII**. REMERCIEMENT**

Nos remerciements vont d'une part à notre encadrant de projet M. Wendling Laurent, pour nous avoir apporté son temps et son expérience en tant que professionnel, il a notamment pu nous expliquer en termes simples les attentes d'une application scientifique. Et nous a guider en étant toujours attentif à nos demandes vers un résultat final très satisfaisant. Également pour sa réactivité de réponse qui a su nous mettre en confiance et nous faire respecter nos échéances. Enfin, nous tenons également à remercier M. Janiszek David, pour la chance qu'il nous a offerte avec cette unité d'enseignement qui s'est révélée incroyablement instructive. Nous avions des doutes, quelques incertitudes concernant l'environnement professionnel, nous en avons désormais beaucoup moins.

