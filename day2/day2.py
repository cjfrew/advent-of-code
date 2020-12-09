import re

p = re.compile(r"^(\d+)-(\d+) (.): (.*)$")


def task1(file):

    count = 0
    working = 0

    with open(file, "r") as file:      
        for line in file: 
            
            line = line.strip()
            line = line.split(" ")
            
            for c in line[2]: 
                if c in line[1].split(":")[0]:
                    count += 1
            if count >= int(line[0].split("-")[0]) and count <= int(line[0].split("-")[1]):
                working += 1
            count = 0
    return working


def task2(file): 
    working = 0

    with open(file, "r") as file:      
        
        for line in file:
            (low, high, letter, password) = p.match(line.strip()).groups()
            low, high = int(low), int(high)
            if (password[low - 1] == letter) ^ (password[high - 1] == letter):
                working += 1
    return working

print(task2("data.txt"))

