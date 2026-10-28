from catalog.interactors.ports.storage_interfaces.media_storage_interface import MediaStorageInterface
from dtos import RequestAddContentDTO, RequestDeleteContentDTO, RequestUpdateContentDTO


class MediaStorage(MediaStorageInterface):
    def save(self, request:RequestAddContentDTO):
        pass

    def delete(self, request:RequestDeleteContentDTO):
        pass

    def update(self, request:RequestUpdateContentDTO):
        pass

