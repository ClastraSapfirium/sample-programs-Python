#Сформировать список из N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

def Sequence(n):
    i = 1
    list = [1]
    while len(list) !=n:
        i*=(-3)
        list.append(i)

    return list

a = int(input('Введите количество членов последовательности '))
print(f'Последовательность: {Sequence(a)}')