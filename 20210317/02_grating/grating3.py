# -*- coding:utf-8 -*-

from psychopy import visual, core, event
import numpy as np

win = visual.Window(units = 'pix')

myTex = ['../jpgs/dislike.jpg','../jpgs/fist.jpg']
myStim1 = visual.GratingStim(win, tex=myTex[0], mask=None, size=200, pos=(-200,0))
myStim2 = visual.GratingStim(win, tex=myTex[1], mask=None, size=100, pos=(200,0))


myStim1.draw()
myStim2.draw()
win.flip()

event.waitKeys()

win.close()