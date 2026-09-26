import time, os, sys
from renderer import renderer
from InputProcessor import process_input
import Shop

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





game_state = {
    "Island": 1,
    "Coins": 0,
    "Inventory": {
            "Resources": {"Wood":0,
                            "Stone":0,
                            "Coal":0,
                            "Iron":0,
                            "Gold":0,
                            "Diamond":0,
                            "Emerald":0
                        },
            "Tools": { #lvl,xp
                "Stone Pickaxe": [1, 0],

                }
},
    "Position": [2, 2],
    "Quit": False,
}

island_rewards = [
    {
        "Dirt": 40,
        "Wood": 40,
    },
    {
        "Stone": 50,
        "Coal": 15,
    },
    {
        "Coal": 50,
        "Stone": 30,
    },
    {
        "Iron":50,
    },
    {
        "Gold": 40
    },
]

while not game_state["Quit"]:
    key = get_key()
    print("\033[1;1H", end="")

    game_state = process_input(key, game_state)

    renderer(game_state)
    time.sleep(1/30)
    pass