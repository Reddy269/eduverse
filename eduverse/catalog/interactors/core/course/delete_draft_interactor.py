from catalog.interactors.dtos import CourseDTO
from catalog.interactors.ports.storage_interfaces import CourseStorageInterface

class DeleteDraftInteractor:
    def __init__(self,
                 storage: CourseStorageInterface
                 ):
        self.storage = storage

    def delete_draft(self,request: CourseDTO):
        self.storage.delete_draft(request)
