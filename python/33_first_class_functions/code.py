def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


output = calculate(20, 4, operator=divide)
print("OUTPUT: ", output)


def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    raise RuntimeError(f"Could not find an element with {expected}.")


def get_friend_name(friend):
    return friend["name"]


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]

print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Bob Smith", get_friend_name))
