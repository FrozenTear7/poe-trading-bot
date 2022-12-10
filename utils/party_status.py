import pyautogui
from constants import PARTY_WINDOW_TAG_X, PARTY_WINDOW_TAG_Y


def party_status():
    pyautogui.press('S')
    pyautogui.moveTo(PARTY_WINDOW_TAG_X, PARTY_WINDOW_TAG_Y)
    pyautogui.click()
    if pyautogui.locate('images/partyInvitationSent.png', pyautogui.screenshot(region=(30, 317, 567, 38))) or \
            pyautogui.locate('images/partyIncomingInvitations.png', pyautogui.screenshot(region=(30, 197, 566, 39))):
        pyautogui.press('S')
        return True

    pyautogui.press('S')
    return False
