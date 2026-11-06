from ports.storage_interfaces import ContentStorageInterface, LessonStorageInterface


class AddContentToLesson:
    def __init__(self,
                 content_storage:ContentStorageInterface,
                 lesson_storage:LessonStorageInterface
                 ):
        self.content_storage = content_storage
        self.lesson_storage = lesson_storage

    def __call__(self, content_id: int, lesson_id: int):
        #check if both exist

        self.content_storage.add_content_to_lesson(content_id, lesson_id)