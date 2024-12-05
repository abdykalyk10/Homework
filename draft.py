

class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f' Имя: {self.full_name} Возрост: {self.age} Состоит в браке: {self.is_married}')

class Student(Person):
    def __init__(self, full_name, age, marks):
        super().__init__(full_name, age, is_married=False)
        self.marks = marks
    def average_mark(self):
        if self.marks:
            average = sum(self.marks.values()) / len(self.marks)
            return average
        else:
            return 0
class Teacher(Person):
    base_salary = 20000
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience
    def salary(self):
        if self.experience > 3:
            bonus_years = self.experience - 3
            bonus = self.base_salary * 0.05
            return self.base_salary + bonus
        else:
            return self.base_salary
teacher = Teacher('Никалай Васильевичь', 46, "Да", 13)
teacher.introduce_myself()
print(f'Зарплата {teacher.base_salary}')

def create_students():
    student = Student("Алег Семенов", 19, {'матем': 5, 'рус-яз.': 4, 'физ-ра': 5})
    student2 = Student("Алег Семенов", 19, {'матем': 4, 'рус-яз.': 4, 'физ-ра': 5})
    return [student, student2]

students = create_students()
for student in students:
    student.introduce_myself()
    for subject, mark in student.marks.items():
        print(f'{subject}: {mark}')
    print(f'Средняя оценка: {student.average_mark()}')
