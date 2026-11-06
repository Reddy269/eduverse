from abc import ABC, abstractmethod

class ContentStorageInterface(ABC):
    @abstractmethod
    def add_content(self, request):
        pass

    @abstractmethod
    def add_content_to_lesson(self, content_id: int, lesson_id: int):
        pass

    @abstractmethod
    def remove_content_from_lesson(self, content_id: int, lesson_id: int):
        pass

    @abstractmethod
    def delete_content(self, content_id: int):
        pass

    @abstractmethod
    def is_content_in_section(self, content_id: int, section_id: int):
        pass
