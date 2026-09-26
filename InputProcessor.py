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




    return game_state