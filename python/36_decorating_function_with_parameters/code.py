import functools

user = {"username": "bob", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return "Access Denied"
    return secure_function


@make_secure
def get_admin_password():
    return "1234"


@make_secure
def get_dashboard_password():
    return "billing_password"


print(get_admin_password("billing"))
