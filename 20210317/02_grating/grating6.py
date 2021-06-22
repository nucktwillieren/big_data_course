# -*- coding:utf-8 -*-

from psychopy import visual, core, event
import numpy as np

win = visual.Window([1024,768],units = 'pix')

myStim=[]
mytex = ['sin','saw','sqr','tri']
mypos = [(-256,-256),(256,-256),(-256,256),(256,256)]
#show 4 different texture
for i in range(len(mytex)):
	myStim.append(visual.GratingStim(win, 
					tex=mytex[i], mask=None, pos=mypos[i],
					sf = .01, size=256))

for i in range(len(mytex)):
	myStim[i].draw()

win.flip()
event.waitKeys()
win.close()