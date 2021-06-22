from psychopy import visual, monitors, event
from win32api import GetSystemMetrics
import numpy as np
import utils

# At home, normally, I develop by desktop computer, 
# so, alternatively, I design for both two size of dimensions of computers.
# Spec of My Desktop: https://www.displayspecifications.com/en/model/91fed8b
# Width: 59.7888cm Height: 33.6312cm
# Spec of My Laptop: https://www.lenovo.com/za/en/laptops/thinkpad/thinkpad-l-series/ThinkPad-L490/p/22TP2TBL490
# Width: 33.5cm Height: 23.5cm

def set_device(name, dis, width):
    mon = monitors.Monitor(name) 
    mon.setDistance(dis)
    mon.setWidth(width) 
    mon.setSizePix((GetSystemMetrics(0), GetSystemMetrics(1)))
    print(name, ": ", mon.currentCalib)
    mon.saveMon()

def set_all_device():
    set_device('laptop60', 60, 33.5)
    set_device('laptop100', 100, 23.5)
    set_device('desktop60', 60, 59.78)
    set_device('desktop100', 100, 59.78)

def main():
    # At first, you have to choose what device you use and the distance.
    # ex: python p1.py -d l -r 60
    # -d for device(laptop=l, desktop=d)
    # -r for distance
    # so, for the first problem, we have to calculate the visual angle when distance = 100
    # python p1.py -d d -r 100
    set_all_device()
    args = utils.add_device_parser()
    mon = utils.parse_to_monitor(args.device, args.distance)

    win = visual.Window((GetSystemMetrics(0), GetSystemMetrics(1)), monitor=mon, units="pix", fullscr=True)
    square_100 = visual.Rect(win, units="pix", width=100, height=100, fillColor=[-1, 0, 1], lineColor=[-1, 0, 1])
    square_100.draw()
    win.flip()
    # In the case when I use desktop, the visual angle is V=2arctan(S/2D) (V*180/pi -> degrees)
    # The real width=3.2cm, when distance=100, the visual angle is 2*arctan(0.016) = 0.032 rad = 1.834 degree
    
    # In the case when I use laptop, the visual angle is V=2arctan(S/2D) (V*180/pi -> degrees)
    # The real width=2.05cm, when distance=100, the visual angle is 2*arctan(0.01025) = 0.020 rad = 1.175 degree

    event.waitKeys()
    win.close()

    print("Desktop: 100px=3.2cm, 0.032 rad = 1.834 degree")
    print("Laptop: 100px=2.05cm, 0.020 rad = 1.175 degree")

if __name__ == '__main__':
    main()
    