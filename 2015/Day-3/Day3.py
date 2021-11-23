# import file

f = open("input.txt", "r")

data = [x.strip() for x in f.read()]

f.close()

# Part 1
# Input will be a mix of v^><. 
# Each will dictate the next house to receive presents 
# Only one instruction dictates the current house, and the house you land on
# Determine how many houses get at least a single present 

def Part1(data):
    # Begin Part 1 of Day 3, Advent of Code 2015

    coordinate = [0,0]
    visited_houses = []
    visited_houses.append(coordinate)
    x, y = coordinate

    for step in data:
        if step == 'v': 
            y -= 1
        if step == '^': 
            y += 1
        if step == '<':
            x -= 1
        if step == '>':
            x += 1

        coordinate = [x, y]
        
        if coordinate not in visited_houses:
            visited_houses.append(coordinate)

    return len(visited_houses)

print("Solution to Part 1: %d" % Part1(data))

def Part2(data):
    # Begin Part 2 of Day 3, Advent of Code 2015

    coordinate = [0, 0]
    visited_houses = []
    visited_houses.append(coordinate)
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0
    counter = 1

    for step in data:

        if (counter % 2) == 0:
            # insert robo santa logic
            if step == 'v':
                robo_y -= 1
            if step == '^':
                robo_y += 1
            if step == '<':
                robo_x -= 1
            if step == '>':
                robo_x += 1

            coordinate = [robo_x, robo_y]

            if coordinate not in visited_houses:
                visited_houses.append(coordinate)
        else: 
            # insert real santa logic
            if step == 'v':
                santa_y -= 1
            if step == '^':
                santa_y += 1
            if step == '<':
                santa_x -= 1
            if step == '>':
                santa_x += 1

            coordinate = [santa_x, santa_y]

            if coordinate not in visited_houses:
                visited_houses.append(coordinate)

        counter += 1

    return len(visited_houses)

print("Solution to Part 2: %d" % Part2(data))
