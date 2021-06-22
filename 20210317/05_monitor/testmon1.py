# -*- coding:utf-8 -*-
'''
create mointor profiles
'''

from psychopy import visual, monitors
from win32api import GetSystemMetrics


#GetSystemMetrics(1) #monitor height


#create a new monitor profile named mylaptop57cm
mon1 = monitors.Monitor('mylaptop57cm') 
mon1.setDistance(57) #set the viewing distance to 57 cm
mon1.setWidth(47.5) #screen width in cm
#mon1.setSizePix(1024,768)
mon1.setSizePix((GetSystemMetrics(0),GetSystemMetrics(1))) #screen size in number of pixels
mon2 = monitors.Monitor('mylaptop114cm') 
mon2.setDistance(114) #set the viewing distance to 114 cm
mon2.setWidth(47.5) #screen width in cm
mon2.setSizePix((GetSystemMetrics(0),GetSystemMetrics(1))) #screen size in number of pixels

print(mon1.currentCalib)
print(mon2.currentCalib)

mon1.saveMon()
mon2.saveMon()