from accounts.interactors.dtos import RequestRegisterEmailDTO
from accounts.interactors.ports import UserStorageInterface
from .exceptions import EmailAlreadyExists


class RegisterEmailInteractor:
    def __init__(self,
                 store: UserStorageInterface
                 ):
        self.store = store

    def execute(self,request:RequestRegisterEmailDTO):
        # rules to check if email already exists
        if not self.store.is_email_taken(request.email,request.UserType):
            raise EmailAlreadyExists(request.email)

        self.store.register_email(request)









