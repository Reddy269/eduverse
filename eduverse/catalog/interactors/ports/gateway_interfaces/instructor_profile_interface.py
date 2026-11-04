from abc import ABC, abstractmethod

from catalog.interactors.dtos import RequestInstructorProfileDTO


class InstructorProfileInterface(ABC):
    @abstractmethod
    def get_profile(self,request:RequestInstructorProfileDTO):
        pass
    @abstractmethod
    def update_profile(self,request):
        pass