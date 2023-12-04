lines = []

with open("inputs/2", "r") as inp:
    lines = inp.readlines()

power_sum = 0
for indx, game in enumerate(lines, 1):
    limits = {"red" : 0, "green" : 0, "blue" : 0}
    new_game = game.replace(f"Game {indx}:", "")
    sets = new_game.split(";")
    for game_set in sets:
        extractions = game_set.split(",")
        for extraction in extractions:
            values = extraction.split()
            limits[values[1]] = max(int(values[0]), limits[values[1]])
    power_sum += limits["red"] * limits["green"] * limits["blue"] 

            


print(power_sum)