friend_ages = {
  "Rolf": 24,
  "Adam": 30,
  "Anne": 27
}

print("Adam", friend_ages["Adam"])

friend_ages["Bob"] = 20
print("Bob", friend_ages["Bob"])

friend_ages["Anne"] = 26
print("Anne", friend_ages["Anne"])


friends = [
  {"name": "Rolf", "age": 24},
  {"name": "Adam", "age": 30},
  {"name": "Anne", "age": 27}
]

print(friends)
print(friends[1]["name"])

student_attendance = {
  "Rolf": 96,
  "Adam": 80,
  "Anne": 100
}

for student in student_attendance:
  print(f"{student}: {student_attendance[student]}")

for student, attendance in student_attendance.items():
  print(f"{student}: {attendance}")

if "Bob" in student_attendance:
  print(f"Bob: {student_attendance['Bob']}")
else:
  print("Bob is not in the class")

attendance_values = student_attendance.values()
print("Average", sum(attendance_values)/len(student_attendance))