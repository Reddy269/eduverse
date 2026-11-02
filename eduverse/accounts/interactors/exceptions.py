# accounts/exception.py
class AccountError(Exception):
    """Base class for errors raised by account use cases."""


class InvalidInputError(AccountError):
    """The request data failed validation."""


class EmailAlreadyExistsError(AccountError):
    """An account with this email already exists."""


class InvalidCredentialsError(AccountError):
    """The email or password is wrong."""

class InvalidPasswordError(AccountError):
    """The password is wrong."""

class InvalidUserTypeError(AccountError):
    """The user type is invalid."""

class InvalidDOBError(AccountError):
    """The DOB is invalid."""

class UsernameDoesNotExistError(AccountError):
    """The username does not exist."""

class PasswordDoesNotMatchUsernameError(AccountError):
    """The password does not match with the username."""
