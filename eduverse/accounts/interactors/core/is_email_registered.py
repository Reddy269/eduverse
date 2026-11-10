
from accounts.interactors.ports import StorageValidationInterface
from accounts.interactors.exceptions import InvalidEmailError
from accounts.interactors.dtos import EMAIL_PATTERN , UserType
from accounts.interactors.exceptions import InvalidUserTypeError


class IsEmailRegisteredInteractor:
    def __init__(self,
                 storage: StorageValidationInterface,
                 ):
        self.storage = storage

    def __call__(self, email:str , user_type:UserType) -> bool:
        #check if usertype is valid

        #check if email is not empty and  is of valid format before making a call to the db
        if not email or not email.strip():
            raise InvalidEmailError("Email is required")

        if EMAIL_PATTERN.fullmatch(email) is None:
            raise InvalidEmailError("Email is invalid")

        return self.storage.is_email_taken(email,usertype=user_type.value)