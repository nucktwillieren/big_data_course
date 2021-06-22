# -*- coding:utf-8 -*-

from psychopy import visual, core, event
import numpy as np
import glob

ff1 = glob.glob('../jpgs/*.jpg')
ff2 = glob.glob1('../jpgs/','*.jpg')

win = visual.Window(units = 'pix')

myStim=[]
myPos=[]
for x in range(-350,350, 100):
	for y in range(-250,250,100):
		myPos.append((x,y))
i=0
for fjpg in ff1:
	myStim.append(visual.GratingStim(win, tex=fjpg, mask=None, size=100,pos = myPos[i]))
	i+=1


for i in range(len(ff1)):
	myStim[i].draw()
	
	
	
win.flip()
#core.wait(1)
event.waitKeys()
win.close()