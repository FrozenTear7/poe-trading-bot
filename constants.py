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
SELL_CURRENCY_FOR_CURRENCY_REGEX = f'@From (<.+> )?(.+): Hi, (I\'d|I would) like to buy your (\d+) (.+) for my (\d+) (.+) in {LEAGUE_NAME}'
CLIPBOARD_CURRENCY_REGEX = '.+Rarity: \w+ - (.+) - -+ - Stack Size: (\d+).+'
ALREADY_INVITED_REGEX = 'The Operation could not be completed because you are already in a party\.'

# Other constants
WAIT_RETRIES = 15
WAIT_AGAIN_RETRIES = 20

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

PARTY_WINDOW_TAG_X = 0.178
PARTY_WINDOW_TAG_Y = 0.167

CELL_SIZE = 70

STASH_TAB_PRICING_MENU_THRESHOLD = 0.083
STASH_TAB_PRICING_MENU_SELECT_ABOVE_THRESHOLD = (-0.047, 0.078)
STASH_TAB_PRICING_MENU_SELECT_UNDER_THRESHOLD = (0, 0.078)

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


def generic_trade_tab_x(row): return int((0.022 * RESOLUTION[0]) + (CELL_SIZE * (row - 1)))
def generic_trade_tab_y(col): return int((0.143 * RESOLUTION[1]) + (CELL_SIZE * (col - 1)))


# Currency (Setup for currency tab)
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
    'Scroll of Wisdom': {
        'exchangeName': 'wisdom',
        'buyLimit': 3000,
        'sell': {
            'active': True,
            'tabName': 'C',
            'subTabName': 'General',
            'x': 0.06,
            'y': 0.189
        },
        'buy': {
            'active': True,
            'tabName': 'T1',
            'x': generic_trade_tab_x(1),
            'y': generic_trade_tab_y(1)
        },
        'stackSize': 40
    },
    # 'Gemcutter\'s Prism': {
    #     'altName': 'gcp',
    #     'x': 550,
    #     'y': 186,
    #     'stackSize': 20
    # },
    # 'Cartographer\'s Chisel': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/zbVRF4',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/4my8I9',
    #     'altName': 'chisel',
    #     'exchangeName': 'chisel',
    #     'buyActive': False,
    #     'sellActive': False,
    #     'buyLimit': 3000,
    #     'tabName': 'C',
    #     'subTabName': 'General',
    #     'buy': {
    #         'x': 44,
    #         'y': 152
    #     },
    #     'sell': {
    #         'x': 600,
    #         'y': 200
    #     },
    #     'stackSize': 20
    # },
    # # 2nd row
    # 'Orb of Alteration': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/Ny7gfR',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/AjnbtX',
    #     'altName': 'alteration',
    #     'exchangeName': 'alt',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 2000,
    #     'tabName': 'C',
    #     'subTabName': 'General',
    #     'buy': {
    #         'x': 44,
    #         'y': 200
    #     },
    #     'sell': {
    #         'x': 116,
    #         'y': 256
    #     },
    #     'stackSize': 20
    # },
    # 'Exalted Orb': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/12R5ck',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/Nn8Vt0',
    #     'altName': 'exalted',
    #     'exchangeName': 'exalted',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 5,
    #     'tabName': 'C',
    #     'subTabName': 'General',
    #     'buy': {
    #         'x': 95,
    #         'y': 152
    #     },
    #     'sell': {
    #         'x': 300,
    #         'y': 270
    #     },
    #     'stackSize': 10
    # },
    # 'Orb of Alchemy': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/yYYOiR',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/rPe7CQ',
    #     'altName': 'alchemy',
    #     'exchangeName': 'alch',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 2000,
    #     'tabName': 'C',
    #     'subTabName': 'General',
    #     'buy': {
    #         'x': 44,
    #         'y': 316
    #     },
    #     'sell': {
    #         'x': 489,
    #         'y': 256
    #     },
    #     'stackSize': 10
    # },
    # # 3rd row
    # 'Exalted Shard': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/nrmMT0',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/4mjgu9',
    #     'altName': 'exalted-shard',
    #     'exchangeName': 'exalted-shard',
    #     'buyActive': True,
    #     'sellActive': False,
    #     'buyLimit': 100000,
    #     'tabName': 'C',
    #     'subTabName': 'General',
    #     'buy': {
    #         'x': 44,
    #         'y': 366
    #     },
    #     'sell': {
    #         'x': 303,
    #         'y': 314
    #     },
    #     'stackSize': 20
    # },
    # 'Divine Orb': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/nrmMT0',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/4mjgu9',
    #     'altName': 'divine',
    #     'exchangeName': 'divine',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 100000,
    #     'tabName': 'C',
    #     'subTabName': 'General',
    #     'buy': {
    #         'x': 40,
    #         'y': 150
    #     },
    #     'sell': {
    #         'x': 610,
    #         'y': 320
    #     },
    #     'stackSize': 10
    # },
    # # # 4th row
    # 'Orb of Fusing': {
    #     'altName': 'fusing',
    #     'x': 176,
    #     'y': 383,
    #     'stackSize': 20
    # },
    # # 5th row
    # 'Vaal Orb': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/18GVuV',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/EB9LC5',
    #     'altName': 'vaal',
    #     'exchangeName': 'vaal',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 2000,
    #     'tabName': 'C',
    #     'subTabName': 'General',
    #     'buy': {
    #         'x': 44,
    #         'y': 416
    #     },
    #     'sell': {
    #         'x': 608,
    #         'y': 510
    #     },
    #     'stackSize': 10
    # },
    # 6th row
    'Orb of Scouring': {
        'exchangeName': 'scour',
        'buyLimit': 1000,
        'sell': {
            'active': True,
            'tabName': 'C',
            'subTabName': 'General',
            'x': 0.227,
            'y': 0.472
        },
        'buy': {
            'active': True,
            'tabName': 'T1',
            'x': generic_trade_tab_x(1),
            'y': generic_trade_tab_y(2)
        },
        'stackSize': 40
    },
    # # 'Awakened Sextant': {
    # #     'altName': 'awakened sextant',
    # #     'x': 548,
    # #     'y': 516,
    # #     'stackSize': 10
    # # },
    # # 7th row
    # 'Orb of Regret': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/zbJai4',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/9z6ztK',
    #     'altName': 'regret',
    #     'exchangeName': 'regret',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 2000,
    #     'tabName': 'C',
    #     'subTabName': 'General',
    #     'buy': {
    #         'x': 44,
    #         'y': 466
    #     },
    #     'sell': {
    #         'x': 438,
    #         'y': 452
    #     },
    #     'stackSize': 40
    # },
    # # Influence
    # 'Eldritch Chaos Orb': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/gW3wrr7iQ',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/Jd0pgovsl',
    #     'altName': 'eldritch-chaos-orb',
    #     'exchangeName': 'eldritch-chaos-orb',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 20,
    #     'tabName': 'C',
    #     'subTabName': 'Influence',
    #     'buy': {
    #         'x': 44,
    #         'y': 520
    #     },
    #     'sell': {
    #         'x': 464,
    #         'y': 454
    #     },
    #     'stackSize': 10
    # },
    # 'Eldritch Orb of Annulment': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/YqMJoRXIY',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/E60YglVu5',
    #     'altName': 'eldritch-orb-of-annulment',
    #     'exchangeName': 'eldritch-orb-of-annulment',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 20,
    #     'tabName': 'C',
    #     'subTabName': 'Influence',
    #     'buy': {
    #         'x': 44,
    #         'y': 576
    #     },
    #     'sell': {
    #         'x': 524,
    #         'y': 454
    #     },
    #     'stackSize': 20
    # },
    # 'Eldritch Exalted Orb': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/MD02JD5sJ',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/BJ0Ze2Ku8',
    #     'altName': 'eldritch-exalted-orb',
    #     'exchangeName': 'eldritch-exalted-orb',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 50,
    #     'tabName': 'C',
    #     'subTabName': 'Influence',
    #     'buy': {
    #         'x': 44,
    #         'y': 626
    #     },
    #     'sell': {
    #         'x': 494,
    #         'y': 516
    #     },
    #     'stackSize': 10
    # },
    # 'Orb of Conflict': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/D80aXEvf5',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/yR7M3R8FR',
    #     'altName': 'orb-of-conflict',
    #     'exchangeName': 'orb-of-conflict',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 10,
    #     'tabName': 'C',
    #     'subTabName': 'Influence',
    #     'buy': {
    #         'x': 44,
    #         'y': 686
    #     },
    #     'sell': {
    #         'x': 166,
    #         'y': 514
    #     },
    #     'stackSize': 10
    # },
    # 'Exceptional Eldritch Ember': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/2rW6R6osk',
    #     'buy_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/pjyGLpWS0',
    #     'altName': 'exceptional-eldritch-ember',
    #     'exchangeName': 'exceptional-eldritch-ember',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 10,
    #     'tabName': 'C',
    #     'subTabName': 'Influence',
    #     'buy': {
    #         'x': 44,
    #         'y': 730
    #     },
    #     'sell': {
    #         'x': 198,
    #         'y': 434
    #     },
    #     'stackSize': 10
    # },
    # 'Exceptional Eldritch Ichor': {
    #     'sell_url': f'https://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/yR64OY8sR',
    #     'buy_url': 'fhttps://www.pathofexile.com/trade/exchange/{LEAGUE_NAME}/KDEmgaqc5',
    #     'altName': 'exceptional-eldritch-ichor',
    #     'exchangeName': 'exceptional-eldritch-ichor',
    #     'buyActive': True,
    #     'sellActive': True,
    #     'buyLimit': 10,
    #     'tabName': 'C',
    #     'subTabName': 'Influence',
    #     'buy': {
    #         'x': 92,
    #         'y': 150
    #     },
    #     'sell': {
    #         'x': 200,
    #         'y': 314
    #     },
    #     'stackSize': 10
    # },
    # # Other
    # 'Gilded Expedition Scarab': {
    #     'buy_url': f'https://www.pathofexile.com/trade/search/{LEAGUE_NAME}/3XpWP3KI5',
    #     'altName': 'gilded-expedition-scarab',
    #     'exchangeName': 'gilded-expedition-scarab',
    #     'buyActive': True,
    #     'sellActive': False,
    #     'buyLimit': 20,
    #     'buy': {
    #         'x': 92,
    #         'y': 362
    #     },
    #     'stackSize': 10
    # },
    # 'Gilded Legion Scarab': {
    #     'buy_url': f'https://www.pathofexile.com/trade/search/{LEAGUE_NAME}/Z6DW8LzuQ',
    #     'altName': 'gilded-legion-scarab',
    #     'exchangeName': 'gilded-legion-scarab',
    #     'buyActive': True,
    #     'sellActive': False,
    #     'buyLimit': 20,
    #     'buy': {
    #         'x': 92,
    #         'y': 420
    #     },
    #     'stackSize': 10
    # },
    # 'Gilded Ambush Scarab': {
    #     'buy_url': f'https://www.pathofexile.com/trade/search/{LEAGUE_NAME}/4r7qLkT9',
    #     'altName': 'gilded-ambush-scarab',
    #     'exchangeName': 'gilded-ambush-scarab',
    #     'buyActive': True,
    #     'sellActive': False,
    #     'buyLimit': 20,
    #     'buy': {
    #         'x': 92,
    #         'y': 467
    #     },
    #     'stackSize': 10
    # },
    # 'Gilded Cartography Scarab': {
    #     'buy_url': f'https://www.pathofexile.com/trade/search/{LEAGUE_NAME}/D8ZOkXT5',
    #     'altName': 'gilded-cartography-scarab',
    #     'exchangeName': 'gilded-cartography-scarab',
    #     'buyActive': True,
    #     'sellActive': False,
    #     'buyLimit': 20,
    #     'buy': {
    #         'x': 92,
    #         'y': 517
    #     },
    #     'stackSize': 10
    # }
}
