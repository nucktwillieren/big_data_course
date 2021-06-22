# -*- coding:utf-8 -*-

from psychopy import visual, core, event

win = visual.Window(size=(100,100), 
	fullscr=True, color=[1,0,0])
#core.wait(1)
event.waitKeys()
win.close()
