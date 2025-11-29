"""
Day 5: Doesn't He Have Intern-Elves For This?
https://adventofcode.com/2015/day/5

Determine which strings are "nice" based on three rules:
1. Contains at least three vowels (a, e, i, o, u)
2. Has at least one letter that appears twice consecutively
3. Does not contain specific forbidden substrings (ab, cd, pq, xy)

Part 2:
New rules for "nice" strings:
1. Contains a pair of any two letters that appears at least twice without overlapping
2. Contains at least one letter which repeats with exactly one letter between them
"""

from advent_of_code.utils.file import get_contents, get_raw_contents

def _three_vowels(string: str) -> bool:
    return sum(map(string.count, 'aeiou')) >= 3


def _consecutive_letter(string: str) -> bool:
    prev_letter = None

    for c in string:
        if c == prev_letter:
            return True
        
        prev_letter = c

def _no_forbidden_substrings(string: str) -> bool:
    forbidden_substrings = ['ab', 'cd', 'pq', 'xy']

    for substring in forbidden_substrings:
        if substring in string:
            return False
    
    return True

def _is_nice(string: str) -> bool:
    return all((_three_vowels(string), _consecutive_letter(string), _no_forbidden_substrings(string)))

def part_1():
    data = get_contents("data/2015/day_05.data")
    
    nice_strings = 0

    for string in data:
        nice_strings += 1 if _is_nice(string) else 0

    print(nice_strings)

def part_2():
    data = get_contents("data/2015/day_05.data")
    # Solution for part 2
    pass

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())