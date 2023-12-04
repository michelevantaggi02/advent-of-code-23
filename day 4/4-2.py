lines = []

with open("inputs/4", "r") as inp:
    lines = inp.readlines()

total = 0

amounts = [1 for i in lines]

for line_indx, line in enumerate(lines):
    winning = [int(i) for i in line[10:40].split()]
    played = [int(i) for i in line[42:].split()]

    winning.sort()
    played.sort()

    win_indx = play_indx = 0

    wins = 0

    while win_indx < len(winning) and play_indx < len(played):
        if winning[win_indx] == played[play_indx]:
            wins += 1
            win_indx += 1
            play_indx += 1
        elif winning[win_indx] > played[play_indx]:
            play_indx += 1
        else:
            win_indx += 1

    for i in range(line_indx + 1, line_indx + 1 + wins):
        amounts[i] += amounts[line_indx]
        
print(sum(amounts))