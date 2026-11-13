from catalog.interactors.dtos import RequestDraftCourseDTO
from catalog.interactors.ports.storage_interfaces import CourseStorageInterface
from catalog.interactors.ports.storage_interfaces import CategoryStorageInterface
from catalog.interactors.exceptions import InvalidInputException, InvalidCategoryException
from .category_rules import CategoryRules
from django.db import transaction

class CreatCourseDraftInteractor:
    def __init__(self,
                 course_storage: CourseStorageInterface,
                 category_storage: CategoryStorageInterface,
                 category_rules: CategoryRules
                 ):
        self.course_storage = course_storage
        self.category_storage = category_storage
        self.category_rules = category_rules
    def save_draft(self,request: RequestDraftCourseDTO):
        # rules for the DTOs content

        # any course can be part of upto 2 main categories and upto 4 sub-categories
        if not request.category or not self.category_rules(request.category):
            raise InvalidCategoryException("invalid category")

        # makes the db calls for Course and CourseCategory ; if anything fails it'll roll back
        with transaction.atomic():
            course_id = self.course_storage.create_draft(request)
            for category_id in request.category:
                self.category_storage.assign_category_to_course(course_id = course_id,category_id =  category_id)

        return f"course: {course_id} . {request.title} has been created "




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


    









