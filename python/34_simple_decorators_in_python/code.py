user = {"username": "jose", "access_level": "guest"}
admin = {"username": "bob", "access_level": "admin"}


def get_admin_password():
    return "1234"


def secure_function(func):
    def make_secure():
        if user["access_level"] == "admin":
            return func()
        else:
            return "Access Denied"
    return make_secure


get_admin_password = secure_function(get_admin_password)

print(get_admin_password())

user = admin

print(get_admin_password())
