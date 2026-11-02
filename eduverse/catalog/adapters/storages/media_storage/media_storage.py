from catalog.interactors.ports.storage_interfaces.media_storage_interface import MediaStorageInterface
from dtos import RequestAddContentDTO, RequestDeleteContentDTO
from catalog.models import Content


class MediaStorage(MediaStorageInterface):
    def save(self, request:RequestAddContentDTO):
        pass

    def delete(self, request:RequestDeleteContentDTO):
        pass




'''
@dataclass
class RequestAddContentDTO:
    content_type: LessonType
    content: BinaryIO
    filename: str

@dataclass
class RequestDeleteContentDTO:
    content_type: LessonType
    filename: str
    
FILE_TYPES = {".mp4":"videos",".pdf":"srticles"}

def file_path(instance, filename):
    ext = filename.split('.')[-1]
    path = FILE_TYPES.get(ext)
    return f"{path}/{filename}"

class Content(models.Model):
    name = models.CharField(max_length = 20)
    file = models.FileField(upload_to=file_path)
'''
