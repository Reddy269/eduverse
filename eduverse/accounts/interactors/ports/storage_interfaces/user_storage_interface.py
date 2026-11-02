from abc import ABC, abstractmethod
from accounts.interactors.dtos import RequestCreateUserDTO, RequestRegisterEmailDTO


class UserStorageInterface(ABC):
    @abstractmethod
    def create_user(self,request:RequestCreateUserDTO):
        pass
    @abstractmethod
    def get_user_id(self,username_or_email:str,usertype:str):
        pass

    @abstractmethod
    def register_email(self, request: RequestRegisterEmailDTO):
        pass
    @abstractmethod
    def delete_user(self):
        pass
