# This part does not have a file input, instead it has a small input string
import hashlib

puzzle_input = "bgvyzdsv"

# Need to MD5 hash the above input  
# How on earth does an MD5 hash work? 


def Part1(key):
    coin = 0
    while not hashlib.md5((key+str(coin)).encode("utf-8")).hexdigest().startswith("00000"):
        coin += 1
    return coin


print("Solution to Part 1: %d" % Part1(puzzle_input))


def Part2(key):
    coin = 0
    while not hashlib.md5((key+str(coin)).encode("utf-8")).hexdigest().startswith("000000"):
        coin += 1
    return coin


print("Solution to Part 2: %d" % Part2(puzzle_input))

