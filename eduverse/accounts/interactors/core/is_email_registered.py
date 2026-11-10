
from accounts.interactors.ports import StorageValidationInterface


class IsEmailRegisteredInteractor:
    def __init__(self,
                 storage: StorageValidationInterface,
                 ):
        self.storage = storage

    def __call__(self, email:str) -> bool:
        #check if email is not empty and  is of valid format before making a call to the db
        return self.storage.is_email_taken(email)