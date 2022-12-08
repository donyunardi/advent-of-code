import os
import string
from os.path import join

c1 = []
c2 = []
c3 = []

with open(join(os.getcwd(), "2022/day3_input.txt"), "r") as input_file:
    lines = input_file.read().splitlines()

for line in lines:
    rucksack = len(line)
    half_rucksack = int(rucksack/2)

    c1.append(list(set(line[:half_rucksack])))
    c2.append(list(set(line[half_rucksack:])))

for i in range(0,len(c1)):
    for j in c1[i]:
        if j in c2[i]:
            c3.append(j)

letters = string.ascii_letters
temp = 0
for item in c3:
    temp += letters.index(item)+1

# Answer to Part 1
print(temp)

lines = [ list(set(i)) for i in lines]

c5 = []
counter = 3
for i in range(0, len(lines), 3):
    c5.append(lines[i:counter])
    counter += 3

c6 = []

for i in c5:
    for j in i[0]:
        if j in i[1] and j in i[2]:
            c6.append(j)

temp = 0
for item in c6:
    temp += letters.index(item)+1

# Answer to Part 2
print(temp)
