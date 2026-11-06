from catalog.interactors.ports.storage_interfaces import CourseStorageInterface
from catalog.interactors.dtos import RequestDraftCourseDTO,RequestUpdateDraftDTO,RequestGetCourseDTO,CourseDTO
from catalog.models import Course


class CourseStorage(CourseStorageInterface):


    def create_draft(self, request: RequestDraftCourseDTO) -> int:
        course_data = {"title": request.title}

        optional_fields = {
            "overview": request.overview,
            "thumbnail_file": request.thumbnail_file,
        }
        course_data.update(
            {name: value for name, value in optional_fields.items() if value is not None}
        )

        course = Course.objects.create(**course_data)
        return course.id

    def update_draft(self, request: RequestUpdateDraftDTO) -> bool:
        fields_to_update =  (
            "title", "overview", "prerequisites", "outcomes","overview",
            "duration", "about_instructor", "thumbnail_image", "preview_content_file",
        )

        course = Course.objects.get(id=request.id)

        changed = []
        for field in fields_to_update:
            value = getattr(request, field)
            if value is not None:
                setattr(course, field, value)
                changed.append(field)

        if changed:
            course.save(update_fields=changed)

        return True


    '''
@dataclass
class RequestUpdateDraftDTO:
    id: int
    title: Optional[str]
    overview: Optional[str]
    prerquisites: Optional[str]
    outcomes: Optional[str]
    overview : Optional[str]
    duration: Optional[str]
    about_instructor: Optional[str]
    thumbnail_image: Optional[UploadedFile]
    preview_content_file: Optional[UploadedFile]
    category: Optional[List[int]]

    def _post_init__(self):
        if self.id is None:
            raise InvalidUpdateRequestException
    '''



    def change_status(self, request) -> bool:
        pass

    def delete_draft(self, request) -> bool:
        pass

    def get_course(self, request:int|str) -> CourseDTO:
        pass

    '''
@dataclass
class RequestDraftCourseDTO:
    title: str
    overview: Optional[str]
    category:List[int] # ex: 'Development>databsed design' has to be part of predefined Category model
                        # if secondary category not in model : instructor can give own category:
                        # the secondary category is dealt with during approval process
    thumbnail_file: Optional[UploadedFile] = None

    def __post_init__(self):
        if self.category is None:
            raise EmptyCategoryException()
        if self.title is None:
            raise EmptyTitleException()
'''
    def does_course_exist(self, course_id:int) -> bool:
        if Course.objects.filter(id=course_id).exists():
            return True
        else:
            return False
