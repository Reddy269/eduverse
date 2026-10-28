from accounts.interactors.ports import PasswordHasherInterface
from accounts.interactors.exceptions import InvalidCredentialsError

class PasswordHasher(PasswordHasherInterface):
    def hash_password(self, password: str) -> str:
        #hashing logic:

        return password

    def verify_password(self, password: str, hashed_password: str) -> bool:
        if password != hashed_password:
            raise InvalidCredentialsError()

