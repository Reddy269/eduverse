from abc import ABC, abstractmethod
from accounts.interactors.dtos import RequestCreateUserDTO, RequestRegisterEmailDTO


class UserStorageInterface(ABC):
    @abstractmethod
    def create_user(self,request:RequestCreateUserDTO):
        pass
    @abstractmethod
    def get_user(self):
        pass
    @abstractmethod
    def is_admin(self):
        pass
    @abstractmethod
    def is_email_taken(self,email:str,usertype:str) -> bool:
        pass
    @abstractmethod
    def is_username_taken(self,username:str,usertype:str) -> bool:
        pass
    @abstractmethod
    def register_email(self,request:RequestRegisterEmailDTO):
        pass
    @abstractmethod
    def is_under_registration(self,email:str,usertype:str) -> bool:
        pass
    @abstractmethod
    def delete_user(self):
        pass