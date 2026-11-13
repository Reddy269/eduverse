from abc import ABC, abstractmethod



class InstructorProfileInterface(ABC):
    @abstractmethod
    def get_profile(self,request:str):
        pass
    @abstractmethod
    def update_profile(self,request):
        pass