from TeacherService import Teacher
from TeacherController import TeacherController

teacher_one = Teacher("Иванов", "Иван", "Иванович")
teacher_two = Teacher("Петров", "Петр", "Петрович")
teacher_three = Teacher("Степнов", "Степан", "Степанович")
teacher_edit = Teacher("Сидоров", "Cтепан", "Игоревич")

teachers = TeacherController()
teachers.add_teacher(teacher_one)
teachers.add_teacher(teacher_two)
teachers.add_teacher(teacher_three)
print(teachers.send_on_console())
teachers.edit_teacher(2, teacher_edit)

print(teachers.send_on_console())
