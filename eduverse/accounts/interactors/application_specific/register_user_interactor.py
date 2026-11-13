from accounts.interactors.core import CreateUserInteractor, IsEmailRegisteredInteractor
from accounts.interactors.ports import UserStorageInterface,PasswordHasherInterface,StorageValidationInterface
from accounts.interactors.dtos import RequestRegisterUserDTO , EMAIL_PATTERN
from accounts.interactors.exceptions import InvalidUsernameError, InvalidPasswordError, EmailAlreadyExistsError, InvalidEmailError
from .password_rules import PasswordRules


# call this interactor only after knowing the fact that email is not already registered
class RegisterUserInteractor:

    def __init__(self,
                 create_user:CreateUserInteractor,
                 storage_validation:StorageValidationInterface,
                 password_rules:PasswordRules,
                 email_check:IsEmailRegisteredInteractor
                 ):
        self.create_user = create_user
        self.storage_validation = storage_validation
        self.password_rules = password_rules
        self.email_check = email_check


    def register_user(self,request: RequestRegisterUserDTO):
        # checks if email is in a valid format:
        if EMAIL_PATTERN.fullmatch(request.email) is None:
            raise InvalidEmailError("invalid email ")

        #checks if email already exists
        if self.email_check(request.email, request.user_type):
            raise EmailAlreadyExistsError("email already exists")

        # username rules
            # if username field is empty
        if not request.username or not request.username.split():
            raise InvalidUsernameError('username must not be empty')
            #username should not be in the format of an email
        if EMAIL_PATTERN.fullmatch(request.username) is not None:
            raise InvalidUsernameError('username should not resemble email format')
            # if username is taken
        if self.storage_validation.is_username_taken(request.username,request.user_type.value):
            raise InvalidUsernameError('username already taken')
        # password rules
            #checks if exists
        if not request.password or not request.password.strip():
            raise InvalidPasswordError('password must not be empty')

            #checks password rules
            #1)

        self.password_rules(password = request.password,email = request.email,username=request.username)


        # hashes password and creates an entry
        self.create_user.create(request)

'''
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


'''



