from catalog.interactors.ports.storage_interfaces import SectionStorageInterface, LessonStorageInterface


class AddLessonToSectionInteractor:
    def __init__(self,
                 section_storage:SectionStorageInterface,
                 lesson_storage:LessonStorageInterface,
                 ):
        self.section_storage = section_storage
        self.lesson_storage = lesson_storage

    def __call__(self, lesson_id:int,course_section_id:int):
        # check if both lesson and section exist
        self.lesson_storage.add_lesson_to_section(lesson_id,course_section_id)
