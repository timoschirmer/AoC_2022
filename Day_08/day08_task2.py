file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

counter = (len(list)*2 + len(list[0])*2 - 4)

highScore = 0

for lineIndex, line in enumerate(list):
    if lineIndex == 0 or lineIndex == (len(list) - 1):
        continue
    for treeIndex, tree in enumerate(line):
        if treeIndex == 0 or treeIndex == (len(line) - 1):
            continue

        visibleLeft = 0
        for i in reversed(range(0, treeIndex)):
            #print("left" + list[lineIndex][i] + str(i))
            if tree > list[lineIndex][i]:
                visibleLeft += 1
            elif tree <= list[lineIndex][i]:
                visibleLeft += 1
                break

        visibleRight = 0
        for i in range(treeIndex + 1, (len(line))):
            #print("right" + list[lineIndex][i] + str(i))
            if tree > list[lineIndex][i]:
                visibleRight += 1
            elif tree <= list[lineIndex][i]:
                visibleRight += 1
                break


        visibleTop = 0
        for i in reversed(range(0, lineIndex)):
            #print("top" + list[i][treeIndex] + str(i))
            if tree > list[i][treeIndex]:
                visibleTop += 1     
            elif tree <= list [i][treeIndex]:
                visibleTop += 1
                break   

        visibleBottom = 0
        for i in range(lineIndex + 1, len(list)):
            #print("bottom" + list[i][treeIndex] + str(i))
            if tree > list[i][treeIndex]:
                visibleBottom += 1
            elif tree <= list[i][treeIndex]:
                visibleBottom += 1
                break

        score = visibleBottom * visibleTop * visibleLeft * visibleRight
        if score > highScore:
            highScore = score

        #print(f"{visibleLeft} * {visibleTop} * {visibleRight} * {visibleBottom} = " + str(score))

print(highScore)
