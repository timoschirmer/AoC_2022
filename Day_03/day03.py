from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def findPriorities(i):
    if i.isupper():
        return(ord(i) - 38)
    if i.islower():
        return(ord(i) - 96)

file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

items = []
priorities = []

for l in list:
    bp1, bp2 = l[:len(l)//2], l[len(l)//2:]

    letter = ''.join(set(bp1).intersection(bp2))

    items.append(letter)
    priorities.append(findPriorities(letter))

print(f"Task1: {sum(priorities)}")


items = []
priorities = []

for x, y, z in grouper(list, 3):
    letter = ''.join(set(x).intersection(y).intersection(z))
    items.append(letter)
    priorities.append(findPriorities(letter))


print(f"Task2: {sum(priorities)}")

