    ################################################
    #marche sous version python 3.2 et pygame 1.9.2#
    ################################################

    #Version de test

import pygame, sys, os, math, time, datetime #importation des fonction nécessairerafraichir
from pygame.locals import *

#toute variable
clock = pygame.time.Clock()
t = 0
i = 0
chargement_fin = False
temps = 0

pygame.mixer.init(48000, -16, 1, 1024)
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
text_font = init_text()

from M_quit import *


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

	if t == 60 :
	    temps += 1
	    t = 0
	else :
	    t += 1

	fenetre.blit(fond, (0,0)) #afficher le fond
	if temps < 10 :
	    chargement(t, 0, True, icon_chargement, fenetre_x, fenetre_y, def_ecran, fenetre)
	elif temps >=2 and i <= ((fenetre_x[def_ecran] - fenetre_y[def_ecran])*0.15-1):
	    i += 3
	    chargement(t, i, False, icon_chargement, fenetre_x, fenetre_y, def_ecran, fenetre)

	if temps < 5 and temps > 0 :
		text_nb = 0
		text_affichage(text_nb, text_font, fenetre_x, fenetre_y, def_ecran, fenetre)
	elif temps > 4 and temps < 8:
		text_nb = 1
		text_affichage(text_nb, text_font, fenetre_x, fenetre_y, def_ecran, fenetre)

	elif chargement_fin == True :
		text_nb = 2 
		text_affichage(text_nb, text_font, fenetre_x, fenetre_y, def_ecran, fenetre)
		perso_debut()

	pygame.display.flip() #rafraichir l'ecrans
