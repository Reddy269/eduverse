from abc import ABC, abstractmethod

from catalog.interactors.dtos import RequestCreateCourseDTO,RequestUpdateCourseDTO


class DraftStorageInterface(ABC):
    @abstractmethod
    def save(self,request:RequestCreateCourseDTO):
        pass

    def update(self,request:RequestUpdateCourseDTO):
        pass