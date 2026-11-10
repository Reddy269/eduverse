from accounts.interactors.core import CreateUserInteractor, IsEmailRegisteredInteractor
from accounts.interactors.ports import UserStorageInterface,PasswordHasherInterface,StorageValidationInterface
from accounts.interactors.dtos import RequestRegisterUserDTO
from accounts.interactors.exceptions import InvalidUsernameError, InvalidPasswordError, EmailAlreadyExistsError
from .password_rules import PasswordRules


# call this interactor only after knowing the fact that email is not already registered
class RegisterUserInteractor:

    def __init__(self,
                 password_hasher: PasswordHasherInterface,
                 create_user:CreateUserInteractor,
                 storage_validation:StorageValidationInterface,
                 password_rules:PasswordRules,
                 email_check:IsEmailRegisteredInteractor
                 ):
        self.password_hasher = password_hasher
        self.create_user = create_user
        self.storage_validation = storage_validation
        self.password_rules = password_rules
        self.email_check = email_check


    def register_user(self,request: RequestRegisterUserDTO):
        # email validation : this should not happen twice
        if not self.email_check(request.email, request.user_type):
            raise EmailAlreadyExistsError("email already exists")

        # username rules
        if not request.username or not request.username.split():
            raise InvalidUsernameError('username must not be empty')
        if not self.storage_validation.is_username_taken(request.username,request.user_type.value):
            raise InvalidUsernameError('username already taken')
        # password rules
        if not request.password or not request.password.strip():
            raise InvalidPasswordError('password must not be empty')

        self.password_rules(password = request.password,email = request.email)

        request.password = self.password_hasher.hash_password(request.password)

        self.create_user.create(request)



