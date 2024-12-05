class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Имя: {self.full_name}, Возраст: {self.age}, Состоит в браке: {'Да' if self.is_married else 'Нет'}")

class Student(Person):
    def __init__(self, full_name, age, marks):
        super().__init__(full_name, age, is_married=False)
        self.marks = marks

    def average_mark(self):
        if self.marks:
            average = sum(self.marks.values()) / len(self.marks)
            return round(average, 2)
        return 0

class Teacher(Person):
    base_salary = 20000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def salary(self):
        if self.experience > 3:
                bonus = (self.experience - 3) * (self.base_salary * 0.05)
                return self.base_salary + bonus
        else:
            return self.base_salary

eacher = Teacher('Надежда Ивановна', 45, True, 14)
eacher.introduce_myself()
print(f'Зарплата: {eacher.salary()} сом.')


def create_students():
    student_1 = Student('Антон Павлович', 18, {'Математика': 5, 'Литература': 4, 'Физика': 4})
    student_2 = Student('Иван Стрельцов', 19, {'Математика': 4, 'Литература': 5, 'Физика': 5})
    student_3 = Student('Сергей Семенов', 17, {'Математика': 5, 'Литература': 3, 'Физика': 4})
    return [student_1, student_2, student_3]

students = create_students()
for student in students:
    student.introduce_myself()
    for subject, mark in student.marks.items():
        print(f'{subject}: {mark}')
    print(f'Средняя оценка: {student.average_mark()}\n')
