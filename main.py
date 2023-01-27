import random
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = 0
names = []
cross = 'X'
zero = 'O'
win_check = False

def draw_field(field):
    print("-------------")
    for i in range(3):
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-------------")






print('Приветствуем вас в игре крестики-нолики.')
print('Надеюсь, что вы знаете правила.')
print('Давайте теперь распределимся, кто будет ходить первым. Первым знаком всегда ставят крестик.')
draw_field(field)
print('Напишите свои имена:')
player1 = input().strip()
names.append(player1)
player2 = input().strip()
names.append(player2)
player1 = random.choice(names)
for c in names:
    if c == player1:
        names.remove(c)
player2 = names[0]
print('Хорошо')
print('Первым ходит ', player1, '. Все было сделано рандомно.', sep='')








def player1_turn(cross, player1):
    flag = False
    print(f'Ваш ход, {player1}. Введите число клетки, куда вы хотите поставить крестик:')
    while flag == False:
        answer = int(input())
        if 1 <= answer <= 9 and (field[answer - 1] != 'X' and field[answer - 1] != 'O'):
            field[answer - 1] = cross
            flag = True
        else:
            if answer < 1 or answer > 9:
                print('Введите число ОТ 1 ДО 9!!!')
                continue
            else:
                print('Это место уже занято. Попробуйте еще раз.')
                continue


def player2_turn(zero, player2):
    flag = False
    print(f'Ваш ход, {player2}. Введите число клетки, куда вы хотите поставить нолик:')
    while flag == False:
        answer = int(input())
        if 1 <= answer <= 9 and (field[answer - 1] != 'X' and field[answer - 1] != 'O'):
            field[answer - 1] = zero
            flag = True
        else:
            if answer < 1 or answer > 9:
                print('Введите число ОТ 1 ДО 9!!!')
                continue
            else:
                print('Это место уже занято. Попробуйте еще раз.')
                continue



while win_check == False:
    player1_turn(cross, player1)
    draw_field(field)
    if field[1 - 1] == cross and field[2 - 1] == cross and field[3 - 1] == cross:
        print(f'{player1} выиграл(-а)')
        win_check = True
    elif field[4 - 1] == cross and field[5 - 1] == cross and field[6 - 1] == cross:
        print(f'{player1} выиграл(-а)')
        win_check = True
    elif field[7 - 1] == cross and field[8 - 1] == cross and field[9 - 1] == cross:
        print(f'{player1} выиграл(-а)')
        win_check = True
    elif field[1 - 1] == cross and field[4 - 1] == cross and field[7 - 1] == cross:
        print(f'{player1} выиграл(-а)')
        win_check = True
    elif field[2 - 1] == cross and field[5 - 1] == cross and field[8 - 1] == cross:
        print(f'{player1} выиграл(-а)')
        win_check = True
    elif field[3 - 1] == cross and field[6 - 1] == cross and field[9 - 1] == cross:
        print(f'{player1} выиграл(-а)')
        win_check = True
    elif field[1 - 1] == cross and field[5 - 1] == cross and field[9 - 1] == cross:
        print(f'{player1} выиграл(-а)')
        win_check = True
    elif field[3 - 1] == cross and field[5 - 1] == cross and field[7 - 1] == cross:
        print(f'{player1} выиграл(-а)')
        win_check = True
    if field[1 - 1] != 0 and field[2 - 1] != 2 and field[3 - 1] != 3 and field[4 - 1] != 4 and field[5 - 1] != 5 and \
            field[6 - 1] != 6 and field[7 - 1] != 7 and field[8 - 1] != 8 and field[9 - 1] != 9:
        print('Ничья')
        win_check = True
    if win_check == False:
        player2_turn(zero, player2)
        draw_field(field)
        if field[1 - 1] == zero and field[2 - 1] == zero and field[3 - 1] == zero:
            print(f'{player2} выиграл(-а)')
            win_check = True
        elif field[4 - 1] == zero and field[5 - 1] == zero and field[6 - 1] == zero:
            print(f'{player2} выиграл(-а)')
            win_check = True
        elif field[7 - 1] == zero and field[8 - 1] == zero and field[9 - 1] == zero:
            print(f'{player2} выиграл(-а)')
            win_check = True
        elif field[1 - 1] == zero and field[4 - 1] == zero and field[7 - 1] == zero:
            print(f'{player2} выиграл(-а)')
            win_check = True
        elif field[2 - 1] == zero and field[5 - 1] == zero and field[8 - 1] == zero:
            print(f'{player2} выиграл(-а)')
            win_check = True
        elif field[3 - 1] == zero and field[6 - 1] == zero and field[9 - 1] == zero:
            print(f'{player2} выиграл(-а)')
            win_check = True
        elif field[1 - 1] == zero and field[5 - 1] == zero and field[9 - 1] == zero:
            print(f'{player2} выиграл(-а)')
            win_check = True
        elif field[3 - 1] == zero and field[5 - 1] == zero and field[7 - 1] == zero:
            print(f'{player2} выиграл(-а)')
            win_check = True





