#10.	Найти рассто¤ние между двум¤ точками пространства

x1 = int(input('Введите координату Х точки 1 '))
y1 = int(input('Введите координату Y точки 1 '))
x2 = int(input('Введите координату Х точки 2 '))
y2 = int(input('Введите координату Y точки 2 '))

sqrt = round((((x2-x1)**2) + ((y2-y1)**2))**(0.5),2)

print('Расстояние между точками равно ', sqrt)