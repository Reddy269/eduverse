from catalog.interactors.dtos import RequestUpdateDraftDTO
from catalog.interactors.ports.storage_interfaces import CourseStorageInterface
from ports.storage_interfaces import CategoryStorageInterface
from .category_rules import CategoryRules
from catalog.interactors.exceptions import InvalidInputException

class UpdateCourseInteractor:
    def __init__(self,
                 course_storage:CourseStorageInterface,
                 category_storage:CategoryStorageInterface,
                 category_rules:CategoryRules
                 ):
        self.course_storage = course_storage
        self.category_storage = category_storage
        self.category_rules = category_rules

    def save_draft(self,request: RequestUpdateDraftDTO):
        #rules for the update details
        if not request.category or self.category_rules(request.category):
            raise InvalidInputException

        self.course_storage.update_draft(request)



