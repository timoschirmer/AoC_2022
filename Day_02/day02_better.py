file = open('input', 'r')
list = [str(line).rstrip('\n') for line in file]

points = []
points2 = []

def myHand(m):
    if m == "A":
        return 1
    elif m == "B":
        return 2
    elif m == "C":
        return 3

for index2, zug in enumerate(list):
    you, me = zug.split()
    if me == "Y":
        points2.append(3)
        me = you
    elif me == "X":
        points2.append(0)
        if you == "A":
            me = "C"
        elif you == "B":
            me = "A"
        elif you == "C":
            me = "B"
    elif me == "Z":
        points2.append(6)
        if you == "A":
            me = "B"
        elif you == "B":
            me = "C"
        elif you == "C":
            me = "A"

    points2[index2] += myHand(me)

list = [i.replace('X','A').replace('Y','B').replace('Z','C') for i in list]
for index, zug in enumerate(list):
    you, me = zug.split()
    if you == me:
        points.append(3)
    elif (you == "A" and me == "C") or (you == "B" and me == "A") or (you == "C" and me == "B"):
        points.append(0)
    elif (you == "A" and me == "B") or (you == "B" and me == "C") or (you == "C" and me == "A"):
        points.append(6)

    points[index] += myHand(me)

print(sum(points))
print(sum(points2))