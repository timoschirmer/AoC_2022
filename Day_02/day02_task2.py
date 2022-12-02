file = open('input', 'r')
list = [str(line).rstrip('\n') for line in file]

points = []


for index, zug in enumerate(list):
    you, me = zug.split()
    if me == "Y":
        points.append(3)
        me = you
    elif me == "X":
        points.append(0)
        if you == "A":
            me = "C"
        elif you == "B":
            me = "A"
        elif you == "C":
            me = "B"
    elif me == "Z":
        points.append(6)
        if you == "A":
            me = "B"
        elif you == "B":
            me = "C"
        elif you == "C":
            me = "A"

    if me == "A":
        points[index] += 1
    elif me == "B":
        points[index] += 2
    elif me == "C":
        points[index] += 3


print(sum(points))




# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

# X for Rock, Y for Paper, and Z for Scissors
# A for Rock, B for Paper, and C for Scissors

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.