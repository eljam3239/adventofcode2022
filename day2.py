#left colums opponenet: a for rock b for paper c for scissors
#right column is you: x for rock, y for paper, z for scissors
#score = shape you selected (1/2/3 -> r/p/s) + outcome(L: 0, D: 3, W: 6)

total_score = 0

input = open('inputday2.txt', 'r')

Lines = input.readlines()