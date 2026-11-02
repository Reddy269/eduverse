from accounts.interactors.dtos import RequestCreateUserDTO
from accounts.interactors.core import CreateUserInteractor
from accounts.interactors.ports import PublishEventInerface,UserStorageInterface
from interactors.application_specific.exceptions import EmailAlreadyExists, PasswordDoesNotMatch, UsernameAlreadyExists
from django.db import transaction


class RegisterUserInteractor:
    def __init__(self,
                 create_user:CreateUserInteractor,
                 signal: PublishEventInerface,
                 store: UserStorageInterface
                 ):
        self.create_user = create_user
        self.signal = signal
        self.store = store

    def register(self,request: RequestCreateUserDTO):
        if request.password != request.confirm_password:
            raise PasswordDoesNotMatch()
        if self.store.is_username_taken():
            raise UsernameAlreadyExists()
        if not self.store.is_email_taken(request.email):
            raise EmailAlreadyExists(request.email)
        if not self.store.is_under_registration(request.email):
            #regitration error ;
            self.store.delete_user()
        with transaction.atomic():
            registerd_user = self.create_user.create(request)
            self.signal.send_signal(registerd_user)
            return registerd_user




