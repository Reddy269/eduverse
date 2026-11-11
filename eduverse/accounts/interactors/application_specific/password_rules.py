from accounts.interactors.exceptions import InvalidPasswordError
import string

class PasswordRules:

    def __call__(self, password:str , email:str) -> bool:
        # rule 1: should not have any space in between them:
        if any(ch.isspace() for ch in password.strip()):
            raise InvalidPasswordError('password must contain only letters, numbers, dots and dashes, no whitespace')
        # rule 2: minimum 8 characters
        if len(password.strip()) < 8:
            raise InvalidPasswordError('password must contain at least 8 characters')

        # rule 3: must have atleast one uppercase , 1 number , 1 symbol
        if not  (any(char.isdigit() for char in password.strip()) and
            any(char.isupper() for char in password.strip()) and
            any(char in string.punctuation for char in password)
                ) :
            raise InvalidPasswordError('password must contain atleast one uppercase letter, number and symbol')

        # rule 4: password must not be the email itself
        if password.strip().lower() == email.strip().lower():
            raise InvalidPasswordError('password must not be the same as email')

