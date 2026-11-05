from catalog.interactors.ports.storage_interfaces import CourseStorageInterface
from dtos import RequestDraftCourseDTO,RequestUpdateDraftDTO,RequestGetCourseDTO,CourseDTO
from catalog.models import Course


class CourseStorage(CourseStorageInterface):


    def create_draft(self, request: RequestDraftCourseDTO) -> bool:
        course = Course()

    def update_draft(self, request: RequestUpdateDraftDTO) -> bool:
        pass

    def change_status(self, request) -> bool:
        pass

    def delete_draft(self, request) -> bool:
        pass

    def get_course(self, request: RequestGetCourseDTO) -> CourseDTO:
        pass

'''
@dataclass
class RequestDraftCourseDTO:
    title: str
    overview: Optional[str]
    category:List[str] # ex: 'Development>databsed design' has to be part of predefined Category model
                        # if secondary category not in model : instructor can give own category:
                        # the secondary category is dealt with during approval process
    thumbnail_file: Optional[UploadedFile] = None
'''