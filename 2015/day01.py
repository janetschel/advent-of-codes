with open("./inputs/day01.in") as file:
    chars: [] = [character for line in file for character in line]

openPar, closePar = chars.count("("), chars.count(")")
print("Solution part 1:", abs(openPar - closePar))

def find_index(chars: []) -> int:
    floor: int = 0
    for index, char in enumerate(chars):
        floor += 1 if char == "(" else -1
        if (floor == -1):
            return index + 1

print("Solution part 2:", find_index(chars))
