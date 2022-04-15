

from constants import HEIGHT, WIDTH


def fix_cell_size_x(cell_size, index):
    if (index % WIDTH) in [3, 6, 9, 11]:
        return cell_size - 1
    else:
        return cell_size


def fix_cell_size_y(cell_size, index):
    if (index % HEIGHT) in [2, 5]:
        return cell_size - 1
    else:
        return cell_size
