import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


class Subject:
    def __init__(self, name, theory, practise, labs):
        self.theory = theory
        self.practise = practise
        self.labs = labs
        self.name = name

    def get_score(self):
        return self.theory + self.practise + self.labs

    def get_grade(self):
        grade = self.get_score() // 10 + 1 if self.get_score() % 10 != 0 else self.get_score() // 10
        if grade > 10:
            grade = 10
        if grade < 6:
            grade = 5
        return grade

    def __str__(self):
        return f"----{self.name}: {self.get_grade()}\n"


class Student:
    def __init__(self, name, surname, index):
        self.name = name
        self.surname = surname
        self.index = index
        self.subjects = []

    def __str__(self):
        return f"Student: {self.name} {self.surname}\n{self.print_subjects()}"

    def print_subjects(self):
        return ''.join([str(subj) for subj in self.subjects])

    def add_subject(self, name, theory, practise, labs):
        self.subjects.append(Subject(name, theory, practise, labs))


if __name__ == "__main__":
    students = {}
    while True:
        line = input().split(",")
        if line[0] == "end":
            break
        student = Student(line[0], line[1], line[2])
        if student.index not in students:
            students[student.index] = student
        students[student.index].add_subject(line[3], int(line[4]), int(line[5]), int(line[6]))
    for s in students.values():
        print(s)
