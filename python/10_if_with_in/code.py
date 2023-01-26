# movies = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter a movie: ")

# if user_movie in movies:
#     print("I've watched it too!")
# else:
#     print("I haven't watched that yet!")

number = 7
user_input = input("Enter 'y' if you want to play: ").lower()

# if user_input == "y":
if user_input in ("y", "Y"):
    user_number = int(input("Guess a number: "))
    if user_number == number:
        print("You guessed it right")
    # elif abs(number - user_number) == 1:
    elif number - user_number in (1, -1):
        print("You were off by 1")
    else:
        print("Sorry, you guessed it wrong")