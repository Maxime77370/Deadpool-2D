#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time, pygame, math
from pygame.locals import *

def init_icon():
	debut = time.time()
	icon_chargement = pygame.image.load ("texture/image_1.png").convert() #rechargé l'image de chargement
	fin = time.time()
	temps = fin - debut
	print("text pre_chargement :", temps)
	return icon_chargement

def chargement(t, i, marche, icon_chargement, fenetre_x, fenetre_y, def_ecran, fenetre):
        ##### chagement taille de l'image de chargement #####
    if marche == True:
        taille_icon_chargement = ((fenetre_x[def_ecran] - fenetre_y[def_ecran])*0.15) + ((fenetre_x[def_ecran] - fenetre_y[def_ecran])*0.05) * math.sin(t * 1 * 3.1415926 / 60) #utilisation de la function sinus
        icon_chargement.set_colorkey(pygame.Color("white")) #rendre trensparent le blanc de l'image de chargement
        icon_chargement = pygame.transform.scale (icon_chargement,(int(taille_icon_chargement),int(taille_icon_chargement))) #redimensionné l'image de chargement grace a la function sinus
        icon_chargement_rect = icon_chargement.get_rect(center=(fenetre_x[def_ecran]/2,fenetre_y[def_ecran]/4*3))
        fenetre.blit(icon_chargement, icon_chargement_rect) #afficher l'image de chargement
        chargement_fin = False


    elif marche == False :
        taille_icon_chargement = ((fenetre_x[def_ecran] - fenetre_y[def_ecran])*0.15)-i
        icon_chargement.set_colorkey(pygame.Color("white")) #rendre trensparent le blanc de l'image de chargement
        icon_chargement = pygame.transform.scale (icon_chargement,(int(taille_icon_chargement),int(taille_icon_chargement)))
        icon_chargement_rect = icon_chargement.get_rect(center=(fenetre_x[def_ecran]/2,fenetre_y[def_ecran]/4*3))
        fenetre.blit(icon_chargement, icon_chargement_rect) #afficher l'image de chargement
        chargement_fin = True

    return chargement_fin