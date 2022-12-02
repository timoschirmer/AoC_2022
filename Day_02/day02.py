file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

points_task1 = []
points_task2 = []

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

# X for Rock, Y for Paper, and Z for Scissors
# A for Rock, B for Paper, and C for Scissors

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

for n in list:
    match n:
        case "A X": # 1 + 3 | AZ 3 + 0
            points_task1.append(4)
            points_task2.append(3)
        case "A Y": # 2 + 6 | AX 1 + 3
            points_task1.append(8)
            points_task2.append(4)
        case "A Z": # 3 + 0 | AY 2 + 6
            points_task1.append(3)
            points_task2.append(8)
        case "B X": # 1 + 0 | BX 1 + 0
            points_task1.append(1)
            points_task2.append(1)
        case "B Y": # 2 + 3 | BY 2 + 3
            points_task1.append(5)
            points_task2.append(5)
        case "B Z": # 3 + 6 | BZ 3 + 6
            points_task1.append(9)
            points_task2.append(9)
        case "C X": # 1 + 6 | CY 2 + 0
            points_task1.append(7)
            points_task2.append(2)
        case "C Y": # 2 + 0 | CZ 3 + 3
            points_task1.append(2)
            points_task2.append(6)
        case "C Z": # 3 + 3 | CX 1 + 6
            points_task1.append(6)
            points_task2.append(7)
        

print(sum(points_task1))
print(sum(points_task2))