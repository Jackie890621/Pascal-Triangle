#Execution : python3.9 
import math

n = input("Please input the height of your Pascal triangle: ")
n = int(n)
number = list()
size = list()
for i in range(n + 1):
    number.append([])
    temp = 0
    temp += i
    if (i == 0):
        number[i].append(1)
        size.append(1)
        continue
    else:
        for j in range(i + 1):
            number[i].append(math.comb(i, j))
            temp += len(str(math.comb(i, j)))
    size.append(temp)

for i in range(n + 1):
    for j in range((size[n] - size[i]) // 2):
        print(end = ' ')
    for j in range(len(number[i])):
        print(number[i][j], end = ' ')
    print()
