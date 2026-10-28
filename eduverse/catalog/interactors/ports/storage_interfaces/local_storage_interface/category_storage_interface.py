from abc import ABC, abstractmethod
from dataclasses import dataclass
from catalog.interactors.dtos import RequestAssignCategoryDTO
from dtos import RequestCreateCourseDTO


class CategoryStorageInterface(ABC):
    @abstractmethod
    def is_root_parent(self,request: RequestCreateCourseDTO) -> bool:
        pass

