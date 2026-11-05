from catalog.interactors.dtos import CourseDTO
from catalog.interactors.ports.storage_interfaces import CourseStorageInterface
from catalog.interactors.exceptions import InvalidCourseException

class DeleteDraftInteractor:
    def __init__(self,
                 storage: CourseStorageInterface
                 ):
        self.storage = storage

    def delete_draft(self,request: int|str) -> bool:
        # delete course from Course : should automatically delete from CourseCategory
        if self.storage.get_course(request) is not None:
            self.storage.delete_draft(request)
        else:
            raise InvalidCourseException(request)

