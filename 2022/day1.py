import os
from os.path import join
total_calories = []
temp = 0
with open(join(os.getcwd(), "2022/day1_input.txt"), "r") as input_file:
    input_data = input_file.read().splitlines()

print(input_data)

for calories in input_data:
    if calories != "":
        temp += int(calories)
    else:
        total_calories.append(temp)
        temp = 0

if temp != 0:
    total_calories.append(temp)

# Answer to Part #1
print(max(total_calories))

# print(total_calories)
total_calories.sort(reverse=True)
print(total_calories)
print(total_calories[0:3])
print(sum(total_calories[0:3]))
