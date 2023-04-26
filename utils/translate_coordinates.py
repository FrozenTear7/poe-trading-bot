from constants import RESOLUTION


def translate_coordinates_horizontal(coordinate):
    return int(coordinate * RESOLUTION[0])


def translate_coordinates_vertical(coordinate):
    return int(coordinate * RESOLUTION[1])
