from catalog.interactors.ports.storage_interfaces import SectionStorageInterface



class RemoveSectionFromCourseInteractor:
    def __init__(self,
                 section_storage:SectionStorageInterface,
                 ):
        self.section_storage = section_storage

    def __call__(self, section_id:int,course_id):
        # first check if both exist
        # check if both have a link
        self.section_storage.remove_section_from_course(section_id,course_id)

