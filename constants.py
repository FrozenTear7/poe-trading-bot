# Game setup
LEAGUE_NAME = 'Crucible'
LOG_FILE = 'C:/Program Files (x86)/Steam/steamapps/common/Path of Exile/logs/Client.txt'  # Steam default location
# Standalone client default location
# LOG_FILE = 'C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/Client.txt'

AMOUNT_OF_STASH_TABS = 16
STASH_TABS = ['C', 'T1', 'T2', 'F']

PYAUTOGUI_SPEED = 0.05
TAKE_ITEM_SPEED = 0.03


# Regexes
LOG_REGEX = '.+\[INFO Client \d+\] (: )?(.+)'
INCOMING_PLAYER_WHISPER_REGEX = '@From .+'
PLAYER_JOINED_AREA_REGEX = '(.+) has joined the area\.'
PLAYER_LEFT_AREA_REGEX = '(.+) has left the area\.'
TRADE_ACCEPTED_REGEX = 'Trade accepted\.'
TRADE_CANCELLED_REGEX = 'Trade cancelled\.'
AFK_REGEX = 'AFK mode is now ON\. Autoreply "This player is AFK\."'
SELL_CURRENCY_FOR_CURRENCY_REGEX = f'@From (<.+> )?(.+): Hi, (I\'d|I would) like to buy your (\d+) (.+) for my (\d+) (.+) in (\w+)'
CLIPBOARD_CURRENCY_REGEX = '.+Rarity: \w+ - (.+) - -+ - Stack Size: (\d+)\/(\d+).*'
ALREADY_INVITED_REGEX = 'The Operation could not be completed because you are already in a party\.'

MY_USERNAME = 'OkayegOkEggEgOkay'

# Other constants
WAIT_RETRIES = 5
WAIT_AGAIN_RETRIES = 5

TRADE_VERIFY_RETRIES = 4

# Trade Window/ Inventory Slots
WIDTH = 12
HEIGHT = 5

MOVETO_DURATION = 0.1
CONFIDENCE = 0.5

# Coordinates
RESOLUTION = (2560, 1440)
STASH_COORDINATES = (0.52, 0.483)

TRADE_WINDOW = (0.156, 0.179, 0.497, 0.441)

PARTY_WINDOW_TAG = (0.178, 0.167)

CELL_SIZE = 70

STASH_TAB_PRICING_MENU_THRESHOLD = 0.083
STASH_TAB_PRICING_MENU_SELECT_ABOVE_THRESHOLD = (-0.047, 0.078)
STASH_TAB_PRICING_MENU_SELECT_UNDER_THRESHOLD = (0, 0.078)

PARTY_INVITATION_RECEIVED = (0.12, 0.189)
PARTY_INVITATION_RECEIVED_BOX_SIZE = (0.107, 0.02)

PARTY_INVITATION_SENT = (0.129, 0.301)
PARTY_INVITATION_SENT_BOX_SIZE = (0.091, 0.022)

TRADE_WINDOW = {
    'start': {
        'x': 0.163,
        'y': 0.189
    },
    'end': {
        'x': 0.49,
        'y': 0.431
    },
}
EQUIPMENT = {
    'start': {
        'x': 0.676,
        'y': 0.568
    },
    'end': {
        'x': 0.569,
        'y': 0.787
    },
}
ACCEPT_BUTTON = {
    'x': 0.198,
    'y': 0.76
}
ACCEPT_ITEMS = {
    'start': {
        'x': 0.256,
        'y': 0.767
    },
    'end': {
        'x': 0.397,
        'y': 0.778
    }
}
SUB_TABS = {
    'C': {
        'General': {
            'x': 0.13,
            'y': 0.139
        },
        'Influence': {
            'x': 0.219,
            'y': 0.139
        }
    },
    'F': {
        'General': {
            'x': 0.09,
            'y': 0.137
        },
        'Breach': {
            'x': 0.17,
            'y': 0.137
        },
        'Scarab': {
            'x': 0.25,
            'y': 0.137
        }
    },
}


# None value is purely cosmetic to better see which trades we're not currently using
def generic_trade_tab_x(row): return 0 if row is None else int((0.022 * RESOLUTION[0]) + (CELL_SIZE * (row - 1)))
def generic_trade_tab_y(col): return 0 if col is None else int((0.143 * RESOLUTION[1]) + (CELL_SIZE * (col - 1)))


# Currency (Setup for currency tab) - Crucible league
CURRENCY_TAB = {
    'Chaos Orb': {
        'sell': {
            'active': False,
            'tabName': 'C',
            'subTabName': 'General',
            'x': 0.287,
            'y': 0.251
        },
        'buy': {
            'active': False,
        },
        'stackSize': 20
    },
    # 1st row
    'Scroll of Wisdom': {'exchangeName': 'wisdom', 'buyLimit': 3000, 'sell': {'active': False, 'tabName': 'C', 'subTabName': 'General', 'x': 0.059, 'y': 0.19}, 'buy': {'active': False, 'tabName': 'T1', 'x': generic_trade_tab_x(None), 'y': generic_trade_tab_y(None)}, 'stackSize': 40},
    'Portal Scroll': {'exchangeName': 'portal', 'buyLimit': 3000, 'sell': {'active': False, 'tabName': 'C', 'subTabName': 'General', 'x': 0.089, 'y': 0.188}, 'buy': {'active': False, 'tabName': 'T1', 'x': generic_trade_tab_x(None), 'y': generic_trade_tab_y(None)}, 'stackSize': 40},
    'Enkindling Orb': {'exchangeName': 'enkindling-orb', 'buyLimit': 300, 'sell': {'active': True, 'tabName': 'C', 'subTabName': 'General', 'x': 0.128, 'y': 0.187}, 'buy': {'active': True, 'tabName': 'T1', 'x': generic_trade_tab_x(1), 'y': generic_trade_tab_y(1)}, 'stackSize': 10},
    'Instilling Orb': {'exchangeName': 'instilling-orb', 'buyLimit': 300, 'sell': {'active': True, 'tabName': 'C', 'subTabName': 'General', 'x': 0.158, 'y': 0.189}, 'buy': {'active': True, 'tabName': 'T1', 'x': generic_trade_tab_x(1), 'y': generic_trade_tab_y(2)}, 'stackSize': 10},
    "Blacksmith's Whetstone": {'exchangeName': 'whetstone', 'buyLimit': 3000, 'sell': {'active': False, 'tabName': 'C', 'subTabName': 'General', 'x': 0.197, 'y': 0.188}, 'buy': {'active': False, 'tabName': 'T1', 'x': generic_trade_tab_x(None), 'y': generic_trade_tab_y(None)}, 'stackSize': 20},
    "Armourer's Scrap": {'exchangeName': 'scrap', 'buyLimit': 3000, 'sell': {'active': False, 'tabName': 'C', 'subTabName': 'General', 'x': 0.227, 'y': 0.186}, 'buy': {'active': False, 'tabName': 'T1', 'x': generic_trade_tab_x(None), 'y': generic_trade_tab_y(None)}, 'stackSize': 40},
    "Glassblower's Bauble": {'exchangeName': 'bauble', 'buyLimit': 3000, 'sell': {'active': False, 'tabName': 'C', 'subTabName': 'General', 'x': 0.257, 'y': 0.187}, 'buy': {'active': False, 'tabName': 'T1', 'x': generic_trade_tab_x(None), 'y': generic_trade_tab_y(None)}, 'stackSize': 20},
    "Gemcutter's Prism": {'exchangeName': 'gcp', 'buyLimit': 3000, 'sell': {'active': True, 'tabName': 'C', 'subTabName': 'General', 'x': 0.287, 'y': 0.188}, 'buy': {'active': True, 'tabName': 'T1', 'x': generic_trade_tab_x(1), 'y': generic_trade_tab_y(3)}, 'stackSize': 20},
    "Cartographer's Chisel": {'exchangeName': 'chisel', 'buyLimit': 3000, 'sell': {'active': True, 'tabName': 'C', 'subTabName': 'General', 'x': 0.315, 'y': 0.187}, 'buy': {'active': True, 'tabName': 'T1', 'x': generic_trade_tab_x(1), 'y': generic_trade_tab_y(4)}, 'stackSize': 20},
    # 2nd row
    'Orb of Alteration': {'exchangeName': 'alt', 'buyLimit': 3000, 'sell': {'active': False, 'tabName': 'C', 'subTabName': 'General', 'x': 0.058, 'y': 0.251}, 'buy': {'active': False, 'tabName': 'T1', 'x': generic_trade_tab_x(None), 'y': generic_trade_tab_y(None)}, 'stackSize': 20},
    'Orb of Annulment': {'exchangeName': 'annul', 'buyLimit': 3000, 'sell': {'active': True, 'tabName': 'C', 'subTabName': 'General', 'x': 0.089, 'y': 0.249}, 'buy': {'active': True, 'tabName': 'T1', 'x': generic_trade_tab_x(1), 'y': generic_trade_tab_y(5)}, 'stackSize': 20},
    'Exalted Orb': {'exchangeName': 'exalted', 'buyLimit': 3000, 'sell': {'active': True, 'tabName': 'C', 'subTabName': 'General', 'x': 0.158, 'y': 0.252}, 'buy': {'active': True, 'tabName': 'T1', 'x': generic_trade_tab_x(1), 'y': generic_trade_tab_y(6)}, 'stackSize': 10},
    'Orb of Alchemy': {'exchangeName': 'alch', 'buyLimit': 3000, 'sell': {'active': False, 'tabName': 'C', 'subTabName': 'General', 'x': 0.257, 'y': 0.251}, 'buy': {'active': False, 'tabName': 'T1', 'x': generic_trade_tab_x(None), 'y': generic_trade_tab_y(None)}, 'stackSize': 20},
    'Veiled Chaos Orb': {'exchangeName': 'veiled-chaos-orb', 'buyLimit': 3000, 'sell': {'active': True, 'tabName': 'C', 'subTabName': 'General', 'x': 0.315, 'y': 0.253}, 'buy': {'active': True, 'tabName': 'T1', 'x': generic_trade_tab_x(1), 'y': generic_trade_tab_y(7)}, 'stackSize': 20},
    # 3rd row
    'Exalted Shard': {'exchangeName': 'exalted-shard', 'buyLimit': 3000, 'sell': {'active': False, 'tabName': 'C', 'subTabName': 'General', 'x': 0.159, 'y': 0.306}, 'buy': {'active': True, 'tabName': 'T1', 'x': generic_trade_tab_x(1), 'y': generic_trade_tab_y(8)}, 'stackSize': 20},
    'Divine Orb': {'exchangeName': 'divine', 'buyLimit': 10, 'sell': {'active': True, 'tabName': 'C', 'subTabName': 'General', 'x': 0.318, 'y': 0.302}, 'buy': {'active': True, 'tabName': 'T1', 'x': generic_trade_tab_x(1), 'y': generic_trade_tab_y(9)}, 'stackSize': 10},
    # 4th row
    # 5th row
    # 6th row
}
