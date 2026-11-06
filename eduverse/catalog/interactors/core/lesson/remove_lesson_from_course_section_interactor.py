from catalog.interactors.ports.storage_interfaces import SectionStorageInterface , LessonStorageInterface


class RemoveLessonFromSectionInteractor:
    def __init__(self,
                 lesson_storage:LessonStorageInterface,
                 section_storage:SectionStorageInterface
                 ):
        self.lesson_storage = lesson_storage
        self.section_storage = section_storage

    def __call__(self, lesson_id:int,course_section_id:int):
        # check if it exists
        self.lesson_storage.remove_lesson_from_section(lesson_id,course_section_id)