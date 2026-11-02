from accounts.interactors.ports import PasswordHasherInterface
from accounts.interactors.exceptions import InvalidCredentialsError

class PasswordHasher(PasswordHasherInterface):
    def hash_password(self, password: str) -> str:
        #hashing logic:

        return password

    def verify_password(self, password: str) -> bool:
        hashed_password = self.hash_password(password)
        if password != hashed_password:
            raise InvalidCredentialsError()
        return True

