# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# list = [33,76,34,1,6,88,77,24,66]
# s=0
# sum=0
# for i in list:
#     s+=1
#     if s%2==0:
#         sum = sum + i
# print(sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# list = [33,76,34,1,6,88,77,24,66]
# s=0
# d=0
# sum=0
# for i in list:
#     s+=1
# sum = i
# while (s!=d):
#     for i in list:
#         print(i + sum)
#         d+=1


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# list = [1.23, 6.554, 9.4, 9.99, 1.677, 7.44]
# a=0
# b=0
# for i in list:
#     if (i>a):
#         while (i>a):
#             a=a+1
#     b = (i-(a-1))
#     print (b)
#     a=0

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# print("Ведите десятичное число:")
# a = int(input())
# b = ''
# while a > 0:
#     b = str(a % 2) + b
#     a = a // 2
# print(b)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# a = b = 1
# print ('Введите количество чисел Фибоначчи:')
# n = int(input())
# print(a, b, end=' ')
# for i in range(2, n):
#     a, b = b, a + b
#     print(b, end=' ')

# Не могу разобраться как вывести отрицательный ряд чисел Фибоначчи.