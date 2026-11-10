from abc import ABC, abstractmethod
from accounts.interactors.dtos import RequestRegisterUserDTO


class UserStorageInterface(ABC):
    @abstractmethod
    def create_user(self,request:RequestRegisterUserDTO):
        pass
    @abstractmethod
    def get_user_id(self,username_or_email:str,usertype:str):
        pass

    @abstractmethod
    def register_email(self, request):
        pass
    @abstractmethod
    def delete_user(self):
        pass

    @abstractmethod
    def get_user_profile(self,username:str,usertype:str):
        pass
