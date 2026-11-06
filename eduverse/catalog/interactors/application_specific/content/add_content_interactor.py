from catalog.interactors.exceptions import InvalidFileException

from catalog.interactors.ports.storage_interfaces import ContentStorageInterface
from catalog.interactors.dtos import RequestAddContentDTO, FileType, LessonType
import os


class AddContentInteractor(ContentStorageInterface):
    def __init__(self,
                 content_storage:ContentStorageInterface,
                 ):
        self.content_storage = content_storage

    def __call__(self, request:RequestAddContentDTO):
        #rule to check if filename is unique
        # rule to check if content is actually either mp4 or pdf
        file_extension = os.path.splitext(request.content.name)[1].lower()
        file_type = FileType[request.content_type.name]  # string -> member

        if file_extension not in file_type.value:
            raise InvalidFileException(request.content.name)

        self.content_storage.add_content(request)


'''
@dataclass
class RequestAddContentDTO:
    name: str
    content_type: str
    content: UploadedFile

    def __post_init__(self):
        try:
            self.content_type = LessonType(self.content_type)
        except ValueError:
            InvalidLessonTypeException(self.content_type)

'''

