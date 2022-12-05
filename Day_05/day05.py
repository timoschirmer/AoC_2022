import re

file = open('input', 'r')

moves = []
ship =[]
emptyLine = False

for line in file:
    line = str(line).rstrip('\n')
    if emptyLine == True:
        moves.append(line)
    elif line == '':
        emptyLine = True
    else:
        ship.append(line)

shipLength = ship[len(ship) - 1]
shipLength = int(shipLength[len(shipLength) - 2:])
del ship[len(ship) - 1]

container = []
for i in range(shipLength):
    container.append([])


for element in ship:
    counter = 0
    cont = 0
    #print(element)
    for character in element:
        if counter == 3:
            counter = 0
            cont += 1
        elif character == '[' or character == ']' or character == ' ':
            counter += 1
        elif character.isupper():
            container[cont].append(character)
            counter += 1


for index, move in enumerate(moves):
    moves[index] = re.findall(r'\d+', move)

#Task 1
""" for move in moves:
    for i in range(int(move[0])):
        container[int(move[2]) - 1].insert(0, container[int(move[1]) - 1][0])
        del container[int(move[1]) - 1][0] """

#Task 2
for move in moves:
    for i in range(int(move[0])):
        container[int(move[2]) - 1].insert(i, container[int(move[1]) - 1][0])
        del container[int(move[1]) - 1][0]
        

task = ''
for c in container:
    task = task + c[0]


print(task)





