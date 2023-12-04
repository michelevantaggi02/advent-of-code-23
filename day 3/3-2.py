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

def check_adjacent(x: int, y: int) -> int:
    checks = {"top_left" : (-1, -1), "top" : (0, -1), "top_right" : (1, -1), "left" : (-1, 0), "right" : (1, 0), "bottom_left" : (-1, 1), "bottom" : (0, 1), "bottom_right" : (1, 1)}
    possible_checks = list(checks.keys())
    if x == 0:
        possible_checks.remove("top_left")
        possible_checks.remove("left")
        possible_checks.remove("bottom_left")
    elif x == line_length -1:
        possible_checks.remove("top_right")
        possible_checks.remove("right")
        possible_checks.remove("bottom_right")
    if y == 0:
        if x != 0:
            possible_checks.remove("top_left")
        possible_checks.remove("top")
        if x != line_length - 1:
            possible_checks.remove("top_right")
    if y == len(lines) -1:
        if x != 0:
            possible_checks.remove("bottom_left")
        possible_checks.remove("bottom")
        if x != line_length -1:
            possible_checks.remove("bottom_right")
    numbers = []
    total = 0
    for move in possible_checks:
        positions = checks[move]
        position_checked = lines[y + positions[1]][x + positions[0]]
        if position_checked.isdigit():
            number, start, stop = retrieve_full_number(lines[y + positions[1]], x + positions[0])
            
            #print(f"{lines[y + positions[1]][start + 1: stop - 1]} is a number adjacent on {move}")
            if not number in numbers:
                numbers.append(number)
    if len(numbers) == 2:
        #print(f"{numbers} are adjacent to {lines[y][x]}")
        total += numbers[0] * numbers[1]
    return total

symbols = "$%&/*-+@=#"

total = 0

for line_indx, line in enumerate(lines):
    stop = 0
    for char_indx, character in enumerate(line):
        if character == "*":
            #print(f"character at [{char_indx}, {line_indx}] is {character} ({line[char_indx]})")
            total += check_adjacent(char_indx, line_indx)

print(total)