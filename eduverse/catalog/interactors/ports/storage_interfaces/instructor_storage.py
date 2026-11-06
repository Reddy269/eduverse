from abc import ABC, abstractmethod

from catalog.interactors.dtos import RequestOnboardInstructorDTO


class InstructorStorageInterface(ABC):
    @abstractmethod
    def save_profile(self,request:RequestOnboardInstructorDTO):
        pass
    @abstractmethod
    def get_profile(self,request:RequestOnboardInstructorDTO) :
        pass
    @abstractmethod
    def does_instructor_exist(self,instructor_id:int) -> bool:
        pass