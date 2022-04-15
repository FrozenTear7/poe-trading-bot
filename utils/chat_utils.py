import pyautogui
import pyperclip


def invite_user(username):
    pyautogui.sleep(3)
    pyautogui.press('ENTER')

    pyautogui.typewrite('/invite ')

    pyperclip.copy(username)
    pyautogui.keyDown('CTRL')
    pyautogui.press('V')
    pyautogui.keyUp('CTRL')

    pyautogui.press('ENTER')


def ignore_player(username):
    pyautogui.sleep(3)
    pyautogui.press('ENTER')

    pyautogui.typewrite('/ignore ')

    pyperclip.copy(username)
    pyautogui.keyDown('CTRL')
    pyautogui.press('V')
    pyautogui.keyUp('CTRL')

    pyautogui.press('ENTER')


def trade_user(username):
    pyautogui.sleep(5)
    pyautogui.press('ENTER')

    pyautogui.typewrite('/tradewith ')

    pyperclip.copy(username)
    pyautogui.keyDown('CTRL')
    pyautogui.press('V')
    pyautogui.keyUp('CTRL')

    pyautogui.press('ENTER')


def thank_user(username):
    pyautogui.press('ENTER')

    pyautogui.typewrite('@')

    pyperclip.copy(username)
    pyautogui.keyDown('CTRL')
    pyautogui.press('V')
    pyautogui.keyUp('CTRL')

    pyautogui.typewrite(' t4t')

    pyautogui.press('ENTER')


def kick_user(username):
    pyautogui.press('ENTER')

    pyautogui.typewrite('/kick ')

    pyperclip.copy(username)
    pyautogui.keyDown('CTRL')
    pyautogui.press('V')
    pyautogui.keyUp('CTRL')

    pyautogui.press('ENTER')


def afk_off():
    pyautogui.press('ENTER')
    pyautogui.typewrite('/afkoff')
    pyautogui.press('ENTER')


def clear_ignore_list():
    pyautogui.sleep(3)
    pyautogui.press('ENTER')
    pyautogui.typewrite('/clear_ignore_list')
    pyautogui.press('ENTER')
