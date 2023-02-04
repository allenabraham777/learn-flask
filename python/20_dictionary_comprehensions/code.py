users = [
  (0, "Bob", "password"),
  (1, "Rolf", "bob123"),
  (2, "Jose", "longpassword"),
  (3, "username", "1234")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if(username_input in username_mapping):
  _, username, password = username_mapping[username_input]

  if password_input == password:
    print("Your details are correct!")
  else:
    print("Your details are incorrect!")
else:
  print("Your details are incorrect!")