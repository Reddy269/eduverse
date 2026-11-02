from abc import ABC, abstractmethod

class StorageValidationInterface(ABC):
    @abstractmethod
    def is_username_taken(self, username: str, usertype: str) -> bool:
        pass

    @abstractmethod
    def is_email_taken(self, email: str, usertype: str) -> bool:
        pass

    @abstractmethod
    def is_under_registration(self, email: str, usertype: str) -> bool:
        pass