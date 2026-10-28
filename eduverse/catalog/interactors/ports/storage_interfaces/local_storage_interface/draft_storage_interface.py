from abc import ABC, abstractmethod

from dtos import RequestUpdateCourseDTO
from interactors.dtos import RequestCreateUserDTO


class DraftStorageInterface(ABC):
    @abstractmethod
    def save(self,request:RequestCreateUserDTO):
        pass

    def update(self,request:RequestUpdateCourseDTO):
        pass