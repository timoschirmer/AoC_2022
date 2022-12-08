file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

counter = (len(list)*2 + len(list[0])*2 - 4)
print(counter)

for lineIndex, line in enumerate(list):
    if lineIndex == 0 or lineIndex == (len(list) - 1):
        continue
    for treeIndex, tree in enumerate(line):
        if treeIndex == 0 or treeIndex == (len(line) - 1):
            continue

        visibleLeft = True
        for i in range(0, treeIndex):
            #print("left" + list[lineIndex][i] + str(i))
            if tree <= list[lineIndex][i]:
                visibleLeft = False

        visibleRight = True
        for i in range(treeIndex + 1, (len(line))):
            #print("right" + list[lineIndex][i] + str(i))
            if tree <= list[lineIndex][i]:
                visibleRight = False


        visibleTop = True
        for i in range(0, lineIndex):
            #print("top" + list[i][treeIndex] + str(i))
            if tree <= list[i][treeIndex]:
                visibleTop = False        

        visibleBottom = True
        for i in range(lineIndex + 1, len(list)):
            #print("bottom" + list[i][treeIndex] + str(i))
            if tree <= list[i][treeIndex]:
                visibleBottom = False

        if visibleBottom == False and visibleLeft == False and visibleRight == False and visibleTop == False:
            print(f"Tree {tree} is not visible")
        else:
            print(f"Tree {tree} is visible")
            counter += 1

        #print(f"left{visibleLeft} top{visibleTop} right{visibleRight} bottom{visibleBottom}")

print(counter)