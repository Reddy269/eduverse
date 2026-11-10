from accounts.interactors.ports import UserStorageInterface
from accounts.interactors.dtos import UserType , IdentifierType


class GetPasswordInteractor:
    def __init__(self,
                 storage: UserStorageInterface,
                 ):
        self.storage = storage

    def __call__(self, identifier:str,user_type:UserType,identifier_type:IdentifierType)->str:
            return self.storage.get_password(identifier,user_type.value,identifier_type.value)





