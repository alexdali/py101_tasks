"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

if __name__ == '__main__':
    pass
    import random
    random_number = random.randint(0, 1_000_000)
    print('''Привет! Давай поиграем в игру.
        Угадай число между 0 и 1 000 000!
    ''')

    while True:
        try:
            input_of_user = input('Введи число между 0 и 1 000 000: ')
            if (input_of_user == 'exit' or len(input_of_user) == 0):
                print('До новых встреч!')
                break
            input_to_int = int(input_of_user)
        except ValueError:
            print('Вводить можно только числа! Попробуй еще раз.')
            continue
        else:
            if (input_to_int < 0 or input_to_int > 1_000_000):
                print('Вводить можно только числа между 0 и 1 000 000!\nПопробуй еще раз.')
                continue
            elif input_to_int > random_number:
                print('Меньше')
                continue
            elif input_to_int < random_number:
                print('Больше')
                continue
            elif input_to_int == random_number:
                print('BINGO!!!')
                break

