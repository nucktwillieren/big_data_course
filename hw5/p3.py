from psychopy import visual, core, event
from win32api import GetSystemMetrics

from p1 import set_all_device
import utils

import platform
import glob

text = "白日依山盡，黃河入海流；欲窮千里目，更上一層樓。"

if platform.system() == 'Windows':
	fpath = "C:\\Windows\\Fonts"
elif platform.system() == 'Darwin':
    fpath = '/Library/Fonts'

ff1 = glob.glob(fpath+'/*.ttf')
ff2 = glob.glob1(fpath,'*.ttf')

def main():
    # for ensure the monitor env loaded, we have to call the argparser again
    # ex: python p4.py -d d -r 100
    set_all_device()
    args = utils.add_device_parser()
    mon = utils.parse_to_monitor(args.device, args.distance)

    win = visual.Window((GetSystemMetrics(0), GetSystemMetrics(1)), monitor=mon, units="pix", fullscr=True, color=(1,1,1))
    win_width_px, win_height_px = GetSystemMetrics(0), GetSystemMetrics(1)
    height = 30
    padding = 5
    margin = 10
    block = height + padding + margin

    fade = 2/4

    for i in range(0, len(text), 6):
        t = visual.TextStim(win, text=text[i:i+6],pos=(0, block*2-block*i//6),color=[-1+i//6*fade,-1+i//6*fade,-1+i//6*fade],units='pix', ori=0, height=height, font=ff2[-(i//6)])
        print(t.font)
        t.draw()
    
    win.flip()

    event.waitKeys()
    win.close()

if __name__ == '__main__':
    main()
    