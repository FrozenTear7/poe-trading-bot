import pyautogui
from constants import PARTY_INVITATION_RECEIVED, PARTY_INVITATION_RECEIVED_BOX_SIZE, PARTY_INVITATION_SENT, PARTY_INVITATION_SENT_BOX_SIZE, PARTY_WINDOW_TAG
import pytesseract
from utils.prefix_print import printtime
from utils.translate_coordinates import translate_coordinates_horizontal, translate_coordinates_vertical


def party_status():
    printtime('Opening the party tab')
    pyautogui.press('S')
    pyautogui.moveTo(translate_coordinates_horizontal(
        PARTY_WINDOW_TAG[0]), translate_coordinates_vertical(PARTY_WINDOW_TAG[1]))
    pyautogui.click()

    invitation_sent_text = pytesseract.image_to_string(pyautogui.screenshot(region=(translate_coordinates_horizontal(
        PARTY_INVITATION_SENT[0]), translate_coordinates_vertical(PARTY_INVITATION_SENT[1]), translate_coordinates_horizontal(
        PARTY_INVITATION_SENT_BOX_SIZE[0]), translate_coordinates_vertical(
        PARTY_INVITATION_SENT_BOX_SIZE[1])))).lower().strip()

    invitation_received_text = pytesseract.image_to_string(pyautogui.screenshot(region=(translate_coordinates_horizontal(
        PARTY_INVITATION_RECEIVED[0]), translate_coordinates_vertical(PARTY_INVITATION_RECEIVED[1]), translate_coordinates_horizontal(
        PARTY_INVITATION_RECEIVED_BOX_SIZE[0]), translate_coordinates_vertical(
        PARTY_INVITATION_RECEIVED_BOX_SIZE[1])))).lower().strip()

    printtime(invitation_sent_text)
    printtime('invitation sent' in invitation_sent_text)
    printtime(invitation_received_text)
    printtime('invitation received' in invitation_received_text)
    printtime('invitation sent' in invitation_sent_text or 'invitation received' in invitation_received_text)

    pyautogui.press('S')
    return 'invitation sent' in invitation_sent_text or 'invitation received' in invitation_received_text
