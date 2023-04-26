import pyautogui
from constants import CELL_SIZE, EQUIPMENT, HEIGHT, WIDTH


def empty_equipment(item_count=60):
    item_counter = 1

    pyautogui.keyDown('CTRL')
    for i in range(WIDTH):
        for j in range(HEIGHT):
            pyautogui.moveTo(EQUIPMENT['start']['x'] + (i * EQUIPMENT[CELL_SIZE]),
                             EQUIPMENT['start']['y'] + (j * EQUIPMENT[CELL_SIZE]))
            pyautogui.click()

            item_counter += 1
            if item_counter > item_count:
                pyautogui.keyUp('CTRL')
                return

    pyautogui.keyUp('CTRL')
