import random
import time, os, sys
from renderer import renderer
from InputProcessor import process_input
import shop

# Input Handler
if os.name == "nt":
    def get_key():
        if not msvcrt.kbhit():
            return None

        key = msvcrt.getch()

        # Arrow/function keys
        if key in (b"\x00", b"\xe0"):
            key = msvcrt.getch()
            return {
                b"H": "up",
                b"P": "down",
                b"K": "left",
                b"M": "right",
            }.get(key)

        return key.decode("utf-8", errors="ignore")
else:
    import select
    import termios
    import tty

    _old_terminal = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())

    def get_key():
        if not select.select([sys.stdin], [], [], 0)[0]:
            return None

        key = sys.stdin.read(1)

        # Arrow keys
        if key == "\x1b":
            if select.select([sys.stdin], [], [], 0)[0]:
                key += sys.stdin.read(1)
            if select.select([sys.stdin], [], [], 0)[0]:
                key += sys.stdin.read(1)

            return {
                "\x1b[A": "up",
                "\x1b[B": "down",
                "\x1b[D": "left",
                "\x1b[C": "right",
            }.get(key)

        return key

# Default game_state
game_state = {
    "Island": 1,
    "Bridges": {1:999,2:999,3:99999,4:999999,5:999999,6:999999,},
    "Coins": 0,
    "Factory": {"Wood":None,"Stone":None,"Iron":None,"Coal":None},
    "Inventory": {
            "Resources": {},
            "Tools": { #lvl,xp
                "Stone Pickaxe": [1, 0],

                }
},
    "Position": [2, 2],
    "Quit": False,
    "Dug": [
        [
            [False for x in range(5)] for i in range(5)
        ] for y in range(8)
    ],
    "Menus": {
        "Inventory": False,
        "Shop": False,
    },
    "Notifications": "",
    "ShopState": ["Resources", 0], # tab ur on, selection
    "InvState": ["Resources", 0],
    "Shop": {
        "Resources": {
            "Wood": 5,
            "Stone": 10,
            "Coal": 15,
            "Iron": 20,
            "Gold": 25,
            "Diamond": 30,
            "Emerald": 35
        },
        "Tools": {
            "Stone Pickaxe": [10, {"Stone": 5, "Wood": 2}],
            "Iron Pickaxe": [20, {"Iron": 5, "Stone": 5}],
            "Diamond Pickaxe": [30, {"Diamond": 5, "Iron": 5}],
            "Emerald Pickaxe": [40, {"Emerald": 5, "Diamond": 5}]
        },
    },
    "AllItems": {
        "Dirt": 1,
        "Wood": 5,
        "Stone": 10,
        "Coal": 15,
        "Iron": 20,
        "Gold": 25,
        "Diamond": 30,
        "Emerald": 35
    }
}
    

os.system("cls" if os.name == "nt" else "clear")

while not game_state["Quit"]:
    key = get_key()
    print("\033[1;1H", end="")

    game_state = process_input(key, game_state)

    renderer(game_state)
    time.sleep(1/15)
    if random.randint(1, 900) == 1:
        game_state["Dug"] = [
            [
                [False for x in range(5)] for i in range(5)
            ] for y in range(8)
        ]
        game_state["Notifications"] = "The island has been regenerated!"
    pass