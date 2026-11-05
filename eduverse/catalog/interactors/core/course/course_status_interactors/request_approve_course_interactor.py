from dtos import CourseStatus
from ports.storage_interfaces import CourseStorageInterface
from catalog.interactors.exceptions import InvalidInputException, InvalidCourseException
from catalog.interactors.ports.gateway_interfaces import CourseStatusInterface

class RequestApproveCourseInteractor:
    def __init__(self,
                 course_storage: CourseStorageInterface,
                 course_status: CourseStatusInterface
                 ):
        self.course_storage = course_storage
        self.course_status = course_status

    def __call__(self,request: str|int):
        try:
            course = self.course_storage.get_course(request)
        except InvalidInputException as e:
            raise InvalidCourseException(str(e)) from e

        if not course.status == CourseStatus.COMPLETED:
            pass
            #raise error
        #code to send request