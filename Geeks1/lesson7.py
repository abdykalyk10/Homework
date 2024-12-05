# Lambda функции. Обработка исключений.
# students_count = range(1,23)
# counter= 1
# data= {}

# while counter != len(students_count):
#     try:
#         exist = int(input(f'#{counter}'))
#     except:
#         print('не верный ввод, повторите попытку!')
#     else:
#         if exist:
#             data [input(f'enter namr #{counter}')] = counter
#             counter += 1
#         print(data)
# print(len(data), students_count)
# try:
#     print(2 * 'leo')
# except:
#     print('есть ошибка')
# else:
#     print('нет ошибки')
# finally:
#     print('Ошибка завершина')


# words= ['berlin', 'abu-dhabi', 'paris', 'rome', 'istabul', 'moscow']
#
# words_mapped= list(map(lambda word: word.upper(), words))
# print(words_mapped)
#
# words_filtered= list(filter(lambda word: "1" not in word, words))
# print(words_filtered)
#
# words_sorter = sorted(words, key= lambda word: word[-1])
# print(words_sorter)
#


# def up_first_letter(word: str) -> str:
#     """Принемет слово и возврощяет его с большой буквой"""
#     return word.title()
#
#
# def show_words(func, objects):
#     for obj in objects:
#         print(func(obj))
# show_words(lambda word: word.title(), ['kant', 'talas', 'balykchy'])# сокрощения с lambda
# show_words(len, ['tokyo', 'london', 'paris'])
# show_words(up_first_letter, ['tokmok', 'karkol', 'bishkek'])


# labda_func= lambda a, b: a+b
# print(labda_func)
# print(type(labda_func))
#
# def plus(a,b):
#     return a + b
# print(plus(2, 3))
# print(type(plus))

#№-1
# def closest_number(sequence, target=0):
#  return (target), sorted(sequence, key=lambda x: abs(x - target))
#
# numbers = [1, 2, 3, 10, 6, 12]
# target = 11
# print(closest_number(numbers, target))
#
# # №-2
# numbers = [1, 4, 7, 3, 8]
# result = filter(lambda x: x % 2==0, numbers )
# print(list(result))
#
#
# matrix = [1, 4, 7, 3]
# result = map(lambda x: x * 2 , matrix)
# print(list(result))
#
# # №-3
# def index_number(iterable=[1, 2, 3, 4, 5]):
#     print(iterable)
#
#     while True:
#         index= input('enter index')
#         try:
#             if index == 'exit':
#                 print("Операция остановлена")
#                 break
#             print(iterable[int(index)])
#         except IndexError:
#             print(f'Введите индекс от 0 до {len(iterable) - 1}')
#         except ValueError:
#             print('Ошибка введите число!')
# print(index_number([1, 2, 3, 4, 9, 45, 78, 8]))
#

