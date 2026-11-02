from accounts.interactors.dtos import RequestCreateUserDTO
from accounts.interactors.core import CreateUserInteractor
from accounts.interactors.ports import PublishEventInerface,UserStorageInterface
from accounts.adapters.hash.password_hasher import PasswordHasher
from accounts.interactors.application_specific.exceptions import EmailAlreadyExists, PasswordDoesNotMatch, UsernameAlreadyExists
from django.db import transaction


class RegisterUserInteractor:
    def __init__(self,
                 signal: PublishEventInerface,
                 storage_validation: UserStorageInterface,
                 password_hasher: PasswordHasher,
                 store:UserStorageInterface,
                 ):
        self.signal = signal
        self.store = store
        self.password_hasher = password_hasher
        self.storage_validation = storage_validation

    def register(self,request: RequestCreateUserDTO):
        if request.password != request.confirm_password:
            raise PasswordDoesNotMatch()
        if self.storage_validation.is_username_taken(request.username,request.usertype):
            raise UsernameAlreadyExists()
        if not self.storage_validation.is_email_taken(request.email,request.usertype):
            raise EmailAlreadyExists(request.email)
        if not self.storage_validation.is_under_registration(request.email,request.usertype):
            #regitration error ;
            self.store.delete_user()
        with transaction.atomic():
            obj = CreateUserInteractor(self.store,self.password_hasher)
            obj.create(request)
            self.signal.se





