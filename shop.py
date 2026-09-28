def Buy(item,count = 1):
    gamestate["Coins"] -= gamestate["Shop"][item]


def color(text, rgb, bold=False):
    r, g, b = rgb
    code = f"\033[1;38;2;{r};{g};{b}m" if bold else f"\033[38;2;{r};{g};{b}m"
    return f"{code}{text}\033[0m"

def shop_renderer(game_state):
    print("Resources [X] | Tools [C]")