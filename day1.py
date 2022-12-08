calories = []
input = open('input.txt', 'r')
lines = input.readlines()


cals=0
for line in lines:
    if line != '\n':
        #print(line)
        cals+=int(line)
    if line.isspace() or line == '\n':
        calories.append(cals)
        cals=0

print(calories)
print(max(calories))

calories.sort()
#print(calories[-4:-1])
top3 = calories[-3]+calories[-2]+calories[-1]
print(top3)