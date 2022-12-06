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
<<<<<<< HEAD
            return(counter + 1)

=======
            print(counter + 1)
            break
>>>>>>> 15c884c2bf20dc8a31b01e77d9bed1efeb09c9da

print(f"Task1: {findDistinctCharacters(4)}\tTask2: {findDistinctCharacters(14)}")





