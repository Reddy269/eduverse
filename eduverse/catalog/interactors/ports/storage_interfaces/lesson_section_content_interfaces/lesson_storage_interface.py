from abc import ABC, abstractmethod
from catalog.interactors.dtos import RequestCreateLessonDTO


class LessonStorageInterface(ABC):
    @abstractmethod
    def create_lesson(self,request:RequestCreateLessonDTO):
        pass

    @abstractmethod
    def add_lesson_to_section(self,lesson_id:int,section_course_id:int):
        pass

    @abstractmethod
    def remove_lesson_from_section(self,lesson_id:int,section_course_id:int):
        pass

    @abstractmethod
    def delete_lesson(self,lesson_id:int):
        pass

    @abstractmethod
    def update_lesson(self,lesson_id:int):
        pass

    @abstractmethod
    def is_lesson_in_section(self,lesson_id:int,section_course_id:int):
        pass
