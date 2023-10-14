#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time, pygame, os, sys
from pygame.locals import *

fond_x = 0
fond_y = 0
taille_map = 6

def init_fond(fenetre_x, fenetre_y, def_ecran, fenetre):
	debut = time.time()
	fond = pygame.image.load ("texture/fond_1.png").convert() #chergement du fond de la fenetre
	fond = pygame.transform.scale (fond,(fenetre_x[def_ecran] * taille_map,fenetre_y[def_ecran])) #redimensionné le fond
	fenetre.blit(fond, (fond_x,fond_y)) #afficher le fond
	fin = time.time()
	temps = fin - debut
	print("creation fond :", temps)
	return fond

def annimation_fond(fond,personnage_vitesse_par_s,fenetre_x,fenetre_y,def_ecran,fenetre, fps):

	global fond_x, fond_y

	fond_x += -1 / fps * personnage_vitesse_par_s

	position_fond = fond.get_rect(topleft = (fond_x,fond_y))

	actu_fond(fond,position_fond, fenetre)

	return position_fond

def actu_fond(fond,position_fond,fenetre):

	fenetre.blit(fond, position_fond)
