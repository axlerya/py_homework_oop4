class TeacherView():
    teachers = []

    def add_teacher(self, teacher: object):
        self.teachers.append(teacher)

    def send_on_console(self):
        return self.teachers
