#left colums opponenet: a for rock b for paper c for scissors
#right column is you: x for rock, y for paper, z for scissors
#score = shape you selected (1/2/3 -> r/p/s) + outcome(L: 0, D: 3, W: 6)

def round_score(choice1, choice2):
    score = 0
    if choice2=='X':
        score+=1
    elif choice2=='Y':
        score+=2
    else:
        score+=3
    
    if choice1=='A' and choice2=='X':
        score+=3
    elif choice1=='A' and choice2 == 'Y':
        score+=6
    elif choice1=='A' and choice2 == 'Z':
        score+=0
    elif choice1 =='B' and choice2 =='X':
        score+=0
    elif choice1 =='B' and choice2 =='Y':
        score+=3
    elif choice1 == 'B' and choice2 == 'Z':
        score+=6
    elif choice1 == 'C' and choice2 == 'X':
        score +=6
    elif choice1 == 'C' and choice2 == 'Y':
        score+=0
    elif choice1 == 'C' and choice2 == 'Z':
        score+=3
    
    return score


total_score = 0

input = open('inputday2.txt', 'r')

#line = input.readline()
#print(line)
#choice1 = line[0]
#choice2 = line[2]
#print(choice1, choice2)

#print(round_score(choice1, choice2))

lines = input.readlines()
for line in lines:
    choice1 = line[0]
    choice2 = line[2]
    score = round_score(choice1, choice2)
    total_score+=score
print(total_score)