from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum
from accounts.interactors.exceptions import InvalidPasswordError, InvalideUserTypeError
import re
from prompt_toolkit import enums



EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class UserType(str, Enum):
    STUDENT = "student"
    INSTRUCTOR = "instructor"


@dataclass
class RegisteredUserDTO:
    name: str
    email: str
    usertype: UserType

    def __init__(self,name,email,usertype):
        self.name = name
        self.email = email
        self.usertype = usertype

    def __post_init__(self):
        self.usertype = UserType(self.usertype)


@dataclass
class RequestRegisterUserDTO:
    name: str
    email: str
    username: str
    user_type: UserType
    DOB: str
    password: str


    # checks if data is valid
    def __post_init__(self):
        try:
            self.UserType = UserType(self.UserType)
        except ValueError:
            raise InvalidUserTypeError()

        if not self.name.strip():
            raise ValueError("name cannot be empty")

        if not self.email.strip():
            raise ValueError("email cannot be empty")

        DOB_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

        if not isinstance(self.DOB, str) or not DOB_PATTERN.match(self.DOB):
            raise InvalidDOBError()

@dataclass
class RequestLoginUserDTO:
    usertype: UserType
    email_or_username: str
    password: str

    def __post_init__(self):
        if not self.email_or_username or not self.email_or_username.strip():
            raise ValueError("email or username cannot be empty")
        if not self.password:
            raise ValueError("password cannot be empty")




