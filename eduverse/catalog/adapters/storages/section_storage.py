from catalog.interactors.ports.storage_interfaces import SectionStorageInterface
from dtos import RequestAddSectionDTO
from catalog.models import Section

class SectionStorage(SectionStorageInterface):
    def add_section(self, request:RequestAddSectionDTO):
        Section.objects.create()

    def assign_scetion_to_course(self, section_id,course_id):
        pass