from abc import ABC, abstractmethod

from catalog.interactors.dtos import RequestAddSectionDTO


class SectionStorageInterface(ABC):
    @abstractmethod
    def add_section(self, request:RequestAddSectionDTO):
        pass

    @abstractmethod
    def assign_section_to_course(self, section_id:int,course_section_id:int):
        pass

    @abstractmethod
    def remove_section_from_course(self, section_id:int,course_section_id:int):
        pass

    @abstractmethod
    def delete_section(self,section_id:int):
        pass

    @abstractmethod
    def is_section_in_course(self,section_id:int,course_id:int):
        pass