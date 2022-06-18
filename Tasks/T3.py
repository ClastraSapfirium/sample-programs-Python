#Вывести на экран числа от -N до N

a = int(input('Введите начало диапазона (отрицательное число) '))
b = int(input('Введите окончание диапазона '))

list = [a]
c = a+1
while c!=b+1:
    list.append(c)
    c+=1
print(list)