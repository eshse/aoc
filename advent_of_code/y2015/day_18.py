"""
Day 18: Like a GIF For Your Yard

Animate a 100x100 grid of lights where each light's next state depends on its current 
state and the number of adjacent lights that are on. Lights follow specific rules: 
on lights stay on with 2-3 neighbors, off lights turn on with exactly 3 neighbors. 
Count how many lights are on after 100 steps.

Part 2:
The four corner lights are stuck on and can't be turned off. With this constraint, 
how many lights are on after 100 steps?
"""

from advent_of_code.utils.file import get_contents, get_raw_contents

def part_1():
    data = get_contents("data/2015/day_18.data")
    # Solution for part 1
    pass

def part_2():
    data = get_contents("data/2015/day_18.data")
    # Solution for part 2
    pass

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())