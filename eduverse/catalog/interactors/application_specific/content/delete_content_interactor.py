from catalog.interactors.ports.storage_interfaces.media_storage_interface import MediaStorageInterface
from dtos import RequestDeleteContentDTO

class DeleteContentInteractor(MediaStorageInterface):
    def __init__(self, storage: MediaStorageInterface):
        self.storage = storage

    def delete(self, request: RequestDeleteContentDTO):
        #rule to check if filename exists
        self.storage.delete(request)

