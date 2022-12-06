import os
from os.path import join
total_calories = []
temp = 0
with open(join(os.getcwd(), "2022/p1_input.txt"), "r") as input_file:
    input_data = input_file.read().splitlines()

for calories in input_data:
    if calories != "":
        temp += int(calories)
    else:
        total_calories.append(temp)
        temp = 0

print(max(total_calories))
