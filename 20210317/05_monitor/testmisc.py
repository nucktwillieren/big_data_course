# -*- coding:utf-8 -*-
'''
Use different monitor profiles to draw the same figure
'''

from psychopy import visual, monitors, core, misc
import numpy as np



#load parameters of two different monitors
mon1 = monitors.Monitor('mylaptop57cm') 
mon2 = monitors.Monitor('mylaptop114cm') 

mon1param = [misc.cm2pix(1,mon1), misc.cm2deg(1,mon1),
 misc.deg2cm(1, mon1), misc.deg2pix(1, mon1),
 misc.pix2cm(1, mon1), misc.pix2deg(1, mon1)]
 
mon2param = [misc.cm2pix(1,mon2), misc.cm2deg(1,mon2),
 misc.deg2cm(1, mon2), misc.deg2pix(1, mon2),
 misc.pix2cm(1, mon2), misc.pix2deg(1, mon2)]
 
