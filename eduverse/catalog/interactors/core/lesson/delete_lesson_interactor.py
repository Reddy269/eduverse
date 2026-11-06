from lesson_storage import LessonStorage
from ports.storage_interfaces import LessonStorageInterface


class DeleteLessonFInteractor:
    def __init__(self,
                 lesson_storage:LessonStorageInterface,
                 ):
        self.lesson_storage = lesson_storage

    def __call__(self, lesson_id:int):
        # check if lesson exitsts

        self.lesson_storage.delete_lesson(lesson_id)
