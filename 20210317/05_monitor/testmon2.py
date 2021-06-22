# -*- coding:utf-8 -*-
'''
Use different monitor profiles to draw the same figure
'''

from psychopy import visual, monitors, core, event
import numpy as np
from win32api import GetSystemMetrics

sdim = np.array([GetSystemMetrics(0), GetSystemMetrics(1)])
scen = sdim / 2 #screen center
wdim = sdim / 4

#load parameters of two different monitors
mon1 = monitors.Monitor('mylaptop57cm') 
mon2 = monitors.Monitor('mylaptop114cm') 

#create a window based on each of the monitor settings, respectively
win1 = visual.Window(wdim, monitor=mon1, 
		units = 'deg',
		pos=(scen[0]-wdim[0], scen[1]))

win2 = visual.Window(wdim, monitor=mon2, 
		units = 'deg',
		pos=(scen[0]+wdim[0]/2, scen[1]))

#load the same image on these two windows, see how they differ
img1 = visual.ImageStim(win1, image='../jpgs/fist.jpg', size=2)
img1.draw()
win1.flip()

img2 = visual.ImageStim(win2, image='../jpgs/fist.jpg', size=2)
img2.draw()
win2.flip()
#core.wait(2)
event.waitKeys()

win1.close()
win2.close()
