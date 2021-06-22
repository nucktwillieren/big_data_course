from psychopy import visual, monitors, event, core
from win32api import GetSystemMetrics

from p1 import set_all_device
import utils

import numpy as np
import glob

def main():
    # for ensure the monitor env loaded, we have to call the argparser again
    # ex: python p4.py -d d -r 100
    set_all_device()
    args = utils.add_device_parser()
    mon = utils.parse_to_monitor(args.device, args.distance)

    win = visual.Window((GetSystemMetrics(0), GetSystemMetrics(1)), monitor=mon, units="pix", fullscr=True, color=(1,1,1))
    win_width_px, win_height_px = GetSystemMetrics(0), GetSystemMetrics(1)

    empty_block = visual.Rect(win, units="pix", width=win_width_px, height=win_height_px, fillColor=[1, 1, 1], lineColor=[1, 1, 1])
    img1 = visual.ImageStim(win, image="./1.png", size=(win_width_px, win_height_px), units="pix")
    #img1_size_x = img1.size[0]
    #img1_size_y = img1.size[1]
    #img1.size = [win_width_px / img1_size_x * img1_size_x, win_height_px / img1_size_y * img1_size_y]
    img2 = visual.ImageStim(win, image="./2.png", size=(win_width_px, win_height_px), units="pix")
    #img2_size_x = img2.size[0]
    #img2_size_y = img2.size[1]
    #img2.size = [win_width_px / img2_size_x * img2_size_x, win_height_px / img2_size_y * img2_size_y]
    for i in range(5):
        empty_block.draw()
        win.flip()
        core.wait(.1)

        img1.draw()
        win.flip()
        core.wait(1)    

        empty_block.draw()
        win.flip()
        core.wait(.1)

        img2.draw()
        win.flip()
        core.wait(1)

    win.close()

if __name__ == '__main__':
    main()
    