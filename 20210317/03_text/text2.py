# -*- coding: utf-8 -*-
'''
Psychopy Draw Text Demo

2016 April 12 by EC

'''

from psychopy import visual, core, event
import sys

import glob
import platform

if platform.system() == 'Windows':
	fpath = "C:\\Windows\\Fonts"
elif platform.system() == 'Darwin':
	fpath = '/Library/Fonts'
ff1 = glob.glob(fpath+'/*.ttf')
ff2 = glob.glob1(fpath,'*.ttf')



#create a window to draw in
win = visual.Window((1080.0,160.0),pos=(50,50),winType='pyglet',allowGUI=None,monitor='testMonitor', units ='deg', screen=0)

text=[]
for i in range(len(ff2)):					
	text.append(visual.TextStim(win,text=ff2[i][:-4],
		pos=(0, 0),
		color=[1.0,1,1],
		units='deg',
		ori=0, height = 2.0,
		font=ff2[i][:-4]))						

					
for i in range(len(ff2)):
	text[i].draw()
	win.flip()
	core.wait(1)

win.close()
						
