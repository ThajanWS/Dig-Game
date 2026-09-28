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
        if game_state["Menus"]["Inventory"]:
            game_state["InvState"][1] = max(0, game_state["InvState"][1] - 1)
        elif game_state["Menus"]["Shop"]:
            game_state["ShopState"][1] = max(0, game_state["ShopState"][1] - 1)
        else:
            move([1, 0])
    elif key == "s" or key == "down":
        if game_state["Menus"]["Inventory"]:
            game_state["InvState"][1] = min(len(game_state["Inventory"]) - 1, game_state["InvState"][1] + 1)
        elif game_state["Menus"]["Shop"]:
            game_state["ShopState"][1] = min(len(game_state["Shop"]) - 1, game_state["ShopState"][1] + 1)
        else:
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
                if result in game_state["Inventory"]["Resources"]:
                    game_state["Inventory"]["Resources"][result] += 1
                else:
                    game_state["Inventory"]["Resources"][result] = 1
                game_state["Notifications"] = f"You got one {result}"
            else:
                game_state["Notifications"] = f"You got nothing :("
        
        # game_state["Inventory"]
    elif key == "i":
        game_state["Menus"]["Inventory"] = not game_state["Menus"]["Inventory"]
        if game_state["Menus"]["Inventory"]:
            game_state["Menus"]["Shop"] = False
    elif key == "g":
        game_state["Menus"]["Shop"] = not game_state["Menus"]["Shop"]
        if game_state["Menus"]["Shop"]:
            game_state["Menus"]["Inventory"] = False
    elif key == "2":
        try:
            if game_state["Bridges"][game_state["Island"]+1] != None:
                if game_state["Bridges"][game_state["Island"]+1] > 0:
                    game_state["Island"] += 1
                    game_state["Bridges"][game_state["Island"]] -= 1
                    game_state["Notifications"] = f"You moved to island {game_state["Island"]}. The bridge is now at {game_state["Bridges"][game_state["Island"]]} durability."
                else:
                    game_state["Notifications"] = f"Bridge {game_state["Island"]} doesn't have enough durability!"
            else:
                game_state["Notifications"] = f"Build a bridge to get to Island {game_state["Island"]+1}!"
        except Exception as e:
            game_state["Notifications"] = "That island doesn't exist."   


    elif key == "1":
            try:
                if game_state["Bridges"][game_state["Island"]-1] != None:
                    if game_state["Bridges"][game_state["Island"]-1] > 0:
                        game_state["Island"] -= 1
                        game_state["Bridges"][game_state["Island"]] -= 1
                        game_state["Notifications"] = f"You moved to island {game_state["Island"]}. The bridge is now at {game_state["Bridges"][game_state["Island"]]} durability."
                    else:
                        game_state["Notifications"] = f"Bridge {game_state["Island"] - 1} doesn't have enough durability!"
                else:
                    game_state["Notifications"] = f"Build a bridge to get to Island {game_state["Island"]-1}!"
            except Exception as e:
                game_state["Notifications"] = "That island doesn't exist."   
    
    elif key == "X":
        if game_state["Menus"]["Inventory"]:
            game_state["InvState"][0] = ["Resources"]
        elif game_state["Menus"]["Shop"]:
            game_state["ShopState"][0] = ["Resources"]
    elif key == "C":
        pass
    elif key == "\n":
        game_state["Notifications"] = " slash n pressed"
    return game_state