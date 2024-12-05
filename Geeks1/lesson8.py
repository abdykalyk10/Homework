# Контекстный менеджер “with”, работа с файлами.
# w - write (запись, перезапись)
# a - add (дозапись )
# x - (проветка подленности названия  )
# r - ()

# file= open('file_name.txt', 'w')
# file.write('строка на кирилце!')
# file.close()

# with open('file_name.txt', 'a') as file:
#      file.write('\n третья строка')
# with open('file2.txt', 'x') as file:
#      file.write('123')
#
# with open('file2.txt', 'r') as file:
#      print(file.write('123'))

# from time import sleep
#
# with open('file_name.txt', 'r') as file:
#      for i in file.read():
#           sleep(0.1)
#           print(i, end='')
# more, less= 1, 100
# list_attems=[]
# print('Загадайте число от 1 до 100')
# print('Отвечайте ("да, больше или меньше")')
#
# while True:
#     number= (more + less) // 2
#     list_attems.append(number)
#     print(f'Программа думает, что вы загадали число: {number}')
#     user=input('да, больше или меньше ')
#
#     if user == 'да':
#         with open('results.txt', 'w') as file:
#             with open('results.txt', 'a') as file:
#                 file.write(f'Загаданное число: {number}\n')
#                 file.write(f'Количество попыток: {len(list_attems)}\n')
#                 file.write(f'Список попыток: {list_attems}\n')
#         break
#     elif user == 'больше':
#         more= number + 1
#     elif user == 'меньше':
#         less= number - 1
#     else:
#         print('Неверны ввод')
# with open('results.txt', 'r') as file:
#     print(file.read())

