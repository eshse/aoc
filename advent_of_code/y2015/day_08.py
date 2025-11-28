"""
Day 8: Matchsticks
https://adventofcode.com/2015/day/8

Calculate the difference between the number of characters in the code representation 
of string literals and the actual characters in memory. Handle escape sequences like 
\\, \", and \x with hexadecimal characters.

Part 2:
Calculate the difference when encoding the strings by escaping special characters. 
Find the total increase in character count when properly encoding all strings.
"""

from advent_of_code.utils.file import get_contents, get_raw_contents

def part_1():
    data = get_contents("data/2015/day_08.data")
    # Solution for part 1
    pass

def part_2():
    data = get_contents("data/2015/day_08.data")
    # Solution for part 2
    pass

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())