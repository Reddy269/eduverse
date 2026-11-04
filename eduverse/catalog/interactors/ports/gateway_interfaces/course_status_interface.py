from abc import ABC, abstractmethod

from catalog.interactors.dtos import CourseDTO


class CourseStatusInterface(ABC):
    @abstractmethod
    def send_request_for_approval(self,request: CourseDTO) -> bool :
        pass
    @abstractmethod
    def revert_request_for_approval(self,request: CourseDTO) -> bool :
        pass
