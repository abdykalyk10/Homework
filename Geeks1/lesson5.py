# Словари, множества. Тест, самостаятельная работа.
# beshbrmak= {'мясо', 'тесто','лук'}
# plov= {'мясо', 'рис','морковь'}
# print(beshbrmak.intersection(plov))
# print(beshbrmak.difference(plov))
# print(beshbrmak.symmetric_difference(plov))
# print(beshbrmak.union(plov))

# student = {
#     'name': 'adilet',
#     'age': '19',
#     1: 45,
#     2: False
# }
# """delete"""
# student.pop(1)
# del student['name']

"""add"""

# student['weight']= 64.8
# student.update({'surname': 'manasov', 'country': 'KG'})
# student ["hobby"] = ['soccer', 'chess']
# student.update()

"""edit"""
# student['age']= 20
# student['name']= 'tilek'



# print(student)
# print(student['name'])
# print(student['age'])

Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
Geeks.pop('bag')
Geeks["address"]= 'Ibraimova 103'
Geeks['contacts'] = '@geeks_edu'
Geeks['conta'] = '0 123 45 67 89'
Geeks['courses'].extend([ 'Data Science', '1C', 'SMM', 'UX/UI Дизаин'])
Geeks['courses'] = set(Geeks['courses'])
Geeks['founded'] = '2018'
print("Количество курсов:", len(Geeks['courses']))
for key, value in Geeks.items():
    print(f"{key}: {value}")
