"""
Day 2: I Was Told There Would Be No Math
https://adventofcode.com/2015/day/2

Calculate the total square feet of wrapping paper needed for presents. For each box 
(with dimensions l x w x h), calculate the surface area plus the area of the smallest 
side as "slack".

Part 2:
Calculate the total feet of ribbon needed. Each present needs ribbon for the smallest 
perimeter around any face plus a bow equal to the cubic volume.
"""

from advent_of_code.utils.file import get_contents, get_raw_contents

def _parse(dimensions):
    l, w, h = map(int, dimensions.split('x'))
    return l, w, h

def _calculate_surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

def _calculate_ribbon(l, w, h):
    shortest_sides = sorted([l, w, h])[:2]
    return 2 * shortest_sides[0] + 2 * shortest_sides[1]

def _calculate_bow(l, w, h):
    return l * w * h

def part_1():
    data = get_contents("data/2015/day_02.data")

    total = 0
    for dimensions in data:
        l, w, h = _parse(dimensions)
        total += _calculate_surface_area(l, w, h)
    
    print(total)

def part_2():
    data = get_contents("data/2015/day_02.data")
    
    total = 0
    for dimensions in data:
        l, w, h = _parse(dimensions)
        ribbon = _calculate_ribbon(l, w, h)
        bow = _calculate_bow(l, w, h)
        total += ribbon + bow
    
    print(total)


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())

# Test Cases
assert _calculate_ribbon(2, 3, 4) == 10
assert _calculate_bow(2, 3, 4) == 24

assert _calculate_ribbon(1, 1, 10) == 4
assert _calculate_bow(1, 1, 10) == 10