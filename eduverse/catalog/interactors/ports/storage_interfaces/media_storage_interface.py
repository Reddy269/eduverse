from abc import ABC, abstractmethod

from dtos import RequestAddContentDTO, RequestDeleteContentDTO, RequestUpdateContentDTO


class MediaStorageInterface(ABC):
    @abstractmethod
    def save(self, request:RequestAddContentDTO):
        pass
    @abstractmethod
    def delete(self, request:RequestDeleteContentDTO):
        pass


'''
    class RequestAddContentDTO:
    content_type: LessonType
    content: BinaryIO
    filename: str
'''