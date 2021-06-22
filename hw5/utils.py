import argparse
from psychopy import monitors

device_map = {
    "d": "desktop",
    "l": "laptop",
}

def add_device_parser():
    parser = argparse.ArgumentParser(description='Process the device options')
    parser.add_argument('-d', '--device', type=str, choices=["l", "d"], default="d",
                        required=False, help='Choose a device')
    parser.add_argument('-r', '--distance', type=float, choices=[60, 100], default=100,
                        required=False, help='Choose a distance')
    args = parser.parse_args()

    return args

def parse_to_monitor(short, dis):
    name = device_map[short]
    monitor = name + str(int(dis))
    print("Using Monitor Spec:", monitor)
    return monitors.Monitor(monitor) 