
lines = []

with open("inputs/1", "r") as inp:
    lines = inp.readlines()

total = 0
for i in lines:
    found_first = found_last = None
    for j in range(len(lines)):
        if i[j].isnumeric() and found_first is None:
            found_first = i[j]
        if i[-(j + 1)].isnumeric() and found_last is None:
            found_last = i[-(j + 1)]
        if found_first and found_last:
            found = int(found_first + found_last)
            total += found
            break

print(total)