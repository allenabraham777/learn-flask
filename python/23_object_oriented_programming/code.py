class Student:
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades

  def average(self):
    return sum(self.grades) / len(self.grades)

student = Student("Rolf", (90, 90, 92, 80, 88))
student2 = Student("Bob", (100, 95, 85, 90, 100))

print(student.average())
print(student2.average())