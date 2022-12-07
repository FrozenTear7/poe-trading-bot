import pyautogui


def party_status():
    pyautogui.press('S')
    if pyautogui.locate('images/partyInvitationSent.png', pyautogui.screenshot(region=(30, 317, 567, 38))) or \
            pyautogui.locate('images/partyIncomingInvitations.png', pyautogui.screenshot(region=(30, 197, 566, 39))):
        pyautogui.press('S')
        return True

    pyautogui.press('S')
    return False
