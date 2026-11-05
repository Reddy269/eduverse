from catalog.interactors.dtos import RequestUpdateDraftDTO
from catalog.interactors.ports.storage_interfaces import CourseStorageInterface
from ports.storage_interfaces import CategoryStorageInterface
from .category_rules import CategoryRules

class UpdateCourseInteractor:
    def __init__(self,
                 course_storage:CourseStorageInterface,
                 category_storage:CategoryStorageInterface
                 ):
        self.course_storage = course_storage
        self.category_storage = category_storage

    def save_draft(self,request: RequestUpdateDraftDTO):
        #rules for the update details
        if request.category is not None:
            category_rules = CategoryRules(self.category_storage)
            category_rules(request.category)

        self.course_storage.update_draft(request)



