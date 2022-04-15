from constants import CURRENCY_TAB


def alt_name_fix(name):
    if name in list(CURRENCY_TAB):
        return name
    else:
        try:
            return list(filter(lambda x: CURRENCY_TAB[x]['altName'] == name, CURRENCY_TAB))[0]
        except:
            return None
