lines = []

with open("inputs/4", "r") as inp:
    lines = inp.readlines()

total = 0

for line in lines:
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

    if wins != 0:
        total+= 2 ** (wins - 1)
        
print(total)