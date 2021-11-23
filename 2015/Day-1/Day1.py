f = open("input.txt", "r")

data = [x.strip() for x in f.read()]

f.close()

# Part 1
# File of parens dictating amount traversed
# ( = Up one floor (addition)
# ) = Down one floor (subtraction)

def Part1(data):
   # Begin Part 1 of Advent of Code 2015

   total = 0
   for step in data:
       if step == '(':
           total += 1
       else:
           total -= 1
   return total

print("Solution to Part 1: %d" % Part1(data))

# Part 2
# Same rules as above
# When on floor 0 (base floor), another ) will lead to the basement (-1)
# Determine which step in the process leads to the basement

def Part2(data):
    # Begin Part 2 of Advent of Code 2015

    position = 1
    total = 0
    for step in data:
        if step == '(':
            total += 1
        else:
            total -= 1
            if total == -1:
                return(position)
        position += 1

print("Solution to Part 2: %d" % Part2(data))
