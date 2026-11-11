from accounts.interactors.dtos import RequestLoginUserDTO, EMAIL_PATTERN, IdentifierType
from accounts.interactors.ports import StorageValidationInterface , PasswordHasherInterface, UserStorageInterface
from accounts.interactors.exceptions import IdentifierDoesNotExistError
from accounts.interactors.core import GetPasswordInteractor

class LoginUserInteractor:

    def __init__(self,
                 storage_validation:StorageValidationInterface,
                 password_validation:PasswordHasherInterface,
                 get_password:GetPasswordInteractor,
                 storage: UserStorageInterface,
                 ):
        self.storage_validation = storage_validation
        self.password_validation = password_validation
        self.get_password = get_password
        self.storage = storage

    def login(self,request:RequestLoginUserDTO):
        # check if identifier is username or email then accordingly check if they exist ; then carry on:
        if EMAIL_PATTERN.fullmatch(request.identifier) is not None:
            identifier_type = IdentifierType.EMAIL
            if not self.storage_validation.is_email_taken(request.identifier,request.user_type):
                raise IdentifierDoesNotExistError("Email does not exist")



        else:
            identifier_type = IdentifierType.USERNAME
            if not self.storage_validation.is_username_taken(request.identifier,request.user_type.value):
                raise IdentifierDoesNotExistError("Userame does not exist")

        hashed_password = self.get_password(identifier = request.identifier,user_type =  request.user_type,identifier_type= identifier_type)

        if not self.password_validation.verify_password(raw_password=request.password,hashed_password = hashed_password):
            return False
        return self.storage.get_user_id(identifier=request.identifier,user_type= request.user_type.value,identifier_type=identifier_type.value)

'''
    class GetPasswordInteractor:
    def __init__(self,
                 storage: UserStorageInterface,
                 ):
        self.storage = storage

    def __call__(self, identifier:str,user_type:UserType,identifier_type:IdentifierType)->str:
            return self.storage.get_password(identifier,user_type.value,identifier_type.value)



    def verify_password(self, raw_password: str) -> bool:
        if raw_password == self.hash_password(raw_password):
            return True
        return False
'''