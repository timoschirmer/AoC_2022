file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

top = 0
counter = 0
for n in list:
    if n == "" and counter < top:
        counter = 0
    elif n == "" and counter > top:
        top = counter
        counter = 0
    else:
        counter += int(n)

print(top)