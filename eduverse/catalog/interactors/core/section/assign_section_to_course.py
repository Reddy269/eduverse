from ports.storage_interfaces import SectionStorageInterface


class AssignSectionToCourse:
    def __init__(self,
                 section_storage:SectionStorageInterface,
                 ):
        self.section_storage = section_storage

    def __call__(self,section_id:int,course_id:int):

        # check if both section and course exist then call adapter

        self.section_storage.assign_section_to_course(section_id,course_id)

