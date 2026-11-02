from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum
from accounts.interactors.exceptions import InvalidPasswordError, InvalidUserTypeError
import re
from prompt_toolkit import enums
from .exceptions import InvalidUserTypeError


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class UserType(str, Enum):
    STUDENT = "student"
    INSTRUCTOR = "instructor"
    ADMIN = "admin"


@dataclass
class UserDTO:
    id : int
    name: str
    email: str
    usertype: UserType

    def __init__(self,id,name,email,usertype):
        self.id = id
        self.name = name
        self.email = email
        self.usertype = usertype

    def __post_init__(self):
        self.usertype = UserType(self.usertype)

@dataclass
class RequestCreateUserDTO:
    email: str
    username: str
    password: str
    confirm_password: str


@dataclass
class RequestRegisterEmailDTO:
    name: str
    email: str
    UserType: UserType
    DOB: str


    # checks if data is valid
    def __init__(self,username,email,password,UserType,DOB,name):
        self.name = name
        self.email = email
        self.UserType = UserType
        self.DOB = DOB
    def __post_init__(self):
        try:
            self.UserType = UserType(self.UserType)
        except ValueError:
            raise InvalidUserTypeError()

        if not self.name.strip():
            raise ValueError("name cannot be empty")

        if not self.email.strip():
            raise ValueError("email cannot be empty")

