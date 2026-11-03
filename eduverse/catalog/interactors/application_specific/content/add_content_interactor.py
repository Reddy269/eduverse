from catalog.interactors.ports.storage_interfaces.media_storage_interface import MediaStorageInterface
from dtos import  RequestAddContentDTO


class AddContentInteractor(MediaStorageInterface):
    def __init__(self,
                 storage: MediaStorageInterface
                 ):
        self.storage = storage

    def upload(self, request: RequestAddContentDTO):
        # rule to check if filename doesnt already exist
        # rule to check if content is actually either mp4 or pdf
        self.storage.save(request)
