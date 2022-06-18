#Подсчитать сумму цифр в вещественном числе
#help(list)

def Numb_Sum(n):
    numbs = []
    for i in n:
        numbs.append(i)
    for i in numbs:
        if i == '.':
            numbs.remove('.')
        elif i== ',':
            numbs.remove(',')
    s = 0
    for i in numbs:
        s+=int(i)
    return s
a = input('Введите вещественное число ')
print(f'Сумма цифр введенного Вами числa равна: {Numb_Sum(a)}')