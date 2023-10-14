    ################################################
    #marche sous version python 3.2 et pygame 1.9.2#
    ###############################################

    #Version de test

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygame, sys, os, math, time, datetime #importation des fonction nécessaire
from pygame.locals import *

#toute variable
clock = pygame.time.Clock()
t = 0
i = 0
d = 0
annimation_nb = 1
chargement_fin = False
temps = 0

pygame.init() #initialisation de pygame

debut_demarage = time.time()

from M_fenetre import * 
fenetre_set = init_fenetre()
fenetre = fenetre_set[0]
fenetre_x = fenetre_set[1]
fenetre_y = fenetre_set[2]
def_ecran = fenetre_set[3]

from M_fond import *
fond = init_fond(fenetre_x, fenetre_y, def_ecran, fenetre)

from M_icon import *
icon_chargement = init_icon()

from M_music import *
init_music()

from M_text import *
text_set = init_text()
text_font = text_set[0]
fps_font = text_set[1]

from M_quit import *

from M_personnage import *
personnage_set = init_personnage()
animation_perso_respiration_1 = personnage_set[0]
animation_perso_respiration_2 = personnage_set[1]
animation_perso_coure_1 = personnage_set[2]
animation_perso_coure_2 = personnage_set[3]
animation_perso_coure_3 = personnage_set[4]
animation_perso_coure_4 = personnage_set[5]

pygame.display.flip() #rafraichir l'ecrans

while True : #boucle principale
	clock.tick(60) #nombre de rafraichissement par seconde
	for event in pygame.event.get(): #activation de la detection de touche
	    if event.type == QUIT : #si la vous appuyer sur le bouton de fermetur de fenetre alors
	        fin_demarage = time.time() 
	        temps_de_marche = fin_demarage - debut_demarage
	        quit(temps_de_marche)
	    if event.type == KEYDOWN and event.key == K_ESCAPE:
	        fin_demarage = time.time() 
	        temps_de_marche = fin_demarage - debut_demarage 
	        quit(temps_de_marche)
	    if chargement_fin == True:
	    	if event.type == KEYUP and event.key == K_d:
	    		print("ok")
	    		

	if t == 60 :
	    temps += 1
	    t = 0
	else :
	    t += 1

	fenetre.blit(fond, (0,0)) #afficher le fond
	if temps < 10 :
	    chargement_fin = chargement(t, 0, True, icon_chargement, fenetre_x, fenetre_y, def_ecran, fenetre)
	elif temps >=2 and i <= ((fenetre_x[def_ecran] - fenetre_y[def_ecran])*0.15-1):
	    i += 3
	    chargement_fin = chargement(t, i, False, icon_chargement, fenetre_x, fenetre_y, def_ecran, fenetre)


	if temps < 5 and temps > 0 :
		text_nb = 0
		text_affichage(text_nb, text_font, fenetre_x, fenetre_y, def_ecran, fenetre)
	elif temps > 4 and temps < 8:
		text_nb = 1
		text_affichage(text_nb, text_font, fenetre_x, fenetre_y, def_ecran, fenetre)

	pygame.display.flip() #rafraichir l'ecrans
