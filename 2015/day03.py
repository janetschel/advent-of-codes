from typing import NamedTuple as nt

with open("./inputs/day03.in") as file:
    directions: [str] = [direction for line in file for direction in line]

def deliver(directions: [str]) -> int:
    current_pos: nt = (0, 0)
    visited: {nt} = {current_pos}

    for direction in directions:
        current_pos = calculate_new_pos(direction, current_pos)
        visited.add(current_pos)
    
    return len(visited)


def deliverPart2(directions: [str]) -> int:
    starting_pos: nt = (0, 0)
    current_pos_santa = current_pos_robot = starting_pos

    visited_santa: {nt} = {starting_pos}
    visited_robot: {nt} = set()

    for index, direction in enumerate(directions):
        if index % 2 == 0:
            current_pos_santa = calculate_new_pos(direction, current_pos_santa)
            visited_santa.add(current_pos_santa)
        else:
            current_pos_robot = calculate_new_pos(direction, current_pos_robot)
            visited_robot.add(current_pos_robot)

    return len(visited_santa | visited_robot)


def calculate_new_pos(direction: str, current_pos: nt) -> nt:
    (x, y) = current_pos

    if direction == "^":
        return (x, y + 1)
    elif direction == "v":
        return (x, y - 1)
    elif direction == ">":
        return (x + 1, y)
    elif direction == "<":
        return (x - 1, y)
    else:
        raise("Invalid direction")


assert deliver([">"]) == 2
assert deliver(["^", ">", "v", "<"]) == 4
assert deliver(["^", "v", "^", "v", "^", "v", "^", "v", "^", "v"]) == 2

assert deliverPart2(["^", "v"]) == 3
assert deliverPart2(["^", ">", "v", "<"]) == 3
assert deliverPart2(["^", "v", "^", "v", "^", "v", "^", "v", "^", "v"]) == 11

at_least_one_present = deliver(directions)
print("Part 1: Number of houses which got at least one present:", at_least_one_present)

at_least_one_present_with_helper = deliverPart2(directions)
print("Part 2: Number of houses which got at least one present:", at_least_one_present_with_helper)
