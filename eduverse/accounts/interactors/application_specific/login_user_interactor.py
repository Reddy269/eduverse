from accounts.interactors.dtos import RequestLoginUserDTO, EMAIL_PATTERN, IdentifierType
from accounts.interactors.ports import StorageValidationInterface , PasswordHasherInterface
from accounts.interactors.exceptions import IdentifierDoesNotExistError
from accounts.interactors.core import GetPasswordInteractor

class LoginUserInteractor:

    def __init__(self,
                 storage_validation:StorageValidationInterface,
                 password_validation:PasswordHasherInterface,
                 get_password:GetPasswordInteractor,
                 ):
        self.storage_validation = storage_validation
        self.password_validation = password_validation
        self.get_password = get_password

    def login(self,request:RequestLoginUserDTO):
        # check if identifier is username or email then accordingly check if they exist ; then carry on:
        if EMAIL_PATTERN.fullmatch(request.identifier) is not None:
            identifier_type = IdentifierType.EMAIL
            if not self.storage_validation.is_email_taken(request.identifier,request.user_type):
                raise IdentifierDoesNotExistError("Email does not exist")



        else:
            identifier_type = IdentifierType.USERNAME
            if not self.storage_validation.is_username_taken(request.identifier,request.user_type):
                raise IdentifierDoesNotExistError("Userame does not exist")

        hashed_password = self.get_password(identifier = request.identifier,user_type =  request.user_type,identifier_type= identifier_type)

        if not self.password_validation.verify_password(raw_password=request.password,hashed_password = hashed_password):
            return False
        return hashed_password

'''
    def verify_password(self, raw_password: str) -> bool:
        if raw_password == self.hash_password(raw_password):
            return True
        return False
'''