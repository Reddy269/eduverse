from catalog.interactors.ports.storage_interfaces import SectionStorageInterface
from catalog.interactors.dtos import RequestAddSectionDTO


class AddSectionInteractor:
    def __init__(self,
                 section_storage: SectionStorageInterface,
                 ):
        self.section_storage = section_storage

    def __call__(self,request:RequestAddSectionDTO):
        pass