from catalog.adapters.storages import InstructorStorage,CourseStorage
from catalog.interactors.dtos import RequestUpdateDraftDTO
from exceptions import InvalidInputException


class AssignCourseToInstructorInteractor:
    def __init__(self,
                 course_storage:CourseStorage,
                 instructor_storage:InstructorStorage,
                 ):
        self.course_storage = course_storage
        self.instructor_storage = instructor_storage

    def __call__(self,instructor_id: int,course_id:int):

        if not self.instructor_storage.does_instructor_exist(instructor_id):
            raise InvalidInputException()

        if not self.course_storage.does_course_exist(course_id):
            raise InvalidInputException()

        # get instructor_id then create RequestUpdateDraft DTO with course_id and instructor_id
        request = RequestUpdateDraftDTO(id = course_id, instructor_id = instructor_id)
        self.course_storage.update_draft(request)


