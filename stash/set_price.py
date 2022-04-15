import pyautogui


def clear_current_price():
    x, y = pyautogui.position()
    if x > 160:
        pyautogui.moveRel(-90, 84)
    else:
        pyautogui.moveRel(0, 84)
    pyautogui.click()
    pyautogui.press('UP')
    pyautogui.press('UP')
    pyautogui.press('ENTER')
    pyautogui.moveRel(260, 0)
    pyautogui.click()
    pyautogui.hotkey('CTRL', 'A')
    pyautogui.press('BACKSPACE')


def set_price(stash_state, price_already_set=False):
    pyautogui.click(button='right')
    if price_already_set:
        clear_current_price()
    pyautogui.typewrite(
        f'~price {stash_state["price"]["sell"]["chaos"]}/{stash_state["price"]["sell"]["self"]} chaos')
    pyautogui.press('ENTER')


def set_chaos_price(stash_state, name, price_already_set=False):
    pyautogui.click(button='right')
    if price_already_set:
        clear_current_price()
    pyautogui.typewrite(
        f'~price {stash_state["price"]["buy"]["self"]}/{stash_state["price"]["buy"]["chaos"]} {name}')
    pyautogui.press('ENTER')
