# Функции: виды параметров, возвращение данных, виды аргументов.
#DRY - don`t repeat yourself
#def- defne
"""схема функции"""


# опредклкния наименования (параметры):
#     (тела фкункции)
#     возврошения данных
#
# вызов функции
# наименования(аргументы)

# def name_function(surname,name= 'user' ):
#     print(f'hello surname:{surname}  name: {name}').title
#
# name_function(name='chingyz', surname= 'aitmatov')


# name_function()
# name_function('ildar')

# name_function('jack')
# name_function('aziz')
# name_function(input('ввелите имя: '))



# def get_square(length: int, width: int)->int:
#     """Принемает ширину и длину, вощврощяет площядь."""
#
#     return length * width
#
# square_2 = get_square(5, 4)
# square_victory = get_square(250, 120)
# print(help(get_square))
# print(get_square.__doc__)

# length= 5
# width = 4
# sqare_2 = length * width
# print(sqare_2)
#
# length= 250
# width = 120
# sqare_victory = length * width
# print(sqare_victory)

# *args ** kwargs
# def plus(*args): # arguments(аргументы)
#     return sum(args)
#
# print(plus(3,2,4,56,6))
# print(plus(3,2,4,56,6,123))
#
# def menu(**kwargs):
#     return kwargs
#
# monday= menu(dring='cola', num=101)
# print(monday)
# password= input()
# print(len(password))
# def check_password(password):
#     if len(password) < 6:
#         return False
#
#     has_letter = False
#     has_digit = False
#
#     for char in password:
#         if char.isalpha():
#             has_letter = True
#         elif char.isdigit():
#             has_digit = True
#
#     return has_letter and has_digit
#
#
# user = input("Введите пароль: ")
# if check_password (user):
#     print(True)
# else:
#     print(False)
#
# def closest_number(sequence, target=0):
#
#     if not sequence:
#         print ("Переданная последовательность пуста.")
#
#     return (target),sorted(sequence, key=lambda x: abs(x - target))
#
#
#
# numbers = [1, 2, 3, 10, 6, 12]
# target = 11
# print(closest_number(numbers, target))

