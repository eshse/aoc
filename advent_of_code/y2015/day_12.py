"""
Day 12: JSAbacusFramework.io
https://adventofcode.com/2015/day/12

Find and sum all numbers in a JSON document, which can contain arrays, objects, 
numbers, and strings.

Part 2:
Sum all numbers in the JSON document, but ignore any object (and its children) 
that has any property with the value "red".
"""

from advent_of_code.utils.file import get_contents, get_raw_contents

def part_1():
    data = get_contents("data/2015/day_12.data")
    # Solution for part 1
    pass

def part_2():
    data = get_contents("data/2015/day_12.data")
    # Solution for part 2
    pass

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())