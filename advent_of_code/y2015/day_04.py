"""
Day 4: The Ideal Stocking Stuffer
https://adventofcode.com/2015/day/4

Santa needs to "mine" AdventCoins by finding the lowest positive number that, when 
appended to a secret key, produces an MD5 hash starting with at least five zeroes.

Part 2:
Find the lowest positive number that produces an MD5 hash starting with at least six zeroes.
"""

import hashlib

key = "bgvyzdsv"

def mine(key, difficulty):
    nonce = 0
    
    while True:
        key_with_nonce = key + str(nonce)
        hash = hashlib.md5(key_with_nonce.encode()).hexdigest()
        
        if hash.startswith('0' * difficulty):
            return nonce

        nonce += 1

def part_1():
    print(mine(key, 5))


def part_2():
    print(mine(key, 6))


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())