# Game setup
LEAGUE_NAME = 'Standard'
# LOG_FILE = 'C:/Program Files (x86)/Steam/steamapps/common/Path of Exile/logs/Client.txt'  # Steam default location
LOG_FILE = 'C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/Client.txt'  # Standalone client default location
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
ALREADT_INVITED_REGEX = 'The Operation could not be completed because you are already in a party\.'

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
STASH_COORDINATES = (1080, 450)

TRADE_WINDOW_START_LEFT = 300
TRADE_WINDOW_START_TOP = 193
TRADE_WINDOW_END_LEFT = 954
TRADE_WINDOW_END_TOP = 476

PARTY_WINDOW_TAG_X=340
PARTY_WINDOW_TAG_Y=180

TRADE_WINDOW = {
    'start': {
        'x': 312,
        'y': 204
    },
    'end': {
        'x': 942,
        'y': 466
    },
    'cellSize': 54
}
EQUIPMENT = {
    'start': {
        'x': 1298,
        'y': 613
    },
    'end': {
        'x': 1093,
        'y': 850
    },
    'cellSize': 53
}
ACCEPT_BUTTON = {
    'x': 380,
    'y': 820
}
ACCEPT_ITEMS = {
    'start': {
        'x': 492,
        'y': 828
    },
    'end': {
        'x': 763,
        'y': 841
    }
}
SUB_TABS = {
    'C': {
        'General': {
            'x': 250,
            'y': 150
        },
        'Influence': {
            'x': 420,
            'y': 150
        }
    },
    'F': {
        'General': {
            'x': 172,
            'y': 148
        },
        'Breach': {
            'x': 330,
            'y': 148
        },
        'Scarab': {
            'x': 484,
            'y': 148
        }
    },
}

# Currency (Setup for currency tab)
CURRENCY_TAB = {
    'Chaos Orb': {
        'altName': 'chaos',
        'buyActive': False,  # DO NOT CHANGE THIS
        'sellActive': False,  # DO NOT CHANGE THIS
        'tabName': 'C',
        'subTabName': 'General',
        'sell': {
            'x': 550,
            'y': 270
        },
        'stackSize': 10
    },
    # 1st row
    # 'Scroll of Wisdom': {
    #     'altName': 'wisdom',
    #     'x': 116,
    #     'y': 186,
    #     'stackSize': 40
    # },
    # 'Gemcutter\'s Prism': {
    #     'altName': 'gcp',
    #     'x': 550,
    #     'y': 186,
    #     'stackSize': 20
    # },
    # 'Cartographer\'s Chisel': {
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/zbVRF4',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/4my8I9',
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
    # 2nd row
    # 'Orb of Alteration': {
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/Ny7gfR',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/AjnbtX',
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
    'Exalted Orb': {
        'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/12R5ck',
        'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/Nn8Vt0',
        'altName': 'exalted',
        'exchangeName': 'exalted',
        'buyActive': True,
        'sellActive': True,
        'buyLimit': 5,
        'tabName': 'C',
        'subTabName': 'General',
        'buy': {
            'x': 95,
            'y': 152
        },
        'sell': {
            'x': 300,
            'y': 270
        },
        'stackSize': 10
    },
    # 'Orb of Alchemy': {
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/yYYOiR',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/rPe7CQ',
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
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/nrmMT0',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/4mjgu9',
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
    'Divine Orb': {
        'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/nrmMT0',
        'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/4mjgu9',
        'altName': 'divine',  # What is altName?
        'exchangeName': 'divine',
        'buyActive': True,
        'sellActive': True,
        'buyLimit': 100000,
        'tabName': 'C',
        'subTabName': 'General',
        'buy': {
            'x': 40,
            'y': 150
        },
        'sell': {
            'x': 610,
            'y': 320
        },
        'stackSize': 10
    },
    # # 4th row
    # # 'Orb of Fusing': {
    # #     'altName': 'fusing',
    # #     'x': 176,
    # #     'y': 383,
    # #     'stackSize': 20
    # # },
    # # 5th row
    # 'Vaal Orb': {
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/18GVuV',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/EB9LC5',
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
    # # 6th row
    # # 'Awakened Sextant': {
    # #     'altName': 'awakened sextant',
    # #     'x': 548,
    # #     'y': 516,
    # #     'stackSize': 10
    # # },
    # # 7th row
    # 'Orb of Regret': {
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/zbJai4',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/9z6ztK',
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
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/gW3wrr7iQ',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/Jd0pgovsl',
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
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/YqMJoRXIY',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/E60YglVu5',
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
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/MD02JD5sJ',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/BJ0Ze2Ku8',
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
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/D80aXEvf5',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/yR7M3R8FR',
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
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/2rW6R6osk',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/pjyGLpWS0',
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
    #     'sell_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/yR64OY8sR',
    #     'buy_url': 'https://www.pathofexile.com/trade/exchange/Archnemesis/KDEmgaqc5',
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
    #     'buy_url': 'https://www.pathofexile.com/trade/search/Archnemesis/3XpWP3KI5',
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
    #     'buy_url': 'https://www.pathofexile.com/trade/search/Archnemesis/Z6DW8LzuQ',
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
    #     'buy_url': 'https://www.pathofexile.com/trade/search/Archnemesis/4r7qLkT9',
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
    #     'buy_url': 'https://www.pathofexile.com/trade/search/Archnemesis/D8ZOkXT5',
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
