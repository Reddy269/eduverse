from catalog.interactors.ports.storage_interfaces.media_storage_interface import MediaStorageInterface
from dtos import RequestUpdateContentDTO

class ReplaceContentInteractor(MediaStorageInterface):
    def __init__(self,storage:MediaStorageInterface):
        self.storage = storage

    def update(self, request:RequestUpdateContentDTO):
        #rule to check if filename exists to be replaced
        #rule to check if content is of the type mp4 or pdf
        self.storage.update(request)

