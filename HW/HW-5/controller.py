from import_info import import_info
from export_info import export_info
from print_info import print_info
from find_info import search_info


def meeting():
    print("Здравствуйте!")

def input_info():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите примечание: ")
    return [last_name, first_name, phone_number, note]

def choice_desh():
    des = input("Введите разделитель: ")
    if des == "":
        des = None
    return des

def menu():
    print("Что требуется сделать сделать?\n\
    1 - импорт данных;\n\
    2 - экспорт данных;\n\
    3 - поиск контакта.")
    men = input("Введите значение: ")
    if men == '1':
        des = choice_desh()
        import_info(input_info(), des)
    elif men == '2':
        data = export_info()
        print_info(data)
    elif men =='3':
        word = input("(Следует учитывать что нумерация контактов начинается с нуля).\n\
Введите данные для поиска:")
        data = export_info()
        item = search_info(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            print("Данные отсутсвуют")
    elif men > '3':
        print("Введено неверное значение, попробуйте ещё раз.")