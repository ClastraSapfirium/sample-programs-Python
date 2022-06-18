#7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not(x or y or z) == (not x and not y and not z)):
                print(f'При x = {x}, y = {y}, z = {z} утверждение истинно')
            else: print(f'При x = {x}, y = {y}, z = {z} утверждение ложно') 