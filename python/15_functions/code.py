def hello():
  print("Hello!")

def user_age_in_sec():
  user_age = int(input("Enter your age: "))
  age_seconds = user_age * 365 * 24 * 60 * 60
  print(f"Age in seconds: {age_seconds}")

hello();
user_age_in_sec();