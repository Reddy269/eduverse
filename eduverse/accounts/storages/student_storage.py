from accounts.interactors.ports.storage_interfaces import UserStorageInterface
from accounts.models import Student
from accounts.interactors.dtos import UserDTO , RequestCreateUserDTO



class StudentStorage(UserStorageInterface):
    def create_user(self, request:RequestCreateUserDTO)->UserDTO:
        student = Student.objects.create(name=request.name, email=request.email, password=request.password)
        return UserDTO(id = student.user_id , name= student.name,email = student.email, usertype = 'student' )

    def is_email_taken(self, email: str) -> bool:
        return Student.objects.filter(email=email).exists()

    def get_user(self, email: str) -> UserDTO:
        pass
    def is_admin(self):
        pass
    def is_user_registered(self,email)->bool:
        if Student.objects.filter(email=email).exists():
            return True
        return False






