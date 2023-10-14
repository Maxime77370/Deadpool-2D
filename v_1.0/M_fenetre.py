import time, pygame
from pygame.locals import *

fenetre_x = [800,1024,1152,1176,1280,1280,1280,1280,1360,1366,1440,1600,1600,1680,1768,1920,1920,1920,2560,2560] #liste de toute les definission ecran accepter
fenetre_y = [600,768,864,664,720,768,960,1024,768,768,900,900,1024,1050,992,1080,1200,1440,1440,1440]            #liste de toute les definission ecran accepter
def_ecran = 1 #choisir la definition de votre ecran entre 0 et 19

def init_fenetre():
	debut = time.time()
	fenetre = pygame.display.set_mode((fenetre_x[def_ecran],fenetre_y[def_ecran]), FULLSCREEN) #création d'une fenetre
	pygame.display.set_caption("chargement") #nommé la fenetre
	icone = pygame.image.load("texture/image_1.png").convert_alpha() #chargement un icone a la fenetre
	pygame.display.set_icon(icone) #afficher l'icone a la fenetre
	fin = time.time()
	temps = fin - debut
	print("creation fenetre :", temps)
	return [fenetre, fenetre_x, fenetre_y, def_ecran]