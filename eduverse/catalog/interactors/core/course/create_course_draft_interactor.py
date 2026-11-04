from catalog.interactors.dtos import RequestDraftCourseDTO
from catalog.interactors.ports.storage_interfaces import CourseStorageInterface

class CreatCourseDraftInteractor:
    def __init__(self,
                 storage: CourseStorageInterface,
                 ):
        self.storage = storage
    def save_draft(self,request: RequestDraftCourseDTO):
        # rules for the DTO
        self.storage.create_draft(request)

    









