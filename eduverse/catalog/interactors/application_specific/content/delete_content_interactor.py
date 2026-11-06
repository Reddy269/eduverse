from catalog.interactors.ports.storage_interfaces import ContentStorageInterface


class DeleteContentInteractor:
    def __init__(self, content_storage: ContentStorageInterface):
        self.content_storage = content_storage

    def delete(self, content_id: int):
        #rule to check if it exists
        self.content_storage.delete_content(content_id)

