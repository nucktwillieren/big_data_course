# -*- coding: utf-8 -*-
'''
Psychopy Draw Text Demo

2016 April 12 by EC

'''

from psychopy import visual, core, event
import sys



#create a window to draw in
win = visual.Window((480.0,160.0),pos=(50,50),winType='pyglet',
					allowGUI=None,monitor='testMonitor',
					units ='deg', screen=0)


text = visual.TextStim(win,text='Hello World!',
		pos=(0, 0),
		color=[1.0,1,1],
		units='deg',
		ori=0, height = 2.0,
		font='Times New Roman')


text.draw()
win.flip()
core.wait(1)

text = visual.TextStim(win,text=u'大家好!',
		pos=(0, 0),
		color=[1.0,1,1],
		units='deg',
		ori=0, height = 2.0,
		font='Microsoft JhengHei')
		#font ='DFKai-SB')
		#look in C:/Windows/Fonts 


text.draw()
win.flip()
core.wait(1)



win.close()
