from abc import ABC, abstractmethod

class CourseCategoryStorageInterface(ABC):
    @abstractmethod
    def is_valid_category(self, category: str) -> bool:
        pass

