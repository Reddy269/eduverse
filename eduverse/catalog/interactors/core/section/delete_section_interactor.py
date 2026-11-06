from catalog.interactors.ports.storage_interfaces import SectionStorageInterface



class DeleteSectionInteractor:
    def __init__(self,
                 section_storage:SectionStorageInterface,
                 ):
        self.section_storage = section_storage

    def __call__(self, section_id:int):
        # check if section is valid

        self.section_storage.delete_section(section_id)

