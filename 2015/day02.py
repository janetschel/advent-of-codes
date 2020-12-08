class Wrapping:
    _width: int
    _length: int
    _height: int

    def __init__(self, length, width, height):
        self._length = int(length)
        self._width = int(width)
        self._height = int(height)

    def calculate_needed_wrapping(self) -> int:
        wrapping: int = 2 * self._length * self._width + 2 * self._width * self._height + 2 * self._height * self._length
        return wrapping + self._calculate_smallest_side()

    def _calculate_smallest_side(self) -> int:
        return min(self._length * self._width, self._width * self._height, self._length * self._height)

    def calculate_needed_ribbon(self) -> int:
        smallest_perimiter: int = self._calculate_smallest_perimiter()
        cubic_volume: int = self._calculate_cubic_volume()

        return smallest_perimiter + cubic_volume

    def _calculate_smallest_perimiter(self) -> int:
        all_sides: [int, int, int] = [self._length, self._width, self._height]
        largest_side: int = max(all_sides)
        all_sides.remove(largest_side)

        total: int = sum([side * 2 for side in all_sides])
        return total

    def _calculate_cubic_volume(self) -> int:
        return self._length * self._width * self._height


with open("./inputs/day02.in") as file:
    wrappings: [Wrapping] = [Wrapping(*line.strip().split("x")) for line in file]

assert Wrapping(*("2x3x4".strip().split("x"))).calculate_needed_wrapping() == 58
assert Wrapping(*("1x1x10".strip().split("x"))).calculate_needed_wrapping() == 43

assert Wrapping(*("2x3x4".strip().split("x"))).calculate_needed_ribbon() == 34
assert Wrapping(*("1x1x10".strip().split("x"))).calculate_needed_ribbon() == 14

total: int = 0
total_ribbon: int = 0
for wrapping in wrappings:
    total += wrapping.calculate_needed_wrapping()
    total_ribbon += wrapping.calculate_needed_ribbon()

print("Part 1: Total wrapping needed:", total, "sq.ft")
print("Part 2: Total ribbon needed:", total_ribbon, "ft")
