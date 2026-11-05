from catalog.interactors.dtos import CourseDTO
from catalog.interactors.ports.storage_interfaces import CourseStorageInterface

class CompleteCourseInteractor:
    def __init__(self,
                 storage:CourseStorageInterface,
                 ):
        self.storage = storage

    def complete_course(self,request: CourseDTO):
        course = self.storage.get_course(CourseDTO)
        # rules for course
        self.storage.change_status()