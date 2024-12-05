# Списик, кортежи Инлексы и срезы Встроенные функцижи к набор элементов
# Списковые включение Lest comprehension.



# number= [1,2,3,4,0]
# print(len(number))# длина
# print(sum(number))# сумма всех обектов
# print(min(number))# минимальное число
# print(max(number))# максимальное число
# print(all(number))# проверка всего списка на > 0
# print(any(number))# проверка только одного элемента списка



# students= ['abdykalyk', 'aisuluu', 'mirbek', 'ademi']
# students2= [student.upper() for student in students if student.startswith('a')]
# print(students2, students)
# add
# from lesson3 import number
# from lesson_3 import letter

# students.append('islam')  #Добовление в конец 1 обекту
# students.insert(2,'aidar') # Добовление по индексу
# students.extend(['petr', 'iskender'])# Добовление несколько обектов
# students += ['petr', 'iskender']# Добовление несколько обектов

# edit
#students[-1], students[0] = students[0], students[-1]
#students.sort()
#students.reverse()
# students[0] = 'sardor'
# students[-2:] = ['aslan', 'timur']

# delete
# students.remove('mirbek')# удаления по обекту
# deleted= students.pop(0) #удаления по индексу
# del students[:2]#удаления...
# students.clear()# очищения

# print(students)

#Инлексы и срезы
# print(students[0])
# print(students[1])
# print(students[-1])
# срезы
# print(students[1:3])
# print(students[-2:])
# print(students[:2])
# print(students[::-1])
# print(students[::2])


# Домашнее задание
# data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
#
# # Создать два пустых списка letters и numbers
# letters = []
# numbers = []
#
# # Сортировать строки и цифры
# for item in data_tuple:
#     if isinstance(item, str):
#         letters.append(item)
#     else:
#         numbers.append(item)
#
# numbers.remove(6.13)  # Удаление элемента
# letters.append(numbers.pop(numbers.index(True)))  # Удаление и перенос True в конец списка
#
# numbers.insert(1, 2)  # Добавление числа 2 между 3 и 1
#
# # Сортировка
# numbers.sort()
# letters.reverse()
#
# # Замена первых двух букв
# letters[1] = 'G'
# letters[2] = 'e'
#
# # Возведение в квадрат
# numbers = [num ** 2 for num in numbers]
#
# # Преобразование в кортежи
# numbers = tuple(numbers)
# letters = tuple(letters)
#
# print(letters)
# print(numbers)
