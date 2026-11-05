from catalog.interactors.dtos import RequestInstructorProfileDTO , RequestOnboardInstructorDTO
from catalog.interactors.ports.storage_interfaces import InstructorStorageInterface
from catalog.interactors.ports.gateway_interfaces import InstructorProfileInterface

class OnboardInstructorInteractor:
    def __init__(self,
                 storage: InstructorStorageInterface,
                 gateway: InstructorProfileInterface,
                 ):
        self.storage = storage
        self.gateway = gateway


    def get_profile(self,request:RequestInstructorProfileDTO):
        # rules for RequestInstructorProfileDTO
        profile_details = self.gateway.get_profile(request)
        return profile_details


    def save_profile(self,request:RequestOnboardInstructorDTO):
        self.storage.save_profile(request)
