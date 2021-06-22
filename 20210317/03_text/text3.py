# -*- coding: utf-8 -*-
'''
Psychopy Draw Text Demo

2016 April 12 by EC

'''

from psychopy import visual, core, event


fontnames =[u'標楷體', u'微軟正黑體',u'華康魏碑體',u'華康楷書體注音']
fontnames2 =[u'DFKai-SB', u'Microsoft JhengHei',u'DFWeiBei-B5',u'DFKaiChuIn']
fontfiles =['','',['../fonts/weibai.ttc'], ['../fonts/hwakaiphone.ttc']]


#create a window to draw in
win = visual.Window((1080.0,160.0),pos=(50,50),winType='pyglet',allowGUI=None,monitor='testMonitor', units ='deg', screen=0)

text=[]
for i in range(len(fontnames)):
	text.append(visual.TextStim(win,text=fontnames[i],
		pos=(0, 0),
		color=[1.0,1,1],
		units='deg',
		ori=0, height = 1.0,
		font=fontnames2[i],
		fontFiles=fontfiles[i]))


for i in range(len(fontnames)):
	text[i].draw()
	win.flip()
	core.wait(1)

win.close()
