"""
Day 1: Secret Entrance
https://adventofcode.com/2025/day/1
"""

from dataclasses import dataclass
from enum import Enum, auto
from advent_of_code.utils.file import get_contents

class Rotation(Enum):
    LEFT = auto()
    RIGHT = auto()

@dataclass
class SafeDial:
    ended_at_zero = 0
    times_at_zero = 0

    def __init__(self, _starting_position: int = 50, _min: int = 0, _max: int = 99):
        self.current_position = _starting_position
        self.min = _min
        self.max = _max

    def rotate(self, rotation: Rotation, distance: int):
        match rotation:
            case Rotation.LEFT:
                for _ in range(distance):
                    self.current_position -= 1
                    
                    if self.current_position < self.min:
                        self.current_position = self.max
                    
                    if self.current_position == 0:
                        self.times_at_zero += 1

            case Rotation.RIGHT:
                for _ in range(distance):
                    self.current_position += 1
                    
                    if self.current_position > self.max:
                        self.current_position = self.min
                    
                    if self.current_position == 0:
                        self.times_at_zero += 1
        
        if self.current_position == 0:
            self.ended_at_zero += 1

def parse_rotation(rotation_string: str):
    rotation = rotation_string[0]
    distance = int(rotation_string[1:])

    if rotation == "R":
        return (Rotation.RIGHT, distance)
    elif rotation == "L":
        return (Rotation.LEFT, distance)
    else:
        raise ValueError("Unkown rotation")

def get_data():
    rotations = []

    data = get_contents("data/2025/day_01.data")

    for line in data:
        rotations.append(line)
    
    return rotations

# Easier to solve in one part today :) 
def part_1():
    rotations = list(map(parse_rotation, get_data()))
    safe_dial = SafeDial()

    for rotation in rotations:
        safe_dial.rotate(*rotation)

    # Part 1
    print(safe_dial.ended_at_zero)

    # Part 2
    print(safe_dial.times_at_zero)
