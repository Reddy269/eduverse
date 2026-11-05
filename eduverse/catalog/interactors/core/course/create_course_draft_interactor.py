from catalog.interactors.dtos import RequestDraftCourseDTO
from catalog.interactors.ports.storage_interfaces import CourseStorageInterface
from catalog.interactors.ports.storage_interfaces import CategoryStorageInterface
from catalog.interactors.exceptions import InvalidCourseException
from exceptions import InvalidInputException
from .category_rules import CategoryRules

class CreatCourseDraftInteractor:
    def __init__(self,
                 course_storage: CourseStorageInterface,
                 category_storage: CategoryStorageInterface,
                 ):
        self.course_storage = course_storage
        self.category_storage = category_storage
    def save_draft(self,request: RequestDraftCourseDTO):
        # rules for the DTOs content
        # any course can be part of upto 2 main categories and upto 4 sub-categories
        category_rules = CategoryRules(self.category_storage)
        if not category_rules(request.category):
            raise InvalidInputException
        course_id = self.course_storage.create_draft(request)
        for category_id in request.category:
            self.category_storage.assign_category_to_course(course_id, category_id)













    '''
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


    









