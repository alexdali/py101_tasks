"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    pass

    passwd = input('Введите пароль: ')
    contains_digit = any(char.isdigit() for char in passwd)
    contains_alpha = any(char.isalpha() for char in passwd)
    if (len(passwd) >= 8 and contains_digit and contains_alpha):
        print('Ваш пароль сложный')
    else:
        print('Ваш пароль простой')