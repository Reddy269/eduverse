import profile

from catalog.interactors.ports.gateway_interfaces import InstructorProfileInterface
from catalog.interactors.dtos import ProfileDTO
from accounts.interactors.core import GetUserProfileInteractor
from accounts.adapters.store import UserStorage


class InstructorProfile(InstructorProfileInterface):
    def get_profile(self,request:str):
        storage = UserStorage()
        get_profile_interactor = GetUserProfileInteractor(storage)
        return get_profile_interactor.get_user_profile(request,'instructor')

    def update_profile(self,request):
        pass
