#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time, pygame, os
from pygame.locals import *

def init_text():
	debut = time.time()
	text_font = pygame.font.SysFont("Courier New", 72)
	fps_font = pygame.font.SysFont("Courier New", 72)
	fin = time.time()
	temps = fin - debut
	print("text pre_chargement :", temps)
	return text_font, fps_font

def text_affichage(text_nb, text_font, fenetre_x, fenetre_y, def_ecran, fenetre):

    text = ['Bienvenue dans le debut du jeu.','Ce jeu consiste a rien :)','Fin de char']
    text_aff = text_font.render(text[text_nb], True, (255, 0, 0))
    fenetre.blit(text_aff,(fenetre_x[def_ecran]/2 - text_aff.get_width() // 2, fenetre_y[def_ecran]/4 - text_aff.get_height() // 2))

def fps_affichage(fps, fps_font, fenetre_x, fenetre_y, def_ecran, fenetre):

	test = round(fps,1)
	fps_aff = fps_font.render('%d' % test, True, (255, 255, 255))
	fenetre.blit(fps_aff,(0, 0))