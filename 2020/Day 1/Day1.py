import itertools

the_list = list()

f = open("day1.txt", "r")

for x in f:
    the_list.append(x)

f.close()

# Part 1
for a, b in itertools.combinations(the_list, 2):
    if int(a) + int(b) == 2020:
        print(int(a) * int(b))

# Part 2
for a, b, c in itertools.combinations(the_list, 3):
    if int(a) + int(b) + int(c) == 2020:
        print(int(a) * int(b) * int(c))
