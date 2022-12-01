file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

sum_list = []
counter = 0
for n in list:
    if n == "":
        sum_list.append(counter)
        counter = 0
    else:
        counter += int(n)

sum_list.sort(reverse=True)

top_sum = sum_list[0] + sum_list[1] + sum_list[2]

print("First: ", sum_list[0], "\nSecond: ", sum_list[1], "\nThird: ", sum_list[2])
print("\nSum: ", top_sum)