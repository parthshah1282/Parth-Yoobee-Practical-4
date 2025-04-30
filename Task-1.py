class student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    def add_grades(self, grade):
        self.grades.append(grade)
    def get_avg(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    def get_letter_grade(self):
        avg = self.get_avg()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    def show_report(self):
        print(f"report for {self.name}:")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.get_avg():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        print()        
student1 = student("Jay")
student2 = student("Ravi")
student1.add_grades(85)
student1.add_grades(75)
student1.add_grades(65)
student2.add_grades(95)
student2.add_grades(85)
student2.add_grades(75)
student1.show_report()
student2.show_report()