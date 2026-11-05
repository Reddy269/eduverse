from abc import ABC, abstractmethod

class LessonStorageInterface(ABC):
    @abstractmethod
    def create_lesson(self,request:RequestCreateLessonDTO):
        pass
    @abstractmethod
    def delete_lesson(self,request:DeleteLessonDTO):
        pass
    @abstractmethod
    def update_lesson(self,request:UpdateLessonDTO):
        pass