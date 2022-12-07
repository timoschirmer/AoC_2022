import re

file = open('input', 'r')

list = [str(line).rstrip('\n').strip('$ ') for line in file]

print(list)

path = []

def pwd(pathList):
    pwd = "/"
    for p in pathList:
        pwd = pwd + p + "/"
    return pwd

#cd ordnername
def dDown(name):
    path.append(name)
    return


#cd ..
def dUp():
    del path[len(path) - 1]
    return

for command in list:
    if re.search("cd", command):
        cd, newDirectory = command.split()
        dDown(newDirectory)
    elif
