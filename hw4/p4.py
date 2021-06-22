from psychopy import visual, core, event
import time
import random

def main():
    win = visual.Window([1024,768], units='pix', colorSpace='rgb')

    win.flip()

    image_file = "./school.png"

    posi_x = [450.0, -450.0]
    posi_y = [300.0, -300.0]


    myStim = visual.ImageStim(win, image=image_file, size=100)
    myStim.autoDraw = True

    for _ in range(2):
        # The random is not that random, 
        # so, sometimes, the position of logo will not be changed within the 2 times.
        myStim.pos = (posi_x[random.randint(0,1)], posi_y[random.randint(0,1)])
        win.flip()
        time.sleep(1)

    win.close()

if __name__ == '__main__':
    main()
    