#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time, os

fps_max = 120
t_reel = 0

def frame_par_seconde(debut_boucle, fin_boucle):

	global t_reel
	t_loop = fin_boucle - debut_boucle

	if t_loop <= 1 / fps_max:

		t_sleep = (1 / fps_max) - t_loop
		time.sleep(t_sleep)
		fps = 1 / (t_loop + t_sleep)

	else:
		t_sleep = 0
		fps = 1 / t_loop

	if t_reel <= 1:
		t_reel += 1 / fps
	else :
		t_reel = 0

	return fps, t_reel