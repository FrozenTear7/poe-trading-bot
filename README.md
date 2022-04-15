# poe-trading-bot

## About

The bot is made purely for flipping currency, it sets buy and sell orders according to the provided setup. Although it is much slower than a normal player, it can work autonomously and bring a good couple of exalts from a day of trading.

Keep in mind that it's not perfect, make sure to check on it from time to time if everything is still working. If you encounter any bugs, please notify me about it, preferably with a video proof, so I can replicate the problem.

## Requirements

_Remember to create a [virtual environment](https://docs.python.org/3/library/venv.html) for the project_

1. Run `pip install -r requirements.txt` to install _Python_ dependencies

## Setup

Values provided in `constants.py` were set with Full HD resolution in mind, if you use different resolution, change them accordingly to your setup. Simple **Paint** will be your best friend to retrieve specific pixel information.
Also make sure to change the log file path if your **Path of Exile** is installed outside of _Steam_ or its default games directory.
There are also other configuration variables that you need to confirm are correct for your PoE setup, such as stash order and positions. That being said, I recommend using the bot only if you have premium Currency Tab, a normal premium currency tab to store orders and preferably other premium tabs such as the Fragment Tab to be able to trade other various currencies.

## Run the bot

Run the bot with `python main.py` from the root directory, kick back and enjoy the show.
The bot purges the ignore list at the start, keep that in mind if you have some important criminals ignored already. Whenever the bot encounters a failed trade, it simply ignores the trader to simply let them know they do not have to spam messages asking what the hell is happening, please accept my trade.

Remember to set all in game notifications to off - especially party invites and trades so that moving items can go smoothly without being interrupted by popups.
The bot requires you to stay by your stash - correct coordinates are required in the `constants.py` setup.

## Stash state

_Sell_ data means for how much of the other currency, you are _selling_ you chaos orb, which is **What you get** in chaos and **What you pay** in the other currency on PoE Trade site.

For example:

You want to exchange your **5 Chaos Orb** for **12 Vaal Orb**, so you have to put:

```json
"sell": {
    "chaos": 5,
    "own": 12
},

```

under the **Vaal Orb** record in `stash_state.json`, where _self_ means the currency you are setting the price for.

---

_Buy_ means the opposite trade, where you want to sell currency for chaos orbs, so you invert the order of _Sell_ logic.

---

I included some exchange URLs in the contants file for easier access, there was a plan to create a script that fetches data from the trade site and sets the prices automatically, but the topic is too delicate. If you come up with a solid solution, please feel free to contribute to the project.

## Contribution

The project is far from perfect, if you have any recommendations, encounter bugs or feel like adding more functionality, please go ahead and create issues or send pull requests.
