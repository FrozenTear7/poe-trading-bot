import pyautogui


def party_status():
    pyautogui.press('S')
    if pyautogui.locate('images/partyInvitationSent.png', pyautogui.screenshot(region=(30, 317, 566, 38))) \
            or pyautogui.locate('images/partyNoInvitations.png', pyautogui.screenshot(region=(30, 197, 566, 158))):
        pyautogui.press('S')
        return False

    pyautogui.press('S')
    return True
