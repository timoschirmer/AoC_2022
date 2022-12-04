import numpy as np

file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

counter_task1 = 0
counter_task2 = 0

def createList(r1, r2):
    #return np.arange(r1, r2+1, 1)
    return [item for item in range(r1, r2+1)]

for l in list:
    elv1, elv2 = l.split(',')
    elv1_1, elv1_2 = elv1.split('-')
    elv2_1, elv2_2 = elv2.split('-')
    elv1_1, elv1_2, elv2_1, elv2_2  = int(elv1_1), int(elv1_2), int(elv2_1), int(elv2_2)
    elv1List = createList(elv1_1, elv1_2)
    elv2List = createList(elv2_1, elv2_2)

    compare = sorted(set(elv1List).intersection(elv2List))

    if compare == elv1List or compare == elv2List:
        counter_task1 += 1

    if len(compare) > 0:
        counter_task2 += 1

print(counter_task1)
print(counter_task2)