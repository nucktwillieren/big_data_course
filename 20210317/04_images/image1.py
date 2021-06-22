# -*- coding:utf-8 -*-

from psychopy import visual, event
import numpy as np
import glob

win = visual.Window([1024,768],monitor='mylaptop57cm', units='pix')

pngpath = '../pngs/'
pf1 = glob.glob(pngpath+'*.png')

myStim = visual.ImageStim(win, image = pf1[1], size=200)

myStim.autoDraw = True
win.flip()

event.waitKeys()

#change color
myStim.color+=[1,1,1]
#myStim.draw()
win.flip()
event.waitKeys()

myStim.color-=[1,1,1] #change the color back
#myStim.draw()
win.flip()
event.waitKeys()

myStim.contrast = -0.5 #reverse contrast
win.flip()
event.waitKeys()

myStim.contrast = 1 #recover contrast
myStim.mask = 'gauss'
myStim.maskParam = {'sd':100}
win.flip()
event.waitKeys()





win.close()