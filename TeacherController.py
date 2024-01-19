from TeacherView import TeacherView


class TeacherController(TeacherView):
    def __init__(self) -> None:
        super().__init__()

    def add_teacher(self, teacher: object):
        return super().add_teacher(teacher)

    def edit_teacher(self, index: int, teacher: object):
        self.teachers[index] = teacher
