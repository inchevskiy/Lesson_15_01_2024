class TooManyStudents(Exception):
    def __init__(self, message="Group is full! Maximum is 10 students!"):
        super().__init__(message)


class Group:
    MAX_STUDENTS = 10

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= self.MAX_STUDENTS:
            raise TooManyStudents("Group is full! Maximum is 10 students!")
        self.students.append(student)


group = Group()
try:
    for i in range(11):
        group.add_student(f"Student {i+1}")
except TooManyStudents as e:
    print(f"Error: {e}")
