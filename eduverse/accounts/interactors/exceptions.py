# accounts/exception.py
class LoginError(Exception):
    message = "Login failed"


class EmptyFieldError(Exception):
    message = "Empty field"

    def __init__(self, message):
        self.message = message


class UsernameorEmailDoesNotExistError(Exception):
    message = "Invalid username or Email"

class InvalidPasswordError(Exception):
    message = "Invalid password"


class InvalidUserTypeError(Exception):
    message = "Invalid user type"

