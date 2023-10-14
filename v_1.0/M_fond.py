import time, pygame
from pygame.locals import *
def init_fond(fenetre_x, fenetre_y, def_ecran, fenetre):
	debut = time.time()
	fond = pygame.image.load ("texture/fond_1.png").convert() #chergement du fond de la fenetre
	fond = pygame.transform.scale (fond,(fenetre_x[def_ecran],fenetre_y[def_ecran])) #redimensionné le fond
	fenetre.blit(fond, (0,0)) #afficher le fond
	fin = time.time()
	temps = fin - debut
	print("creation fond :", temps)
	return fond
