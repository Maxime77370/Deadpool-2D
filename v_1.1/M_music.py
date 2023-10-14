#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time, pygame
from pygame.locals import *

musique_volume = 0.5 #volume du son entre 0 et 1

def init_music():
	debut = time.time()
	pygame.mixer.init(48000, -16, 1, 1024)
	pygame.mixer.music.load("Musique/Rock-It.mp3") #chergement de la musique de chargement
	pygame.mixer.music.set_volume(musique_volume)
	pygame.mixer.music.play(loops=-1, start=0.0) #joue musique de chargement
	fin = time.time()
	temps = fin - debut
	print("musique pre_chargement :", temps)