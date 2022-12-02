file = open('input', 'r')
list = [str(line).rstrip('\n') for line in file]
list = [i.replace('X','A').replace('Y','B').replace('Z','C') for i in list]

points = []

for index, zug in enumerate(list):
    you, me = zug.split()
    if you == me:
        points.append(3)
    elif (you == "A" and me == "C") or (you == "B" and me == "A") or (you == "C" and me == "B"):
        points.append(0)
    elif (you == "A" and me == "B") or (you == "B" and me == "C") or (you == "C" and me == "A"):
        points.append(6)

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