from accounts.interactors.core import IsEmailRegisteredInteractor
from accounts.interactors.dtos import RequestRegisterUserDTO, UserType
from accounts.interactors.exceptions import EmailAlreadyExistsError

class RegisterEmailInteractor:
    def __init__(self,
                 email_check: IsEmailRegisteredInteractor,
                 ):
        self.email_check = email_check

    def __call__(self,email:str,user_type:UserType) -> bool:
        if self.email_check(email,user_type):
            raise EmailAlreadyExistsError("email already exists")

        # email authentication logic : yet to be thought of and coded


        return True