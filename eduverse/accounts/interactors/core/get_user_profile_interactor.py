from accounts.interactors.ports import UserStorageInterface
from accounts.interactors.dtos import UserProfileDTO


class GetUserProfileInteractor:
    def __init__(self,
                 store: UserStorageInterface,
                 ):
        self.store = store
    def get_user_profile(self,user_id:str,usertype:str) -> UserProfileDTO:
        return self.store.get_user_profile(user_id,usertype)