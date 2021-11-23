# input file
f = open("input.txt", "r")

data = [x.strip() for x in f.readlines()]

f.close()

# Part 1
# Formula is 2*l*w + 2*w*h + 2*h*l
# Total amount needed at the end 
# Input will be AxBxC format
# Where A, B, C are l, w, and h

def Part1(data):
    #Begin Part 1 of Day 2, Advent of Code 2015
    l = 0
    w = 0
    h = 0
    total_square_ft = 0

    for line in data:
        l, w, h = line.split('x')
        l = int(l)
        w = int(w)
        h = int(h)

        total_square_ft += (2*l*w) + (2*w*h) + (2*h*l)
        slack = min(l*w, w*h, h*l)
        total_square_ft += slack

    return total_square_ft

print("Solution to Part 1: %d" % Part1(data))

# Part 2
# Same input format
# Formula is smallest perimeter of any one face
# plus l*w*h for the bow

def Part2(data):
    # Begin Part 2 of Day 2, Advent of Code 2015
    total_length = 0 

    for line in data:
        l,w,h = line.split('x')
        measurements = [int(l), int(w), int(h)]
        measurements.sort()

        total_length += (2*measurements[0] + 2*measurements[1]) + (int(l) * int(w) * int(h))

    return total_length

print("Solution to Part 2: %d" % Part2(data))
