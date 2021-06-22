from psychopy import visual, monitors, event, core
from win32api import GetSystemMetrics
from utils import *


def main():
    win = visual.Window((GetSystemMetrics(0), GetSystemMetrics(
        1)), units="pix", fullscr=True, color=(1, 1, 1))
    win_width_px, win_height_px = GetSystemMetrics(0), GetSystemMetrics(1)

    mouse = event.Mouse()

    grids = create_grids(win_width_px, win_height_px,
                         8, -win_width_px/2, -win_height_px/2)

    text = visual.TextStim(win, text="", pos=(0, 0), color=[
                           -1, -1, 1], units='pix', ori=0, height=50)

    block_map = {}
    coder_map = {}

    for index, posi in enumerate(grids):
        block = visual.Rect(win, pos=posi, units="pix", width=win_width_px/4,
                            height=win_height_px/2, fillColor=[-1, 1, 1], lineColor=[-1, -1, 1])
        coder = visual.TextStim(win, text=str(index), pos=posi, color=[
            -1, -1, 1], units='pix', ori=0, height=20)

        block_map[index] = block
        coder_map[index] = coder

        block.draw()
        coder.draw()

    text.draw()

    win.flip()

    while 1:
        # is the mouse inside the shape (hovering over it)?
        for key, block in block_map.items():
            if block.contains(mouse):
                text.text = str(key)
            if mouse.isPressedIn(block):
                # press a rect to exit
                win.close()
                return
            block.draw()
            coder_map[key].draw()

        text.draw()
        win.flip()


if __name__ == '__main__':
    main()
