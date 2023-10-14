#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time, pygame, sys, os, datetime, math
from pygame.locals import *

def quit(temps_de_marche):
    print("temps de marche :", temps_de_marche) #ecrir le temps de marche du programe
    date = datetime.datetime.now()
    fileR = open("save/fichier.txt","r")
    text = fileR.read()
    fileR.close()
    fileW = open("save/fichier.txt","w")
    fileW.write("\n" + str(date) + "\n" + "Temps de marche : " + str(temps_de_marche) + "\n" + text)
    fileW.close()
    pygame.quit() #desinitalisation de pygame
    sys.exit() #desinitalisation de sys