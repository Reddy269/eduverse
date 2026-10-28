from abc import ABC, abstractmethod

class CourseStorageInterface(ABC):
    @abstractmethod
    def save(self):
        pass