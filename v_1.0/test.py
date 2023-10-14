    ################################################
    #marche sous version python 3.2 et pygame 1.9.2#
    ################################################

    #Version de test

import pygame, sys, os, math, time, datetime #importation des fonction nécessaire
from pygame.locals import *

pygame.init() #initialisation de pygame
clock = pygame.time.Clock()

t = 0
i = 0
d = 0

personnage_x = 0
personnage_y = 0

annimation_nb = 1
personnage_vitesse = 0

debut_demarage = time.time()

from M_fenetre import * 
fenetre_set = init_fenetre()
fenetre = fenetre_set[0]
fenetre_x = fenetre_set[1]
fenetre_y = fenetre_set[2]
def_ecran = fenetre_set[3]

from M_fond import *
fond = init_fond(fenetre_x, fenetre_y, def_ecran, fenetre)

from M_personnage import *
personage_set = init_personage()
animation_perso_respiration_1 = personage_set[0]
animation_perso_respiration_2 = personage_set[1]
animation_perso_coure_1 = personage_set[2]
animation_perso_coure_2 = personage_set[3]
animation_perso_coure_3 = personage_set[4]
animation_perso_coure_4 = personage_set[5]

pygame.display.flip() #rafraichir l'ecrans

while True:
	clock.tick(60)
	for event in pygame.event.get(): #activation de la detection de touche
	    if event.type == QUIT : #si la vous appuyer sur le bouton de fermetur de fenetre alors
	        fin_demarage = time.time() 
	        temps_de_marche = fin_demarage - debut_demarage
	        quit(temps_de_marche)
	    elif event.type == KEYDOWN:
	        if event.key == K_ESCAPE:
	            fin_demarage = time.time() 
	            temps_de_marche = fin_demarage - debut_demarage 
	            quit(temps_de_marche)
	        elif event.key == K_d:
	            personnage_vitesse = 8
	            annimation_nb = 2
	        elif event.key == K_a:
	            personnage_vitesse = -8
	            annimation_nb = 2
	    elif event.type == KEYUP:
	        if event.key == K_d:
	            personnage_vitesse = 0
	            annimation_nb = 1
	        elif event.key == K_a:
	            personnage_vitesse = 0
	            annimation_nb = 1

	personnage_x += personnage_vitesse

	fenetre.blit(fond, (0,0)) #afficher le fond
	if t == 60 :
	    t = 0
	else :
	    t += 1



	personage = annimation_personage(personnage_vitesse, personnage_x, personnage_y,annimation_nb,t,animation_perso_respiration_1,animation_perso_respiration_2,animation_perso_coure_1,animation_perso_coure_2,animation_perso_coure_3,animation_perso_coure_4,fenetre_x,fenetre_y,def_ecran,fenetre)
	pygame.display.flip() #rafraichir l'ecrans
