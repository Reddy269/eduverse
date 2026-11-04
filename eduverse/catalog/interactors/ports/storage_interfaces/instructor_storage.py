from abc import ABC, abstractmethod

from catalog.interactors.dtos import RequestOnboardInstructorDTO


class InstructorStorageInterface(ABC):
    @abstractmethod
    def save_profile(self,request:RequestOnboardInstructorDTO):
        pass