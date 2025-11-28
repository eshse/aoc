"""
Day 1: Not Quite Lisp
https://adventofcode.com/2015/day/1

Santa needs to find the correct floor by following instructions where "(" means going 
up one floor and ")" means going down one floor. The goal is to determine the final 
floor Santa reaches based on the input sequence of parentheses.

Part 2:
Find the position of the first character that causes Santa to enter the basement (floor -1).
"""

from advent_of_code.utils.file import get_contents, get_raw_contents

def part_1():
    data = get_contents("data/2015/day_01.data")[0]
    
    floor = 0

    for c in data:
        match c:
            case '(':
                floor += 1
            case ')':
                floor -= 1
    
    print(floor)

def part_2():
    data = get_contents("data/2015/day_01.data")[0]
    
    floor = 0

    for i, c in enumerate(data, 1):
        match c:
            case '(':
                floor += 1
            case ')':
                floor -= 1
                if floor < 0:
                    print(i)
                    break

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())