import os
import django
from accounts.interactors.exceptions import InvalidEmailError
from accounts.interactors.exceptions import InvalidInputError


try:
    print('before catching')
    raise InvalidEmailError
    print('after catching')
except InvalidInputError as e:
    print('exception part:')
    print(e.message)