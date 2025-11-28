"""
Day 6: Probably a Fire Hazard
https://adventofcode.com/2015/day/6

Manage a 1000x1000 grid of lights with instructions to "turn on", "turn off", or "toggle" 
lights in specific rectangular ranges. Determine how many lights are lit after following 
all instructions.

Part 2:
Instead of simple on/off states, lights have brightness levels. "Turn on" increases 
brightness by 1, "turn off" decreases by 1 (minimum 0), and "toggle" increases by 2. 
Calculate the total brightness.
"""

from advent_of_code.utils.file import get_contents, get_raw_contents

def part_1():
    data = get_contents("data/2015/day_06.data")
    # Solution for part 1
    pass

def part_2():
    data = get_contents("data/2015/day_06.data")
    # Solution for part 2
    pass

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())