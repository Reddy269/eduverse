from abc import ABC, abstractmethod
from accounts.interactors.dtos import RequestCreateUserDTO


class UserStorageInterface(ABC):
    @abstractmethod
    def create_user(self,request:RequestCreateUserDTO):
        pass
    def get_user(self):
        pass
    def is_admin(self):
        pass
    def is_email_taken(self):
        pass
    def is_user_registered(self):
        pass