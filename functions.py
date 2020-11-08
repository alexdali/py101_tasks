"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def check_contains_even(*args):
    """
    функция принимает на вход любое
    количество чисел и сообщает, есть ли среди них чётное
    >>> check_contains_even(1,2,5)
    'Среди аргументов есть четное число'
    >>> check_contains_even(1,3,5)
    'Среди аргументов нет четных чисел'
    >>> check_contains_even(1,7,15,0)
    'Среди аргументов есть четное число'
    >>> check_contains_even(1,7,15,11)
    'Среди аргументов нет четных чисел'
    """
    # print(args)
    set_of_args = set(args)
    if any(digit % 2 == 0 for digit in set_of_args):
        print('Среди аргументов есть четное число')
    else:
      print('Среди аргументов нет четных чисел')


# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
age = 17
#sell_alcohol()
#return print("Мы не продаём алкоголь несовершеннолетним.") if age <=21 else sell_alcohol()



# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
def is_kword(str):
  """
  функция проверит, является ли строка ключевым словом в Питоне
  >>> is_kword('try')
  "Эта строка: 'try' является ключевым словом в Питоне!"
  >>> is_kword('test_string')
  "Эта строка: 'test_string' не является ключевым словом в Питоне!"
  >>> is_kword('for')
  "Эта строка: 'for' является ключевым словом в Питоне!"
  """
  import keyword
  if keyword.iskeyword(str):
      print("Эта строка: '{}' является ключевым словом в Питоне!".format(str))
  else:
    print("Эта строка: '{}' не является ключевым словом в Питоне.".format(str))


# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
def get_type(check_value):
    """
    функция возвращает тип данных на русском языке
    >>> get_type(1)
    >>> get_type('')
    >>> get_type(True)
    >>> get_type(None)
    >>> get_type([])
    >>> get_type(())
    >>> get_type({'q','e','g',})
    >>> get_type({})
    """
    if type(check_value) is int:
        print('Это число')
    elif type(check_value) is str:
        print('Это строка')
    elif type(check_value) is bool:
        print('Это булевый')
    elif check_value is None:
        print('Это None')
    elif type(check_value) is list:
        print('Это список')
    elif type(check_value) is tuple:
        print('Это кортеж')
    elif type(check_value) is set:
        print('Это множество')
    elif type(check_value) is dict:
        print('Это словарь')