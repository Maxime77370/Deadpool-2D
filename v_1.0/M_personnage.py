import time, pygame, math
from pygame.locals import *

def init_personage():
	debut = time.time()
	animation_perso_respiration_1 = pygame.image.load ("texture/annimation/personage_respiration/frame_1.png").convert()
	animation_perso_respiration_2 = pygame.image.load ("texture/annimation/personage_respiration/frame_2.png").convert()
	animation_perso_coure_1 = pygame.image.load ("texture/annimation/personage_coure/frame_1.png").convert()
	animation_perso_coure_2 = pygame.image.load ("texture/annimation/personage_coure/frame_2.png").convert()
	animation_perso_coure_3 = pygame.image.load ("texture/annimation/personage_coure/frame_3.png").convert()
	animation_perso_coure_4 = pygame.image.load ("texture/annimation/personage_coure/frame_4.png").convert()
	fin = time.time()
	temps = fin - debut
	print("personage pre_chargement :", temps)
	return [animation_perso_respiration_1, animation_perso_respiration_2,animation_perso_coure_1, animation_perso_coure_2, animation_perso_coure_3, animation_perso_coure_4]

def annimation_personage(personnage_vitesse, personnage_x, personnage_y, annimation_nb, t,animation_perso_respiration_1,animation_perso_respiration_2,animation_perso_coure_1,animation_perso_coure_2,animation_perso_coure_3,animation_perso_coure_4,fenetre_x,fenetre_y,def_ecran,fenetre):

	if annimation_nb == 1:

		animation_perso_respiration_dimension_x = 25*((fenetre_x[def_ecran]/fenetre_y[def_ecran])*4)
		animation_perso_respiration_dimension_y = 48*((fenetre_x[def_ecran]/fenetre_y[def_ecran])*4)

		if t >= 0 and t < 30:
			personage = animation_perso_respiration_1
			personage.set_colorkey(pygame.Color("white"))
			personage = pygame.transform.scale (personage,(int(animation_perso_respiration_dimension_x),int(animation_perso_respiration_dimension_y)))
		elif t >= 30 and t <= 60:
			personage = animation_perso_respiration_2
			personage.set_colorkey(pygame.Color("white"))
			personage = pygame.transform.scale (personage,(int(animation_perso_respiration_dimension_x),int(animation_perso_respiration_dimension_y)))

	if annimation_nb == 2:

		animation_perso_coure_dimension_x = 29*((fenetre_x[def_ecran]/fenetre_y[def_ecran])*4)
		animation_perso_coure_dimension_y = 47*((fenetre_x[def_ecran]/fenetre_y[def_ecran])*4)

		if t >= 0 and t < 15:
			personage = animation_perso_coure_1
			personage.set_colorkey(pygame.Color("white"))
			personage = pygame.transform.scale (personage,(int(animation_perso_coure_dimension_x),int(animation_perso_coure_dimension_y)))
		if t >= 15 and t < 30:
			personage = animation_perso_coure_2
			personage.set_colorkey(pygame.Color("white"))
			personage = pygame.transform.scale (personage,(int(animation_perso_coure_dimension_x),int(animation_perso_coure_dimension_y)))
		if t >= 30 and t < 45:
			personage = animation_perso_coure_3
			personage.set_colorkey(pygame.Color("white"))
			personage = pygame.transform.scale (personage,(int(animation_perso_coure_dimension_x),int(animation_perso_coure_dimension_y)))
		if t >= 45 and t <= 60:
			personage = animation_perso_coure_4
			personage.set_colorkey(pygame.Color("white"))
			personage = pygame.transform.scale (personage,(int(animation_perso_coure_dimension_x),int(animation_perso_coure_dimension_y)))

	position_personnage = personage.get_rect(topleft = (personnage_x,personnage_y))

	if position_personnage.bottom < fenetre_y[def_ecran]:
		personnage_y += 4

	fenetre.blit(personage, position_personnage)
	return personage


