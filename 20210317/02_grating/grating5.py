# -*- coding:utf-8 -*-

from psychopy import visual, core, event
import numpy as np

win = visual.Window(units='deg', monitor='mylaptop57cm')

myTex = ['../jpgs/dislike.jpg','jpgs/fist.jpg']
myMask =[]
myMask.append(np.array([
		[ 1, 0,-1, 0],
		[ 0,-1, 0, 1],
		[-1, 0, 1, 0],
		[ 0, 1, 0,-1]
        ]))
		
myMask.append(np.array([
		[ 1, 0,-1, 0] ]))
myMask.append(np.array([[1,0,-1,0]]).transpose())		
myStim=[]
for i in range(3):
	myStim.append(visual.GratingStim(win, tex=myTex[0],
		mask=myMask[i]
		, size=1))
myPos=[(-0.75,0), (0,0), (0.75,0)]
for i in range(3):
	myStim[i].setPos(myPos[i])
	myStim[i].draw()
	
	
win.flip()

event.waitKeys()

win.close()