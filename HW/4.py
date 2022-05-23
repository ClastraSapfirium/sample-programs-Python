# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека

from random import randint

def input_dat(player_name):
    x = int(input(f"{player_name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{player_name}, введите корректное количество конфет: "))
    return x


def p_print(player_name, k, clock, value):
    print(f"Ходил {player_name}, он взял {k}, теперь у него {clock}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

clock1 = 0 
clock2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        clock1 += k
        value -= k
        flag = False
        p_print(player1, k, clock1, value)
    else:
        k = input_dat(player2)
        clock2 += k
        value -= k
        flag = True
        p_print(player2, k, clock2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")



# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход.")


def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    clock = 0
    win = False
    while not win:
        draw_board(board)
        if clock % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        clock += 1
        if clock > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if clock == 9:
            print("Ничья!")
            break
    draw_board(board)

board = list(range(1,10))
main(board)