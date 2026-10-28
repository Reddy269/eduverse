from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum
from accounts.interactors.exceptions import InvalidPasswordError
import re
from prompt_toolkit import enums


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
    name: str
    email: str
    password: str
    usertype: UserType


@dataclass
class RequestRegisterUserDTO:
    name: str
    email: str
    password: str
    UserType: UserType

    # checks if data is valid
    def __init__(self,name,email,password,UserType):
        self.name = name
        self.email = email
        self.password = password
        self.UserType = UserType
    def __post_init__(self):
        self.UserType = UserType(self.UserType)
        self.email = self.email.strip().lower()

        if not self.name.strip():
            raise ValueError("name cannot be empty")
        if not EMAIL_PATTERN.match(self.email):
            raise ValueError("email is not valid")
        if len(self.password) < 8:
            raise InvalidPasswordError(
                f"Password must be at least {8} characters long"
            )
        if not any(char.isupper() for char in self.password):
            raise InvalidPasswordError("Password must contain at least one capital letter")
        if not any(char.isdigit() for char in self.password):
            raise InvalidPasswordError("Password must contain at least one number")