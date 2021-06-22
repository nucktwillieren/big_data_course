from psychopy import visual, core, event
import time

def main():
    win = visual.Window(units='pix', colorSpace='rgb')

    win.flip()

    for i in range(2):
        win.color = (1,0,0)
        win.clearBuffer(color=True)
        win.flip()
        
        time.sleep(1)

        win.color = (0,1,0)
        win.clearBuffer(color=True)
        win.flip()

        time.sleep(1)

        win.color = (0,0,1)
        win.clearBuffer(color=True)
        win.flip()
        time.sleep(1)

    win.close()

if __name__ == '__main__':
    main()
    