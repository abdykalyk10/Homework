
vowels = 'АЕЁИОУЫЭЮЯAEIOUYaeiouyаеёиоуыэюя'
consonants = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩBCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxzбвгджзйклмнпрстфхцчшщ'

while True:
    vowels_letter = 0
    consonants_letter = 0
    word = input('Введите слово на латини или кирилли: ')
    if word == 'stop' or word == 'стоп' :
        print('Операция остановлена!')
        break
    print('Слово:', word)
    for letter in word:
        if letter in vowels:
            vowels_letter += 1
        elif letter in consonants:
            consonants_letter += 1
    total_letters = vowels_letter + consonants_letter
    print(f'Количество букв: {total_letters}\n'
          f'Гласных букв: {vowels_letter}\n'
          f'Согласных букв: {consonants_letter}')
    if total_letters > 0:
        percentage_vow = (vowels_letter / total_letters) * 100
        percentage_con = (consonants_letter / total_letters) * 100
        print(f'Гласные/Согласные: {round(percentage_vow, 2)}% / {round(percentage_con, 2)}%')
    else:
        print('Вы не ввели букву!')
