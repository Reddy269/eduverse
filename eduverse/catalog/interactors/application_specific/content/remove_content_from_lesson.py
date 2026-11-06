from catalog.interactors.ports.storage_interfaces import ContentStorageInterface

class RemoveContentFromLesson(ContentStorageInterface):

    def __init__(self,
                 content_storage: ContentStorageInterface
                 ):
        self.content_storage = content_storage

    def __call__(self, content_id: int, lesson_id: int):
        # check if both exists
        self.content_storage.remove_content_from_lesson(content_id, lesson_id)


