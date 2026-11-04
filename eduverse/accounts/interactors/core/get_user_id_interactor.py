from accounts.interactors.dtos import RequestLoginUserDTO
from accounts.interactors.ports import UserStorageInterface


class GetUserIdInteractor:
    def __init__(self,
                 store:UserStorageInterface
                 ):
        self.store = store
    def get_user_id(self,username_or_email:str,usertype:str):
        return self.store.get_user_id(username_or_email,usertype)
