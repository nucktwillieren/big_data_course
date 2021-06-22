# -*- coding:utf-8 -*-

from psychopy import visual, core, event
import numpy as np

win = visual.Window(color='black', units='pix')

myTex = np.array([
        [ 1, 0, 1, 0.5]
        ])


		
#myStim = visual.GratingStim(win, tex=myTex, mask=None, size=256)
#myStim = visual.GratingStim(win, tex=myTex, mask=None, size=64, color=[1, 1, 0])
myStim = visual.GratingStim(win, tex=myTex.transpose(), mask=None, size=100)


myStim.draw()
win.flip()

#core.wait(1)
event.waitKeys()

win.close()