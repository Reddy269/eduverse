from accounts.interactors.dtos import RequestLoginUserDTO
from accounts.interactors.ports import StorageValidationInterface , PasswordHasherInterface




class LoginUserInteractor:

    def __init__(self,
                 storage_validation:StorageValidationInterface,
                 password_validation:PasswordHasherInterface,
                 ):
        self.storage_validation = storage_validation
        self.password_validation = password_validation

    def login(self,request:RequestLoginUserDTO):
        if not self.storage_validation.is_email_taken(request.email_or_username,request.usertype):
            pass

        if not self.password_validation.verify_password(request.password):
            pass
        return True
