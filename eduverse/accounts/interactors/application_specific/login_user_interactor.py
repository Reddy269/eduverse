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
        if EMAIL_PATTERN.fullmatch(request.identifier) is None:
            identifier_type = IdentifierType.EMAIL
            if not self.storage_validation.is_username_taken(request.identifier,request.usertype):
                raise IdentifierDoesNotExistError("Username does not exist")



        else:
            identifier_type = IdentifierType.USERNAME
            if not self.storage_validation.is_email_taken(request.identifier,request.usertype):
                raise IdentifierDoesNotExistError("Email does not exist")

        hashed_password = self.get_password(request.identifier, request.usertype, identifier_type)

        if hashed_password != self.password_validation.verify_password(request.password):
            return False
        return True
