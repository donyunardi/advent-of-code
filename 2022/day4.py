import os
import string
from os.path import join

with open(join(os.getcwd(), "2022/day4_input.txt"), "r") as input_file:
    lines = input_file.read().splitlines()

temp1 = []

for line in lines:
    # print(line)
    temp1.append(line.split(","))

# print(temp1)

temp2 = []

temp1l = len(temp1)

for item in range(0,temp1l):
    # print(temp1[item])
    xx1 = temp1[item][0].split("-")
    xx2 = temp1[item][1].split("-")
    # print(xx1)
    # print(xx2)
    temp1[item][0] = list(range(int(xx1[0]), int(xx1[1])+1))
    temp1[item][1] = list(range(int(xx2[0]), int(xx2[1])+1))
    # print(temp1)
    # temp2.append(range(int(xx1[0]), int(xx1[1])), range(int(xx2[0]), int(xx2[1])))

# print(temp1)
counter = 0
for x in temp1:
    if all(item in x[0] for item in x[1]):
        counter += 1
    elif all(item in x[1] for item in x[0]):
        counter += 1

# Answer Part 1
print(counter)

counter = 0
for x in temp1:
    if any(item in x[0] for item in x[1]):
        counter += 1
    elif any(item in x[1] for item in x[0]):
        counter += 1

print(counter)
