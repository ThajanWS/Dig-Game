island_emojis = ["X", "🟩", "⬜", "⬛","🔲", "🟨", "🟦", "🟩"]

def renderer(game_state):
    print("Coins: " + str(game_state["Coins"]))
    island_emoji = island_emojis[game_state["Island"]]

    board = [[island_emoji for x in range(5)] for i in range(5)]

    board[game_state["Position"][0]][game_state["Position"][1]] = "👨"

    for i in board:
        print("".join(i))
    return "done"