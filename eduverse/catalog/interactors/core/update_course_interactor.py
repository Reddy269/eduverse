from catalog.interactors.dtos import RequestUpdateContentDTO, RequestAddContentDTO
from catalog.models import Course, Lesson
from catalog.interactors.ports import DraftStorageInterface,MediaStorageInterface
from catalog.interactors.content import AddContentInteractor
from dtos import RequestUpdateCourseDTO


class UpdateCourseInteractor:
    def __init__(self,
                 draft_storage: DraftStorageInterface,
                 media_storage: MediaStorageInterface,
                 add_content_interactor: AddContentInteractor,
                 ):
        self.draft_storage = draft_storage
        self.media_storage = media_storage
        self.add_content_interactor = add_content_interactor

    def update(self, request:RequestUpdateCourseDTO,course_id):
        course = Course.objects.get(id=course_id)
        if request.name is not None:
            course.title = request.name
        if request.prerequisites is not None:
            course.prerequisites = request.prerequisites
        if request.listing_image_filename is not None:
            course.listing_image_metadata = request.listing_image_filename
        if request.preview_content_filename is not None:
            course.preview_content_metadata = request.preview_content_filename















''''class Course(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=3, choices=course_status, default="DRA")
    prerequisites = models.TextField(null=True,blank=True)
    overview = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField(null=True,blank=True)
    about_instructor = models.TextField(null=True,blank=True)
    listing_image_metadata = models.TextField(null=True,blank=True)
    preview_content_metadata = models.TextField(null=True,blank=True)

    class RequestUpdateCourseDTO:
    name: Optional[str]
    categories: Optional[List[str]]
    prerequisites: Optional[str]
    about: Optional[str]
    lessons: Optional[List[LessonDTO]]
    listing_image_filename: Optional[str]
    preview_content_filename: Optional[str]

    class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    reference_order = models.IntegerField()
    reference_module = models.CharField(max_length=100)
    lesson_type = models.CharField(max_length=100)
    content_metadata = models.TextField()

    class LessonDTO:
    name: str
    description: str
    LessonType: LessonType
    filename: str
    
    class RequestAddContentDTO:
    content_type: LessonType
    content: BinaryIO
    filename: str


'''