# -*- coding:utf-8 -*-

from psychopy import visual, core
import numpy as np

win = visual.Window([1024,768],units = 'pix')
wdim = win.size

gs = win.size/4 #grating size (pixel)

fac = np.array([[1,1],[1,-1],[-1,-1],[-1,1]])
mypos =  fac*gs #determine the central position of each patch 
 
myStim=[]
mytex = ['sin','saw','sqr','tri']

#show 4 different texture
for i in range(len(mytex)):
	myStim.append(visual.GratingStim(win, 
					tex=mytex[i], mask=None, pos=mypos[i],
					sf = .01, size=gs))

for i in range(len(mytex)):
	myStim[i].draw()

win.flip()
core.wait(3)

win.close()