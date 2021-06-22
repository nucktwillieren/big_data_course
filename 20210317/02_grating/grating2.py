# -*- coding:utf-8 -*-

from psychopy import visual, core, event
import numpy as np

win = visual.Window(units = 'pix')

myTex1 = np.random.rand(8,8)
myStim1 = visual.GratingStim(win, tex=myTex1, mask='gauss', size=200, pos=(-200,0))

myTex2 = np.random.random((8,8, 4))
myStim2 = visual.GratingStim(win, tex=myTex2, mask=None, size=200, pos =(200,0))


myStim1.draw()
myStim2.draw()
win.flip()

event.waitKeys()

win.close()