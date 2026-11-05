from catalog.interactors.ports.storage_interfaces import CourseStorageInterface
from catalog.interactors.exceptions import InvalidCourseException, InvalidInputException, CourseNotEditableException
from catalog.interactors.dtos import CourseStatus


class RevertCourseToDraftInteractor:
    def __init__(self, course_storage:CourseStorageInterface):
        self.course_storage = course_storage

    def __call__(self,request:int|str):
        #check the status of the course if already in draft : pass ; if in completed :-just change status to draft;
        #if in pending-approval : need to send request to gateway to revert the request in admin
        #if in published : need to send request to gateway to admin
        try:
            course = self.course_storage.get_course(request)
        except InvalidInputException as e:
            raise InvalidCourseException(str(e)) from e

        if course.status == CourseStatus.DRAFT:
            pass

        elif course.status == CourseStatus.COMPLETED:
            course.status = CourseStatus.DRAFT  # editing a completed course sends it back to draft

        elif course.status == CourseStatus.PENDING:
            raise CourseNotEditableException(course.status)  # TODO: decide the rule

        elif course.status == CourseStatus.PUBLISHED:
            raise CourseNotEditableException(course.status)  # TODO: decide the rule

        else:
            raise ValueError(f"unknown status: {course.status}")