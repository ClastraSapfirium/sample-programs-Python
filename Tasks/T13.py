# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def Set_Creating(s):
    set1 = set()
    for item in s:
        set1.add(item)
    return set1

a = input('Введите строку 1 с любыми неповторяющимися значениями: ')
b = input('Введите строку 2 с любыми неповторяющимися значениями: ')
print(Set_Creating(a).intersection(Set_Creating(b)))
print(f'Количество вхождений строки 1 в строке 2: {len(Set_Creating(a).intersection(Set_Creating(b)))}')