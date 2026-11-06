from catalog.interactors.dtos import RequestCreateLessonDTO
from catalog.interactors.ports.storage_interfaces import LessonStorageInterface


class CreateLessonInteractor:
    def __init__(self,
                 lesson_storage:LessonStorageInterface):
        self.lesson_storage = lesson_storage

    def __call__(self, request:RequestCreateLessonDTO):
        #check if dto is valid

        self.lesson_storage.create_lesson(request)
