f = open("Day4.txt", "r")

data = [x.strip() for x in f.readlines()]

f.close()

##Imports:
# byr - Birth Year
# iyr - Issue Year 
# eyr - Expiration Year
# hgt - Height
# hcl - Hair Color
# ecl - Eye Color
# pid - Passport ID
# cid - Country ID

## Part 1
def Part1(data):
    #Parse Data
    #with open("Day4.txt", "r"):
    total_valid = req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    current = 0
    for line in data:
        if line == '':
            if current == len(req_fields):
                total_valid += 1
            current = 0
            continue
            
        #split key/value pair, check if in req_fields
        for pair in line.split():
            key, value = pair.split(':')
            if key in req_fields:
                current += 1

    return total_valid

# print("Solution to Part 1: %d" % Part1(data))
## Part 2

# def validate():
def validate(passport):
    is_valid = True
    for key in passport:
        if(key == "byr"):
           year = int(passport[key])
           if 1920 <= year <= 2002:
               continue
           else:
               is_valid = False
               break
        elif(key == "iyr"):
            year = int(passport[key])
            if 2010 <= year <= 2020:
                continue
            else:
                is_valid = False
                break
        elif(key == "eyr"):
            year = int(passport[key])
            if 2020 <= year  <= 2030:
                continue
            else:
                is_valid = False
                break
        elif(key == "hgt"):
            #input height validation logic here
            if('cm' in passport[key]):
                cm_hgt = int(passport[key].removesuffix('cm'))
                if 150 <= cm_hgt <= 193:
                    continue
                else: 
                    is_valid = False
                    break
            elif ('in' in passport[key]):
                in_hgt = int(passport[key].removesuffix('in'))
                if 59 <= in_hgt <= 76:
                    continue
                else:
                    is_valid = False
                    break
            else:
                is_valid = False
                break
        elif(key == "hcl"):
            if passport[key][0] != '#':
                is_valid = False
                break
            else: 
                hair_color = passport[key][1:]
                if(int(hair_color, 16)):
                    continue
                else: 
                    is_valid = False
                    break
        elif(key == "ecl"):
            colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if passport[key] in colors:
                continue
            else: 
                is_valid = False
                break
        elif(key == "pid"):
            if len(passport[key]) == 9:
                if passport[key].isnumeric():
                    continue
                else:
                    is_valid = False
                    break
            else:
                is_valid = False
                break

    return is_valid

def Part2(data):

    total_valid = 0
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passport = {} 
    current = 0
    for line in data:
        if line == '':
            if current == len(req_fields):
                # Validate the entries using the newly built passport dict   
                if validate(passport):
                    total_valid += 1
            passport.clear()
            current = 0
            continue
            
        #split key/value pair, check if in req_fields
        for pair in line.split():
            key, value = pair.split(':')
            if key in req_fields:
                passport[key] = value
                current += 1

    return total_valid

print("Solution to part 2 is: %d" % Part2(data))
