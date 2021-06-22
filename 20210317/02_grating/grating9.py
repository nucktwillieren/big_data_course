# -*- coding:utf-8 -*-

from psychopy import visual, event
import numpy as np

win = visual.Window([1024,768],monitor='mylaptop57cm')

myStim=[]
myStim.append(visual.GratingStim(win, tex='sin', 
			mask=None, size=(30,4), pos=(0, -5),
			sf=.5, units='deg'))
myStim.append(visual.GratingStim(win, tex='sin', 
			mask=None, size=(30,4), pos=(0, 0),
			sf=.5, units='degFlatPos'))
myStim.append(visual.GratingStim(win, tex='sin', 
			mask=None, size=(30,4), pos=(0, 5),
			sf=.5, units='degFlat'))

for sti in myStim:
	sti.draw()

win.flip()

event.waitKeys()

win.close()