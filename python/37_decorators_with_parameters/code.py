import functools

user = {"username": "bob", "access_level": "admin"}
admin = {"username": "rolf", "access_level": "user"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function():
            if user["access_level"] == access_level:
                return func()
            else:
                return f"Access Denied for {user['username']}"
        return secure_function
    return decorator


@make_secure("admin")
def get_admin_password():
    return "1234"


@make_secure("user")
def get_dashboard_password():
    return "billing_password"


print(get_admin_password())
print(get_dashboard_password())


user = admin
print(get_admin_password())
print(get_dashboard_password())
