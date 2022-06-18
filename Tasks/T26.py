# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fib(n): 
    if n in [1,2]: 
        return 1 
    else: 
        return Fib(n-1) + Fib(n-2) 

def Neg_Fib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return Neg_Fib(n+2) - Neg_Fib(n+1)

a= int(input('Введите число для построения Негафибоначчи '))
m = a
ls = []
for m in range(-a, 0):
    ls.append(Neg_Fib(m))
ls.append(0)

for a in range(1, a+1):
    ls.append(Fib(a))

print(ls)