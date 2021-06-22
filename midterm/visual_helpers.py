from psychopy import visual
from utils import create_grids_iter, create_random_grids_iter


def create_grid_rects(in_width, in_height, margin, c_number, offset_x=0, offset_y=0, **rect_options):
    rects = []
    for x, y, width_of_content, height_of_content in create_grids_iter(in_width, in_height, margin, c_number, offset_x, offset_y):
        rect_options["pos"] = (x, y)
        rect_options["width"] = width_of_content
        rect_options["height"] = height_of_content
        rects.append(visual.Rect(**rect_options))

    return rects


def create_random_grid_rects(in_width, in_height, c_number, offset_x=0, offset_y=0, **rect_options):
    rects = []
    for x, y in create_grids_iter(in_width, in_height, c_number, offset_x=0, offset_y=0):
        rect_options["pos"] = (x, y)
        rects.append(visual.Rect(**rect_options))

    return rects
