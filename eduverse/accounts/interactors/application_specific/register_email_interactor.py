from accounts.interactors.dtos import RequestRegisterEmailDTO
from accounts.interactors.ports import  PublishEventInerface
from accounts.interactors.ports.publish_interfaces import StudentRegistredDTO

from accounts.interactors.ports.publish_interfaces import StudentRegistredDTO
from interactors.ports import UserStorageInterface
from .exceptions import EmailAlreadyExists


class RegisterEmailInteractor:
    def __init__(self,
                 signal :PublishEventInerface,
                 store: UserStorageInterface
                 ):
        self.signal = signal
        self.store = store

    def execute(self,request:RequestRegisterEmailDTO):
        # rules to check if email already exists
        if not self.store.is_email_taken(request.email):
            raise EmailAlreadyExists(request.email)

        self.store.register_email(request.email)









