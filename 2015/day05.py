with open("./inputs/day05.in") as file:
    strings: [str] = [line for line in file]

def is_nice_string(string: str) -> bool:
    checks: [bool] = [
        _contains_vowels(string), 
        _contains_neighboring_char(string),
        _does_not_contain_substrings(string)
    ]

    return all(checks)


def is_nice_string_part2(string: str) -> bool:
    checks: [bool] = [
        _has_group_of_repeating_chars(string), 
        _has_repeating_letter_split(string),
    ]

    return all(checks)


def _contains_vowels(string: str) -> bool:
    chars: {str} = {}
    for char in string:
        if char not in chars:
            chars[char] = 0
        
        chars[char] += 1

    return _vowels_present(chars)


def _contains_neighboring_char(string: str) -> bool:
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True

    return False


def _does_not_contain_substrings(string: str) -> bool:
    return "ab" not in string and "cd" not in string and "pq" not in string and "xy" not in string


def _vowels_present(chars: {}) -> bool:
    vowel_count: [int] = [chars.get(vowel) for vowel in "aeiou"]
    return sum([0 if num == None else num for num in vowel_count]) >= 3


def _has_group_of_repeating_chars(string: str) -> bool:
    for i in range(len(string) - 1):
        possible_repeating: str = string[i] + string[i + 1]
        for j in range(i + 2, len(string) - 1):
            if string[j] + string[j + 1] == possible_repeating:
                return True

    return False


def _has_repeating_letter_split(string: str) -> bool:
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True

    return False


assert is_nice_string("ugknbfddgicrmopn")
assert is_nice_string("aaa")
assert not is_nice_string("jchzalrnumimnmhp")
assert not is_nice_string("haegwjzuvuyypxyu")
assert not is_nice_string("dvszwmarrgswjxmb")

assert is_nice_string_part2("qjhvhtzxzqqjkmpb")
assert is_nice_string_part2("xxyxx")
assert not is_nice_string_part2("uurcxstgmygtbstg")
assert not is_nice_string_part2("ieodomkazucvgmuy")

nice_strings_pt1: int = 0
nice_strings_pt2: int = 0
for string in strings:
    nice_strings_pt1 += 1 if is_nice_string(string) else 0
    nice_strings_pt2 += 1 if is_nice_string_part2(string) else 0

print("Part 1 nice strings", nice_strings_pt1)
print("Part 2 nice strings", nice_strings_pt2)
