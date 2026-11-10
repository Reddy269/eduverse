from accounts.interactors.ports import StorageValidationInterface


class DoesUserExistInteractor:
    def __init__(self,
                 storage: StorageValidationInterface,
                 ):
        self.storage = storage

    def __call__(self, email:str, usertype:str):
        return self.storage.is_email_taken(email,usertype)