#Дано число. Проверить кратно ли оно (5 и 10) или 15, но не 30

a = int(input('Введите целое число '))

if (a%5 == 0 and a%10 == 0) and a%30!=0:
    print('число а кратно 5 и 10 но не 30')
else: print ('Число а не кратно 5 или 10 или кратно 30')
if (a%15 == 0 and a%30!=0):
    print ('Число а кратно 15 но не 30')
else: print('Число а не кратно 15 или кратно 30')