import re
import json
from collections import OrderedDict

file = open('input', 'r')

list = [str(line).rstrip('\n').strip('$ ') for line in file]


files = {}
pwd = []
for command in list:
    cmd = command.split()
    if re.search(r"cd .+", command):
        if cmd[1] == "..":
            pwd.pop()
        else:
            pwd.append(cmd[1])
    elif re.search("\d+\d.+", command):
        name = '/'.join(pwd)
        if name not in files:
            files[name] = 0
        files[name] += int(cmd[0])
    elif re.search(r"dir .+", command):
        name = '/'.join(pwd)
        if name not in files:
            files[name] = 0

sortedFiles = OrderedDict(sorted(files.items(), key=lambda key:len(key[0]), reverse=True))

for folder in sortedFiles:
    path = re.sub(r'(.+)\/.+', r'\g<1>', folder)
    tempSize = sortedFiles[folder]
    sortedFiles[path] += tempSize
sortedFiles["/"] = sortedFiles["/"] / 2


task1 = 0
for file, size in sortedFiles.items():
    if size <= 100000:
        task1 += size


sortedFiles = OrderedDict(sorted(sortedFiles.items(), key=lambda x:x[1]))

maxSpace = 70000000
updateSpace = 30000000
freeSpace = maxSpace - sortedFiles.get("/")
neededSpace = updateSpace - freeSpace

def task2(sortedFile):
    for file in sortedFile:
        if sortedFile.get(file) >= neededSpace:
            return sortedFile.get(file)


print(f"Task1: {task1}\nTask2: {task2(sortedFiles)}")
