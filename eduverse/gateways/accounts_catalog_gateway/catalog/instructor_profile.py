import profile

from catalog.interactors.ports.gateway_interfaces import InstructorProfileInterface
from catalog.interactors.dtos import RequestInstructorProfileDTO , ProfileDTO
from accounts.adapters.store import UserStorage


class InstructorProfile(InstructorProfileInterface):
    def get_profile(self,request:RequestInstructorProfileDTO):
        username = request.username
        storage = UserStorage()
        profile_details_list = storage.get_user_profile(username,"instructor")
        profile_details = ProfileDTO(
                                username = profile_details_list[0],
                                email = profile_details_list[1],
                                display_name = profile_details_list[2],
                                dob = profile_details_list[3],
                                )
        return profile_details

    def update_profile(self,request):
        pass
