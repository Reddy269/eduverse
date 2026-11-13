from abc import ABC, abstractmethod
from accounts.interactors.dtos import RequestRegisterUserDTO


class UserStorageInterface(ABC):
    @abstractmethod
    def create_user(self,request:RequestRegisterUserDTO):
        pass
    @abstractmethod
    def get_user_id(self,identifier:str,user_type:str,identifier_type:str)->int:
        pass

    @abstractmethod
    def register_email(self, request):
        pass

    @abstractmethod
    def delete_user(self):
        pass

    @abstractmethod
    def get_user_profile(self,user_id: str,user_type:str):
        pass

    @abstractmethod
    def get_password(self,identifier:str,usertype:str,identifier_type:str)->str:
        pass