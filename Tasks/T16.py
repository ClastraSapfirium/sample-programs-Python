# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму.

def Sequence_Sum(x):
    list1 = []
    summ = 0.0
    k = 1
    for i in range(x):
        item = (1+1/k)**k
        list1.append(item)
        summ += list1[i]
        k += 1
    return summ
print('Введите количество членов последовательности ')
print('(1 + 1/n)^n')
a = int(input())
print(f'Сумма чисел последовательности равна {round(Sequence_Sum(a),2)}')