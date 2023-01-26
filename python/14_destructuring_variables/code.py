t = 5, 11
x, y = t

print(x, y)

student_attendance = {
  "Rolf": 96,
  "Adam": 80,
  "Anne": 100
}

for t in student_attendance.items():
  print(t)

for student, attendance in student_attendance.items():
  print(f"{student}: {attendance}")

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
for name, age, job in people:
  print(f"{name} : {age} : {job}")

head, *tail = [1, 2, 3, 4, 5]

print("Head: ", head, " Tail: ", tail)