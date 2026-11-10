from accounts.interactors.core import IsEmailRegisteredInteractor
from accounts.interactors.dtos import RequestRegisterUserDTO
from accounts.interactors.exceptions import EmailAlreadyExistsError

class RegisterEmailInteractor:
    def __init__(self,
                 email_check: IsEmailRegisteredInteractor,
                 ):
        self.email_check = email_check

    def __call__(self,request:RequestRegisterUserDTO):
        if not self.email_check(request.email,request.user_type):
            raise EmailAlreadyExistsError("email already exists")

        # email authentication logic : yet to be thought of and coded


        return True