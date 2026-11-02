from abc import ABC, abstractmethod

class ReceiveCourseContent(ABC):
    @abstractmethod
    def get_course_thumbnail(self):
        pass
    @abstractmethod
    def get_course_path_items(self):
        pass
