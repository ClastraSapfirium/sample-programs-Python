# Написать программу, получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]


def Factorial_plus(n):
    prods = []
    f = 1
    for i in range(1,n+1):
        f*=i
        prods.append(f)
    return prods
        

a = int(input('Введите целое число '))
print(f'Набор произведений чисел от 1 до {a}: {Factorial_plus(a)}')