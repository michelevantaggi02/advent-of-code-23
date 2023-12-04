lines = []

with open("inputs/2", "r") as inp:
    lines = inp.readlines()

count = 0
for indx, game in enumerate(lines, 1):
    limits = {"red" : 12, "green" : 13, "blue" : 14}
    new_game = game.replace(f"Game {indx}:", "")
    sets = new_game.split(";")
    possible = True
    for game_set in sets:
        extractions = game_set.split(",")
        for extraction in extractions:
            values = extraction.split()
            if int(values[0]) > limits[values[1]]:
                #print(f"in game {indx} : {values[1]} {values[0]} > {limits[values[1]]}")
                possible = False
                break;
        if not possible:
            break;
    if possible:
        #print(f"{indx= }, {game}")
        count += indx

print(count)