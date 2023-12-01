
lines = []

with open("inputs/1", "r") as inp:
    lines = inp.readlines()

total = 0

#lines = lines[0:4]

tests = ["two1nine",
"eightwothree",
"abcone2threexyz",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen",
"xtwone3four",
]

#lines = tests
for i in lines:
    i = str(i[0:-1])
    found_first = found_last = None
    literals = ["zero", "one", "two", "three", "four","five", "six", "seven", "eight", "nine"]
    values = {}
    lowest_index = len(i)
    highest_index = -1
    pairs = {}
    for k in range(10):
        pairs[literals[k]] = str(k)
    for k in literals:
        values[i.find(k)] = k
        lowest_index = min(lowest_index, i.find(k) if i.find(k) != -1 else lowest_index)
        values[i.rfind(k)] = k
        highest_index = max(highest_index, i.rfind(k))
        #print(f"index of {k}: {i.find(k)}")
    


    for j in range(len(i)):

        if j > lowest_index and found_first is None:
            print(f"lowest value: {j} > {lowest_index}: {values[lowest_index]} -> {pairs[values[lowest_index]]}")
            found_first = pairs[values[lowest_index]]
        elif i[j].isnumeric() and found_first is None:
            found_first = i[j]
        if len(i) - (j + 1) < highest_index and found_last is None:
            print(f"highest value: {len(i) - (j + 1)} < {highest_index}: {values[highest_index]} -> {pairs[values[highest_index]]}")
            found_last = pairs[values[highest_index]]
        elif i[-(j + 1)].isnumeric() and found_last is None:
            found_last = i[-(j + 1)]
        if not found_first is None and not found_last is None:
            found = int(found_first + found_last)
            total += found

            print(f" {i} -> {found} -> {total}")
            break

print(total)