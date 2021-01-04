class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

def highest_avg(stud_lst):
    avg = {}
    for student in stud_lst:
        avg[student.name] = sum(student.grades)/len(student.grades)
    return(max(avg, key=avg.get))


