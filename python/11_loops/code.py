# number = 7
# user_input = input("Would you like to play? (Y/n) ").lower()

# while user_input != "n":
#     user_number = int(input("Guess a number: "))
#     if user_number == number:
#         print("You guessed it right")
#     elif abs(number - user_number) == 1:
#         print("You were off by 1")
#     else:
#         print("Sorry, you guessed it wrong")
#     user_input = input("Would you like to play again? (Y/n) ").lower()

# WHILE LOOP

number = 7

while True:
    user_input = input("Would you like to play? (Y/n) ").lower()
    if(user_input == 'n'):
        break
    user_number = int(input("Guess a number: "))
    if user_number == number:
        print("You guessed it right")
    elif abs(number - user_number) == 1:
        print("You were off by 1")
    else:
        print("Sorry, you guessed it wrong")

#FOR LOOP

friends = ["Bob", "Job", "Rob", "Aob"]

for friend in friends:
    print(f"{friend} is a friend")

for index in range(len(friends)):
    print(f"{friends[index]} is a friend")

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total = total + grade
print(total / amount)

total = sum(grades)
print(total / amount)
