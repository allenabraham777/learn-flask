def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


print("Welcome to the average grade program.")

students = [
    {"name": "Bob", "grades": [78, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 92]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")
except ZeroDivisionError as e:
    print(f"ERROR: {name} has no grades!")
else:
    print(f"Average calculation successful.")
finally:
    print("End of average grade program.")
