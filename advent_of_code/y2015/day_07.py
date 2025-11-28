"""
Day 7: Some Assembly Required
https://adventofcode.com/2015/day/7

Simulate a circuit with bitwise logic gates. Determine the signal ultimately provided to 
wire 'a' by processing wire connection and gate operation instructions, using 16-bit 
signals and operations like AND, OR, LSHIFT, RSHIFT, and NOT.

Part 2:
Override wire 'b' with the signal from wire 'a' in part 1, then reset all other wires 
and re-run the circuit. What new signal is provided to wire 'a'?
"""

from advent_of_code.utils.file import get_contents, get_raw_contents

def part_1():
    data = get_contents("data/2015/day_07.data")
    # Solution for part 1
    pass

def part_2():
    data = get_contents("data/2015/day_07.data")
    # Solution for part 2
    pass

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())