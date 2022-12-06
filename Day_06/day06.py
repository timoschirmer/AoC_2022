file = open('input', 'r')
stream = file.read()

#String abcd --> d: last character

def hasNoDuplicates(lst):
    s = set()
    for elem in lst:
        if elem in s:
            return False
        s.add(elem)
    return True

def findDistinctCharacters(length):
    test = []
    for i in range(length):
        test.append('')

    for counter, char in enumerate(stream):
        test.append(char)
        del test[0]
        #print(f"index:{counter}\t{test}")

        if hasNoDuplicates(test) and counter >= length:
            return(counter + 1)


print(f"Task1: {findDistinctCharacters(4)}\tTask2: {findDistinctCharacters(14)}")





