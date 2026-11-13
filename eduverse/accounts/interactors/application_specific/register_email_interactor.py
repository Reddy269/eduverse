from accounts.interactors.core import IsEmailRegisteredInteractor
from accounts.interactors.dtos import RequestRegisterUserDTO, UserType , EMAIL_PATTERN
from accounts.interactors.exceptions import EmailAlreadyExistsError
from accounts.interactors.exceptions import InvalidEmailError


class RegisterEmailInteractor:
    def __init__(self,
                 email_check: IsEmailRegisteredInteractor,
                 ):
        self.email_check = email_check

    def __call__(self,email:str,user_type:UserType) -> bool:
        # check if email has a valid format
        if EMAIL_PATTERN.fullmatch(email) is None:
            raise InvalidEmailError("invalid email ")

        # checks if email already exists
        if self.email_check(email,user_type):
            raise EmailAlreadyExistsError("email already exists")




        return True