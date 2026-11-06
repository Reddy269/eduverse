from catalog.interactors.ports.storage_interfaces import ContentStorageInterface
from catalog.models import Content
from catalog.interactors.dtos import RequestAddContentDTO


class ContentStorage(ContentStorageInterface):

    def add_content(self, request:RequestAddContentDTO):
        content = Content.objects.create(name = request.name, content_type = request.content_type, content = request.content)



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
            
class Content(models.Model):
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.PROTECT, null=True,blank=True)
    name = models.CharField(max_length = 20)
    content_type = models.CharField(max_length = 20,choices = [(t.value,t.name) for t in LessonType])
    file = models.FileField(upload_to=file_path)


'''
