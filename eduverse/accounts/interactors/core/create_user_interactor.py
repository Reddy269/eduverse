from accounts.interactors.dtos import  RequestRegisterUserDTO
from accounts.interactors.ports import PasswordHasherInterface,UserStorageInterface




class CreateUserInteractor:
    def __init__(
            self,
            storage:UserStorageInterface,
            password_hasher:PasswordHasherInterface,
    ):
        self.storage = storage
        self.password_hasher = password_hasher

    def create(self, request : RequestRegisterUserDTO ):
        hashed_password= self.password_hasher.hash_password(request.password)
        request.password = hashed_password
        return self.storage.create_user(request)




