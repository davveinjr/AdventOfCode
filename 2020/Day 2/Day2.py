import collections

the_list = list()

f = open("Day2.txt", "r")

for x in f:
    the_list.append(x)

f.close()

# Part 1
total_part_one = 0

for line in the_list:
    the_range, middle, the_pw = line.split()
    the_min, the_max = the_range.split('-')
    target = middle[0]

    d = collections.defaultdict(int)
    for c in the_pw:
        d[c] += 1

    if int(the_min) <= d[target] <= int(the_max):
        total_part_one += 1

print(total_part_one)

# Part 2
total_part_two = 0

for line in the_list:
    the_range, middle, the_pw = line.split()
    location_one, location_two = the_range.split('-')
    target = middle[0]

    if len(the_pw) >= int(location_two):
        if the_pw[int(location_one) - 1] == target and the_pw[int(location_two) - 1] != target:
            total_part_two += 1
        elif the_pw[int(location_one) - 1] != target and the_pw[int(location_two) - 1] == target:
            total_part_two += 1
    elif int(location_one) <= len(the_pw) <= int(location_two):
        if the_pw[int(location_one) - 1] == target and the_pw[int(location_two) - 1] != target:
            total_part_two += 1

print(total_part_two)
