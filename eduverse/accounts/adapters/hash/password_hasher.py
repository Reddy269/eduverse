from accounts.interactors.ports import PasswordHasherInterface


class PasswordHasher(PasswordHasherInterface):
    def hash_password(self, password: str) -> str:
        #hashing logic:

        return password

    def verify_password(self, password: str) -> bool:
        hashed_password = self.hash_password(password)
        if password != hashed_password:
            pass
        return True

