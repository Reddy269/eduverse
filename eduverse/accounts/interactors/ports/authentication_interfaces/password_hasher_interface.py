from abc import ABC, abstractmethod

class PasswordHasherInterface(ABC):
    @abstractmethod
    def hash_password(self, password: str) -> str:
        pass
    def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        pass
