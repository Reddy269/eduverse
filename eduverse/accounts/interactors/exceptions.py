# accounts/exception.py



class InvalidInputError(Exception):
    message = "Invalid input"
    def __init__(self, message):
        self.message = message

class InvalidEmailError(InvalidInputError):
    def __init__(self, message = None):
        if message is not None:
            super().__init__(message)

class InvalidUserTypeError(InvalidInputError):
    def __init__(self, message = None):
        if message is not None:
            super().__init__(message)

class EmailAlreadyExistsError(InvalidInputError):
    def __init__(self, message = None):
        if message is not None:
            super().__init__(message)

class InvalidUsernameError(InvalidInputError):
    def __init__(self, message = None):
        if message is not None:
            super().__init__(message)


class InvalidPasswordError(InvalidInputError):
    def __init__(self, message = None):
        if message is not None:
            super().__init__(message)

class IdentifierDoesNotExistError(InvalidInputError):
    def __init__(self, message = None):
        if message is not None:
            super().__init__(message)






class LoginError(Exception):
    message = "Login failed"


class EmptyFieldError(Exception):
    message = "Empty field"

    def __init__(self, message):
        self.message = message


class UsernameorEmailDoesNotExistError(Exception):
    message = "Invalid username or Email"

