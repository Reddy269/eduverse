from abc import ABC, abstractmethod

from dtos import RequestAddContentDTO, RequestDeleteContentDTO, RequestUpdateContentDTO


class MediaStorageInterface(ABC):
    @abstractmethod
    def save(self, request:RequestAddContentDTO):
        type = request.content_type
        if type == "Video":

    @abstractmethod
    def delete(self, request:RequestDeleteContentDTO):
        pass
    @abstractmethod
    def update(self, request:RequestUpdateContentDTO):
        pass


'''
    class RequestAddContentDTO:
    content_type: LessonType
    content: BinaryIO
    filename: str
'''