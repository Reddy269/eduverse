from abc import ABC, abstractmethod

from catalog.interactors.dtos import CourseDTO, RequestDraftCourseDTO, RequestUpdateDraftDTO, RequestGetCourseDTO, UploadedFile


class CourseStorageInterface(ABC):
    @abstractmethod
    # returns the newley created course_id
    def create_draft(self, request: RequestDraftCourseDTO) -> int:
        pass
    @abstractmethod
    def update_draft(self, request: RequestUpdateDraftDTO) -> bool:
        pass
    @abstractmethod
    def change_status(self, request:CourseDTO) -> bool:
        pass
    @abstractmethod
    def delete_draft(self, request: int|str) -> bool:
        pass
    @abstractmethod
    def get_course(self,request: int|str) ->CourseDTO :
        pass
    @abstractmethod
    def does_course_exist(self,course_id:int) -> bool:
        pass




'''
class RequestDraftCourseDTO:
    title: str
    overview: Optional[str]
    category:List[str] # ex: 'Development>databsed design' has to be part of predefined Category model
                        # if secondary category not in model : instructor can give own category:
                        # the secondary category is dealt with during approval process
    thumbnail_file: Optional[UploadedFile] = None

'''

