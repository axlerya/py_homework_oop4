class Teacher:
    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patrinymic = patronymic

    def __repr__(self):
        return f"Фамилия: {self.surname} Имя: {self.name} Отчество: {self.patrinymic}"
