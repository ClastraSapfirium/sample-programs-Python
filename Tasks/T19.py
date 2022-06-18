# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

import time
def rand_val(x,y):
   sub=y-x
   rnd=int(time.time())
   rnd %= sub
   rnd+=x
   return rnd
x=int(input('Задайте начальное значение '))
y=int(input('Задайте конечное значение '))
print(rand_val(x,y))