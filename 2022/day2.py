import os
from os.path import join
p1 = []
p2 = []

with open(join(os.getcwd(), "2022/day2_input.txt"), "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        p1.append(line.split()[0])
        p2.append(line.split()[1])

counter = len(p2)

rps_value = {
    'X': 1, #Rock
    'Y': 2, #Paper
    'Z': 3  #Scissor
}

temp = 0
hand_played_score = [ rps_value[p2[i]] for i in range(0, counter) ]

game_played_score = 0

for i in range(0,counter):
    if (p1[i] == 'A' and p2[i] == 'X') or (p1[i] == 'B' and p2[i] == 'Y') or (p1[i] == 'C' and p2[i] == 'Z'):
        game_played_score += 3
    elif (p1[i] == 'C' and p2[i] == 'X') or (p1[i] == 'A' and p2[i] == 'Y') or (p1[i] == 'B' and p2[i] == 'Z'):
        game_played_score += 6
    else:
        game_played_score += 0

print(game_played_score)
print(sum(hand_played_score) + game_played_score)
