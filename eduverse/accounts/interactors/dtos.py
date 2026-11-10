from dataclasses import dataclass
from datetime import datetime , date
from typing import List, Optional
from enum import Enum
from accounts.interactors.exceptions import InvalidUserTypeError, InvalidInputError
import re
from prompt_toolkit import enums

EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")

DOB_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

'''
    "a@b.com": True,
    "first.last+tag@mail.example.co.in": True,
    "a@b": False,              # no domain extension
    "a@@b.com": False,         # double @
    "a b@c.com": False,        # space
    "@b.com": False,           # empty local part
    "a@b.c": False,            # extension too short
    "a..b@c.com": True,        # known weakness, see below

'''


class UserType(str, Enum):
    STUDENT = "student"
    INSTRUCTOR = "instructor"

class IdentifierType(str, Enum):
    USERNAME = 'username'
    EMAIL = 'email'






@dataclass
class RequestRegisterUserDTO:
    user_type: UserType

    email: str
    name: str
    dob: date

    username: Optional[str] = None
    password: Optional[str] = None

    # checks if data is valid
    def __post_init__(self):
        try:
            self.user_type = UserType(self.user_type.strip().lower())
        except (ValueError, AttributeError):
            raise InvalidUserTypeError("invalid user type")

        if not self.name.strip():
            raise InvalidInputError("name cannot be empty")

        if not self.email.strip():
            raise InvalidInputError("email cannot be empty")

        # datetime is a subclass of date, so reject it explicitly
        if not isinstance(self.dob, date) or isinstance(self.dob, datetime):
            raise InvalidInputError("invalid date format")

        if self.dob > date.today():
            raise InvalidInputError("date of birth cannot be in the future")

@dataclass
class RequestLoginUserDTO:
    user_type: UserType
    identifier: str
    password: str

    def __post_init__(self):
        try:
            self.user_type = UserType(self.user_type.strip().lower())
        except (ValueError, AttributeError):
            raise InvalidUserTypeError("invalid user type")

        if not self.identifier :
            raise ValueError("email or username cannot be empty")
        if not self.password:
            raise ValueError("password cannot be empty")




