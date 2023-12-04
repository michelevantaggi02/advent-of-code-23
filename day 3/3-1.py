lines = []

with open("inputs/3", "r") as inp:
    lines = inp.readlines()
    

line_length = len(lines[0])

def retrieve_full_number(full_string: str, start_index: int) -> ():
    left_limit = right_limit = 0
    return_val = full_string[start_index]
    for i in range(1, len(full_string)):
        if start_index - i < 0:
            left_limit = 0
        if start_index + i > len(full_string):
            right_limit = len(full_string)
        if left_limit == 0:
            left_val = full_string[start_index - i]
            if left_val.isdigit():
                return_val = left_val + return_val
            else:
                left_limit = start_index - i
        if right_limit == 0:
            right_val = full_string[start_index + i]
            if right_val.isdigit():
                return_val += right_val
            else:
                right_limit = start_index + i + 1
        if  right_limit != 0 and left_limit != 0:
            break
    return int(return_val), left_limit, right_limit


symbols = "$%&/*-+@=#"

total = 0

stop = 0

for line_indx, line in enumerate(lines):
    stop = 0
    for char_indx, character in enumerate(line):
        if character.isdigit() and char_indx >= stop:
            number, start, stop = retrieve_full_number(line, char_indx)
            print(f"found full number {number} ({line[start: stop]}) in line {line_indx}[{start}:{stop}]")
            for s in symbols:
                if line[max(start, 0) : min(stop, len(line))].count(s) != 0:
                    print(f"found {s} on adjacent: {line[max(start, 0) : min(stop, len(line))]}")
                    total += number
                    break
                elif line_indx > 0 and lines[line_indx - 1][max(start, 0) : min(stop, len(line))].count(s) != 0:
                    print(f"found {s} on top: {lines[line_indx - 1][max(start, 0) : min(stop, len(line))]}")
                    total += number
                    break
                elif line_indx < len(lines) - 1 and lines[line_indx + 1][max(start, 0) : min(stop, len(line))].count(s) != 0:
                    total += number
                    print(f"found {s} on bottom: {lines[line_indx - 1][max(start, 0) : min(stop, len(line))]} -> {total}")
                    
                    break

print(total)
#        if symbols.find(character) != -1:
#            value = check_adjacent(char_indx, line_indx)
#            print(f"sum around {char_indx, line_indx} ({character}) is {value}")