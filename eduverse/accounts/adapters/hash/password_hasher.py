from accounts.interactors.ports import PasswordHasherInterface


class PasswordHasher(PasswordHasherInterface):
    def hash_password(self, password: str) -> str:
        #hashing logic:

        return password

