#Операторы: принадлежности, назначения. Циклы.
from calendar import weekheader

# Оператор: принадлежности

# numbers= range(1,11)
# print(4 in numbers)
# print(24 in numbers)
#
# word= 'geeks'
# print('g' in word)
# print('o' in word)

# Оператор: назначения

# number= 5
# print(number)
# number += 4#9
# number /= 2 #4.5
# number **=2 #20.25
# number -= 0.25
# number %= 2
# print(number)

# Оператор: цикл

# rounds = 0
# while rounds < 100:
#     rounds += 1
#     if rounds == 50:
#         print('exit....')
#     if rounds % 2 ==0:
#         continue
#     print('Hello, world!', rounds)

# word= 'KYRGYZSTAN'
# for letter in word:
#     if letter == 'S':
#         break
#     #if letter == 'R' or letter == 'Z':
#     if letter in 'RZ':
#         continue
#     print(letter)
# Перечень дней недели
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

# Сумма всех затрат
total_expenses = 0

# Запрос суммы за каждый день
for day in days:
    amount = float(input(f"Введите сумму, потраченную в {day}: "))
    total_expenses += amount

# Подсчёт средней суммы
average_expenses = total_expenses / len(days)

print(f"Общая сумма расходов за неделю 12 + 12: {total_expenses:.1f}")
print(f"Средняя потраченная сумма за день: {average_expenses:.1f}")
