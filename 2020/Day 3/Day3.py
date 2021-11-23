import itertools

f = open("Day3.txt", "r")

data = [x.strip() for x in f.readlines()]

f.close()

# Part 1
def part1(data):
    x = 0
    collisions = 0
    map_width = len(data[0])
    map_height = len(data)
    for y in range (map_height):
        if data[y][x] == '#':
            collisions += 1
        x = (x + 3) % map_width
    return collisions 


print("Solution part 1: %d" % part1(data))
# Part 2
def part2(data, x_slope, y_slope):
    x = 0
    y = 0
    collisions = 0
    map_width = len(data[0])
    map_height = len(data)
    while y < map_height:
        if data[y][x] == '#':
            collisions += 1
        x = (x + x_slope) % map_width
        y = y + y_slope
    return collisions 

coll1 = part2(data, 1, 1)
coll2 = part2(data, 3, 1)
coll3 = part2(data, 5, 1)
coll4 = part2(data, 7, 1)
coll5 = part2(data, 1, 2)

print("Solution part2: " , coll1*coll2*coll3*coll4*coll5)
