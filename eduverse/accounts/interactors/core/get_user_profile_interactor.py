from accounts.interactors.ports import UserStorageInterface



class GetUserProfileInteractor:
    def __init__(self,
                 store: UserStorageInterface,
                 ):
        self.store = store
    def get_user_profile(self,username_or_email:str,usertype:str):
        return self.store.get_user_profile(username_or_email)