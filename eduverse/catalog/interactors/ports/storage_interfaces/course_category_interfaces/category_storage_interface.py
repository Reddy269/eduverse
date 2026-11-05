from abc import ABC, abstractmethod
from typing import Optional

class CategoryStorageInterface(ABC):
    @abstractmethod
    def is_valid_category(self, category_id: int) -> bool:
        pass

    @abstractmethod
    def has_parent_category(self, category_id: int) -> bool:
        pass

    @abstractmethod
    def get_parent_id(self, category_id: int) -> Optional[int]:
        pass

    @abstractmethod
    def get_category_tree(self):
        pass

    @abstractmethod
    def assign_category_to_course(self, category_id: int, course_id: int):
        pass

    @abstractmethod
    def remove_category_from_course(self,category_id: int,course_id: int):
        pass

    @abstractmethod
    def get_categories_of_course(self,category_id: int):
        pass




