import functools

user = {"username": "jose", "access_level": "guest"}
admin = {"username": "bob", "access_level": "admin"}


def secure_function(func):
    @functools.wraps(func)
    def make_secure():
        if user["access_level"] == "admin":
            return func()
        else:
            return "Access Denied"
    return make_secure


@secure_function
def get_admin_password():
    return "1234"


print(get_admin_password.__name__)
print(get_admin_password())

user = admin

print(get_admin_password())
