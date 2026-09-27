from shop import shop_renderer
import os
# import time

menu_open = ""
island_emojis = ["X", "🟩", "⬜", "⬛","🔲", "🟨", "🟦", "🟩"]

def color(text, rgb, bold=False):
    r, g, b = rgb
    code = f"\033[1;38;2;{r};{g};{b}m" if bold else f"\033[38;2;{r};{g};{b}m"
    return f"{code}{text}\033[0m"

def renderer(game_state):
    global menu_open

    if game_state["Menus"]["Inventory"]:
        if menu_open != "Inventory":
            os.system("cls" if os.name == "nt" else "clear")
            menu_open = "Inventory"
        
        print(color("Coins: " + str(game_state["Coins"]), (255, 200, 0), True) +"\n")
        
        print(color("Inventory", (255, 86, 74), True))
        print("\nResources:")
        for resource, amount in game_state["Inventory"]["Resources"].items():
            print(f"{resource}: {amount}")
        
        print("\nTools:")
        for tool, (lvl, xp) in game_state["Inventory"]["Tools"].items():
            print(f"{tool} - Level: {lvl}, XP: {xp}")

    elif game_state["Menus"]["Shop"]:
        if menu_open != "Shop":
            os.system("cls" if os.name == "nt" else "clear")
            menu_open = "Shop"
        
        print(color("Coins: " + str(game_state["Coins"]), (255, 200, 0), True) +"\n")
        
        print(color("Shop", (255, 0, 0), True))
        
        shop_renderer(game_state)
    else:
        if menu_open != "Island":
            os.system("cls" if os.name == "nt" else "clear")
            menu_open = "Island"
            
        print(color("Coins: " + str(game_state["Coins"]), (255, 200, 0), True) +"\n")
        print(game_state["Notifications"] + " "*100)
        
        island_emoji = island_emojis[game_state["Island"]]
        
        board = [
            [   
                island_emoji if not game_state["Dug"][game_state["Island"]][i][x] else "🟫"
                for x in range(5)
            ]
            for i in range(5)
        ]   
        
        board[game_state["Position"][0]][game_state["Position"][1]] = "👨"

        print("\n"+color(" "*10 + "Island" +" "+ str(game_state["Island"]),(74, 171, 255 )))
        for i in board:
            print("\t" + "".join(i))

        # print("\t" + "00:00" + "\t")
        
        print("   ",color("Inv [I]", (255, 0, 0))+"\t" + color("Shop [G]", (13, 255, 0)))
    
    return True
   