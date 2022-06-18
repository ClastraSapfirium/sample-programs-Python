# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

def Seq_Create(x, filename):
    ls = []
    for i in range(-x-1, x):
        item = i + 1
        ls.append(item)
    with open(filename,'w') as dt:
        for item in ls:
            dt.write(f'{item}\n')

def Count_Lines(filename):
    k = 0
    with open(filename, 'r') as fl:
        for ln in fl:
            k+=1
    return k

def Mltplctn(a,b, filename):
    k = 0
    s = 0
    with open(filename,'r') as dt:
        for ind, ln in enumerate(dt,1):
            if a == ind:
                k = int(ln)
            if b == ind:
                s = int(ln)
    return k*s

print('Укажите параметр N для последовательности')
a= int(input())
fn = 'E:\GeekEducation\Python\Python Tasks\Task17\File.txt'
Seq_Create(a, fn)
print(f'Получено {Count_Lines(fn)} позиций')
print('Укажите две позиции для перемножения данных из них')
x = int(input())
y = int(input())
print(f'Произведение элементов на указанных позициях равно {Mltplctn(x,y,fn)}')