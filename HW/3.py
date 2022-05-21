# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные: 'ываабв лповап абвцукв алоабвабв ываываыв'
# Выходные данные: 'лповап ываываыв'

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')



# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

def prog(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def deprog(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст кодировки: ")
print(f"Текст после кодировки: {prog(s)}")
print(f"Текст после дешифровки: {deprog(prog(s))}")

# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

print('Введите последовательность целых чисел одной строкой. Разделитель - пробел')
a = input()
dt = a.split()
dt = list(map(int, dt ))

unique = [item for item in dt if dt.count(item) == 1]
print(unique)