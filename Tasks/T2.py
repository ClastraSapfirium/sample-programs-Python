#Найти максимальное из пяти чисел

def Find_Max(a,b,c,d,e):
    max = a
    if b>max:
        max = b
    if c>max:
        max = c
    if d>max:
        max = d
    if e>max:
        max = e
    return max

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))
d = int(input('Введите четвертое число '))
e = int(input('Введите пятое число '))

print('Максимум равен ', Find_Max(a,b,c,d,e))