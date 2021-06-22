# -*- coding:utf-8 -*-
'''
2016.04.13 Created by EC

Demonstrate all kinds of built-in textures and masks
'''
from psychopy import visual, core
import numpy as np

win = visual.Window([1024,768],units = 'pix')
wdim = win.size

gs = win.size/8 #grating size (pixel)

fac = np.array([
	[[1.5,1.5],[0.5,1.5],[-0.5,1.5],[-1.5,1.5]],
	[[1.5,0],[0.5,0],[-0.5,0],[-1.5,0]],
	[[1.5,-1.5],[0.5,-1.5],[-0.5,-1.5],[-1.5,-1.5]]
	])
mypos =  fac*gs #determine the central position of each patch 
 
myStim=[]
mytex = ['sin','saw','sqr','tri']
myMask = ['gauss','raisedCos','circle']

#show 4 different texture
for j in range(len(myMask)):
	for i in range(len(mytex)):
			myStim.append(visual.GratingStim(win, 
					tex=mytex[i], mask=myMask[j], pos=mypos[j,i,],
					sf = .05, size=gs))
for j in range(len(myMask)):
	for i in range(len(mytex)):
		myStim[(j-1)*4+i-1].draw()

win.flip()
core.wait(5)

win.close()