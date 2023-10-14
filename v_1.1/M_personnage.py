#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time, pygame, math
from pygame.locals import *

def init_personnage():
	debut = time.time()
	animation_perso_respiration_1 = pygame.image.load ("texture/annimation/personnage_respiration/frame_1.png").convert()
	animation_perso_respiration_2 = pygame.image.load ("texture/annimation/personnage_respiration/frame_2.png").convert()
	animation_perso_coure_1 = pygame.image.load ("texture/annimation/personnage_coure/frame_1.png").convert()
	animation_perso_coure_2 = pygame.image.load ("texture/annimation/personnage_coure/frame_2.png").convert()
	animation_perso_coure_3 = pygame.image.load ("texture/annimation/personnage_coure/frame_3.png").convert()
	animation_perso_coure_4 = pygame.image.load ("texture/annimation/personnage_coure/frame_4.png").convert()

	fin = time.time()
	temps = fin - debut
	print("personnage pre_chargement :", temps)
	return [animation_perso_respiration_1, animation_perso_respiration_2,animation_perso_coure_1, animation_perso_coure_2, animation_perso_coure_3, animation_perso_coure_4]

def annimation_personnage(personnage_vitesse_par_s, personnage_x, personnage_y,annimation_nb,t_reel,animation_perso_respiration_1,animation_perso_respiration_2,animation_perso_coure_1,animation_perso_coure_2,animation_perso_coure_3,animation_perso_coure_4,fenetre_x,fenetre_y,def_ecran,fenetre,fps):

	personnage_direction = 1

	if annimation_nb == 1:

		animation_perso_respiration_dimension_x = 25*((fenetre_x[def_ecran]/fenetre_y[def_ecran])*4)
		animation_perso_respiration_dimension_y = 48*((fenetre_x[def_ecran]/fenetre_y[def_ecran])*4)

		if t_reel >= 0 and t_reel < 0.5:
			personnage = animation_perso_respiration_1
			personnage.set_colorkey(pygame.Color("white"))
			personnage = pygame.transform.scale (personnage,(int(animation_perso_respiration_dimension_x),int(animation_perso_respiration_dimension_y)))
		elif t_reel >= 0.5 and t_reel <= 1:
			personnage = animation_perso_respiration_2
			personnage.set_colorkey(pygame.Color("white"))
			personnage = pygame.transform.scale (personnage,(int(animation_perso_respiration_dimension_x),int(animation_perso_respiration_dimension_y)))
		else:
			personnage = animation_perso_respiration_1
			personnage.set_colorkey(pygame.Color("white"))
			personnage = pygame.transform.scale (personnage,(int(animation_perso_respiration_dimension_x),int(animation_perso_respiration_dimension_y)))

	elif annimation_nb == 2:

		animation_perso_coure_dimension_x = 29*((fenetre_x[def_ecran]/fenetre_y[def_ecran])*4)
		animation_perso_coure_dimension_y = 47*((fenetre_x[def_ecran]/fenetre_y[def_ecran])*4)

		if t_reel >= 0 and t_reel < 0.25:
			personnage = animation_perso_coure_1
			personnage.set_colorkey(pygame.Color("white"))
			personnage = pygame.transform.scale (personnage,(int(animation_perso_coure_dimension_x),int(animation_perso_coure_dimension_y)))
		elif t_reel >= 0.25 and t_reel < 0.5:
			personnage = animation_perso_coure_2
			personnage.set_colorkey(pygame.Color("white"))
			personnage = pygame.transform.scale (personnage,(int(animation_perso_coure_dimension_x),int(animation_perso_coure_dimension_y)))
		elif t_reel >= 0.5 and t_reel < 0.75:
			personnage = animation_perso_coure_3
			personnage.set_colorkey(pygame.Color("white"))
			personnage = pygame.transform.scale (personnage,(int(animation_perso_coure_dimension_x),int(animation_perso_coure_dimension_y)))
		elif t_reel >= 0.75 and t_reel <= 1:
			personnage = animation_perso_coure_4
			personnage.set_colorkey(pygame.Color("white"))
			personnage = pygame.transform.scale (personnage,(int(animation_perso_coure_dimension_x),int(animation_perso_coure_dimension_y)))
		else:
			personnage = animation_perso_coure_1
			personnage.set_colorkey(pygame.Color("white"))
			personnage = pygame.transform.scale (personnage,(int(animation_perso_coure_dimension_x),int(animation_perso_coure_dimension_y)))

	if personnage_vitesse_par_s > 0:

		if personnage_direction == -1:

			personnage = pygame.transform.flip(personnage, False, False)
			personnage_direction = 1

	elif personnage_vitesse_par_s < 0:

		if personnage_direction == 1:

			personnage = pygame.transform.flip(personnage, True, False)
			personnage_direction = -1

	position_personnage = personnage.get_rect(topleft = (personnage_x,personnage_y))

	if position_personnage.bottom < fenetre_y[def_ecran]:
		personnage_y += fenetre_y[def_ecran] / 4 / fps

	return personnage, personnage_x, personnage_y, position_personnage

def actu_personnage(personnage, position_personnage, fenetre):

	 fenetre.blit(personnage, position_personnage)