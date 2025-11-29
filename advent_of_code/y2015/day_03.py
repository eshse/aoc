"""
Day 3: Perfectly Spherical Houses in a Vacuum
https://adventofcode.com/2015/day/3

Santa delivers presents on a 2D grid, starting at his initial location. He moves north (^), 
south (v), east (>), or west (<), delivering a present at each new house. Count how many 
unique houses receive at least one present.

Part 2:
Santa and Robo-Santa start at the same location and take turns following the directions. 
Count how many unique houses receive at least one present from either Santa or Robo-Santa.
"""

from dataclasses import dataclass

from advent_of_code.utils.file import get_contents, get_raw_contents

data = get_contents("data/2015/day_03.data")[0]

@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def go_north(self):
        return Position(self.x, self.y + 1)

    def go_east(self):
        return Position(self.x + 1, self.y)

    def go_south(self):
        return Position(self.x, self.y - 1)

    def go_west(self):
        return Position(self.x - 1, self.y)


def part_1():
    position = Position(0, 0)
    positions = {position}  # Use a set from the start

    for move in data:
        match move: 
            case '^':
                position = position.go_north()
            case '>':
                position = position.go_east()
            case 'v':
                position = position.go_south()
            case '<':
                position = position.go_west()
            case _:
                raise ValueError()
    
        positions.add(position)
    
    print(len(positions))

def part_2():
    santa_position = Position(0, 0)
    robo_santa_position =  Position(0, 0)
    positions = {santa_position}

    for i, move in enumerate(data):
        if i % 2 == 0:
            match move: 
                case '^':
                    santa_position = santa_position.go_north()
                case '>':
                    santa_position = santa_position.go_east()
                case 'v':
                    santa_position = santa_position.go_south()
                case '<':
                    santa_position = santa_position.go_west()
                case _:
                    raise ValueError()
    
            positions.add(santa_position)
        else:
            match move: 
                case '^':
                    robo_santa_position = robo_santa_position.go_north()
                case '>':
                    robo_santa_position = robo_santa_position.go_east()
                case 'v':
                    robo_santa_position = robo_santa_position.go_south()
                case '<':
                    robo_santa_position = robo_santa_position.go_west()
                case _:
                    raise ValueError()
    
            positions.add(robo_santa_position)

    print(len(positions))

if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())