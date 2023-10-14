    ################################################
    #marche sous version python 3.2 et pygame 1.9.2#
    ################################################

    #Version de test
    
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygame, sys, os, math, time, datetime #importation des fonction nécessaire
from pygame.locals import *

pygame.init() #initialisation de pygame
clock = pygame.time.Clock()

annimation_nb = 1
personnage_vitesse_par_s = 0
first_frame_chute = True
debut_chute = 0
saut = False

debut_demarage = time.time()

from M_fenetre import * 
fenetre_set = init_fenetre()
fenetre = fenetre_set[0]
fenetre_x = fenetre_set[1]
fenetre_y = fenetre_set[2]
def_ecran = fenetre_set[3]

from M_fond import *
fond = init_fond(fenetre_x, fenetre_y, def_ecran, fenetre)

position_fond = (0,0)

from M_personnage import *
personnage_set = init_personnage()
animation_perso_respiration_1 = personnage_set[0]
animation_perso_respiration_2 = personnage_set[1]
animation_perso_coure_1 = personnage_set[2]
animation_perso_coure_2 = personnage_set[3]
animation_perso_coure_3 = personnage_set[4]
animation_perso_coure_4 = personnage_set[5]

from M_clock import *
fps = 100
personnage_x = fenetre_x[def_ecran] / 2
personnage_y = fenetre_y[def_ecran] / 2 
position_personnage = (personnage_x, personnage_y)
t_reel = 0

from M_music import *
init_music()

from M_text import *
text_set = init_text()
text_font = text_set[0]
fps_font = text_set[1]


from M_quit import *

pygame.display.flip() #rafraichir l'ecrans

while True:

	debut_boucle = time.time()

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
				personnage_vitesse_par_s = fenetre_x[def_ecran] / 2
				annimation_nb = 2
			elif event.key == K_a:
				personnage_vitesse_par_s = -fenetre_x[def_ecran] / 2
				annimation_nb = 2
			elif event.key == K_SPACE:
				saut  = True
		elif event.type == KEYUP:
			if event.key == K_d:
				personnage_vitesse_par_s = 0
				annimation_nb = 1
			elif event.key == K_a:
				personnage_vitesse_par_s = 0
				annimation_nb = 1

	annimation_personnage_var = annimation_personnage(personnage_vitesse_par_s, personnage_x, personnage_y,annimation_nb,t_reel,animation_perso_respiration_1,animation_perso_respiration_2,animation_perso_coure_1,animation_perso_coure_2,animation_perso_coure_3,animation_perso_coure_4,fenetre_x,fenetre_y,def_ecran)
	personnage = annimation_personnage_var[0]

	if personnage_vitesse_par_s > 0:
		if position_personnage.right <= fenetre_x[def_ecran] * 3/4 :
			personnage_x += 1 / fps * personnage_vitesse_par_s
		if position_personnage.right >= fenetre_x[def_ecran] * 3/4 :
			position_fond = annimation_fond(fond,personnage_vitesse_par_s,fenetre_x,fenetre_y,def_ecran,fenetre, fps)
	if personnage_vitesse_par_s < 0:
		if position_personnage.left >= fenetre_x[def_ecran] * 1/4 :
			personnage_x += 1 / fps * personnage_vitesse_par_s
		if position_personnage.left <= fenetre_x[def_ecran] * 1/4 :
			position_fond = annimation_fond(fond,personnage_vitesse_par_s,fenetre_x,fenetre_y,def_ecran,fenetre, fps)

	position_personnage_var = mouvement_personnage(saut, debut_chute, first_frame_chute, personnage, position_personnage, personnage_x, personnage_y, fenetre_y, fenetre_x, def_ecran, fps)
	personnage_y = position_personnage_var[0]
	personnage_x = position_personnage_var[1]
	position_personnage = position_personnage_var[2]
	first_frame_chute = position_personnage_var[3]
	debut_chute = position_personnage_var[4]
	saut = position_personnage_var[5]

	actu_fond(fond,position_fond,fenetre)
	actu_personnage(personnage, position_personnage, fenetre)
	fps_affichage(fps, text_font, fenetre_x, fenetre_y, def_ecran, fenetre)

	pygame.display.flip() #rafraichir l'ecrans

	fin_boucle = time.time()

	fps_var = frame_par_seconde(debut_boucle, fin_boucle)
	fps = fps_var[0]
	t_reel = fps_var[1]