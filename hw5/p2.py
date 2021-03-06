from psychopy import visual, monitors, event
from win32api import GetSystemMetrics

from p1 import set_all_device
import utils

import numpy as np
import glob

def get_multiply(number):
    # This algorithm is to find how the grids can be generated by x, y 
    # For example, if we have 30 items that we have to arrange, 
    # generally, we will make a 5*6(x, y) grid system to put those items in the grids system.
    # Hence, we need this algorithm to find the x and y.
    # However, the returning results of this algorithm x is less than y.
    # In the most cases when we display the grids on the screen,
    # the x(width) is larger than y(height), so we can swap the x and y when we get the result.
    # Ex: y, x = get_multiply(30) -> y = 5, x = 6
    x, y = 1, 1
    for i in range(1, int(number**(1/2))+1):
        if number % i == 0:
            x = i
            y = number / i
    return int(x), int(y)

def create_grids(width, height, number, offset_x=0, offset_y=0, dimension=1):
    y, x = get_multiply(number)
    width_of_blocks = width / x
    height_of_blocks = height / y
    dis_to_center_of_blocks_x, dis_to_center_of_blocks_y = width_of_blocks / 2, height_of_blocks / 2

    grids = []

    cursor_y = -dis_to_center_of_blocks_y + offset_y
    for i in range(y):
        if dimension == 2:
            grids.append([])
        cursor_x = -dis_to_center_of_blocks_x + offset_x
        cursor_y += height_of_blocks
        for j in range(x):
            cursor_x += width_of_blocks
            if dimension == 2:
                grids[i].append([cursor_x, cursor_y])
            else:
                grids.append([cursor_x, cursor_y])

    return grids

def main():
    # for ensure the monitor env loaded, we have to call the argparser again
    # ex: python p2.py -d d -r 100
    set_all_device()
    args = utils.add_device_parser()
    mon = utils.parse_to_monitor(args.device, args.distance)
    jpgs = glob.glob("./jpgs/*.jpg")
    number = len(jpgs)

    win = visual.Window((GetSystemMetrics(0), GetSystemMetrics(1)), monitor=mon, units="pix", fullscr=True, color=(1,1,1))
    win_width_px, win_height_px = GetSystemMetrics(0), GetSystemMetrics(1)

    grids = create_grids(win_width_px, win_height_px , number, -win_width_px/2, -win_height_px/2)
    for jpg, posi in zip(jpgs, grids):
        img = visual.ImageStim(win, pos=posi, image=jpg, size=210, units="pix")
        print(jpg, posi)
        img.draw()

    win.flip()

    event.waitKeys()
    win.close()

if __name__ == '__main__':
    main()
    