#9.	Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

a = int(input('Введите номер координатной четверти '))

if a == 1: print(f'Допустимые значения координат для {a} четверти: Х от 0 до бесконечности, Y от 0 до бесконечности')
elif a == 2: print(f'Допустимые значения координат для {a} четверти: Х от - бесконечности до 0, Y от 0 до бесконечности')
elif a == 3: print(f'Допустимые значения координат для {a} четверти: Х от - бесконечности до 0, Y от - бесконечности до 0')
elif a == 4: print(f'Допустимые значения координат для {a} четверти: Х от 0 до бесконечности, Y от - бесконечности до 0')
else: print('Введите корректный номер координатной плоскости')