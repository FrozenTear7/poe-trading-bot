import pyautogui
from constants import WAIT_RETRIES


def wait_for_window():
    pyautogui.sleep(1)

    while True:
        if not pyautogui.locate('images/waitingForTradeAccept.png', pyautogui.screenshot(region=(726, 490, 465, 96))):
            break
        pyautogui.sleep(1)

    return pyautogui.locate('images/tradeWindow.png', pyautogui.screenshot(region=(296, 496, 664, 362)))


def wait_for_user_items() -> bool:
    for _ in range(WAIT_RETRIES):
        try:
            if pyautogui.locate('images/acceptTradeItems.png', pyautogui.screenshot(region=(486, 824, 282, 25))):
                return True
        except pyautogui.ImageNotFoundException:
            pass

        pyautogui.sleep(1)

    return False
