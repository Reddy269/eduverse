from accounts.interactors.core import CreateUserInteractor
from accounts.interactors.ports import UserStorageInterface,PasswordHasherInterface
from interactors.dtos import RequestRegisterUserDTO

# call this interactor only after knowing the fact that email is not already registered
class RegisterUserInteractor:

    def __init__(self,
                 storage: UserStorageInterface,
                 password_hasher: PasswordHasherInterface,
                 create_user:CreateUserInteractor,
                 ):
        self.storage = storage
        self.password_hasher = password_hasher
        self.create_user = create_user


    def register_user(self,request: RequestRegisterUserDTO):
        # check if username is not taken
        # check if password obeys rules
        self.create_user.create(request)



