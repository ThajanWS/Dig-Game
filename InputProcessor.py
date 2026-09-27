import random
from data import islandData

menu_bindings = {
    ""
}

def process_input(key, game_state):
    def move(vector):
        if 0 <= game_state["Position"][0] - vector[0] < 5:
            game_state["Position"][0] -= vector[0]
        if 0 <= game_state["Position"][1] + vector[1] < 5:
            game_state["Position"][1] += vector[1]

    if key == "w" or key == "up":
        move([1, 0])
    elif key == "s" or key == "down":
        move([-1, 0])
    elif key == "a" or key == "left":
        move([0, -1])
    elif key == "d" or key == "right":
        move([0, 1])
    elif key == "q":
        game_state["Quit"] = True
    elif key == " ":
        if not game_state["Dug"][game_state["Island"]][game_state["Position"][0]][game_state["Position"][1]]:
            game_state["Dug"][game_state["Island"]][game_state["Position"][0]][game_state["Position"][1]] = True
            
            choice = random.randint(1, 100)
            result = ""
            current = 0
            for i, v in islandData[game_state["Island"]].items():
                current += v
                if current > choice:
                    result = i
                    break
                
            if result != "":
                if result in game_state["Inventory"]:
                    game_state["Inventory"][result] += 1
                else:
                    game_state["Inventory"][result] = 1
                game_state["Notifications"] = f"You got one {result}"
            else:
                game_state["Notifications"] = f" "
        
        # game_state["Inventory"]
    elif key == "i":
        game_state["Menus"]["Inventory"] = not game_state["Menus"]["Inventory"]
        if game_state["Menus"]["Inventory"]:
            game_state["Menus"]["Shop"] = False
    elif key == "g":
        game_state["Menus"]["Shop"] = not game_state["Menus"]["Shop"]
        if game_state["Menus"]["Shop"]:
            game_state["Menus"]["Inventory"] = False

    return game_state