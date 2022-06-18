# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

number = open("my_file.txt")
numb_contents = number.readline().split()


for i in range(len(numb_contents)):
    numb_contents[i]=int(numb_contents[i])
print (numb_contents)
for j in range(len(numb_contents)):

    if numb_contents[j] -1 == numb_contents[j-1]:
        continue
    else:
        print (numb_contents[j] - 1)