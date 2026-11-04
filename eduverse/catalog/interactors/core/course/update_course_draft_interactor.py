from catalog.interactors.dtos import RequestUpdateDraftDTO
from catalog.interactors.ports.storage_interfaces import CourseStorageInterface



class UpdateCourseInteractor:
    def __init__(self,
                 storage:CourseStorageInterface,
                 ):
        self.storage = storage

    def save_draft(self,request: RequestUpdateDraftDTO):
        #rules for the update details
        self.storage.update_draft(request)



