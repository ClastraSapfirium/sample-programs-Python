# # Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


def String_Min_and_Max(str):
    list1 = str.split(' ')
    #print(list1)
    min = int(list1[0])
    max = int(list1[0])
    for i in range(len(list1)):
        list1[i] = int(list1[i])
        if list1[i]<min:
            min = list1[i]
        if list1[i]>max:
            max = list1[i]
    return min, max
    #print(f'Минимум равен {min}, максимум равен {max}')
  

a = input('Введите строку, состоящую из наборов чисел. В качестве символа-разделителя используйте пробел ')
print(String_Min_and_Max(a))