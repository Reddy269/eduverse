from accounts.interactors.ports import UserStorageInterface
from accounts.interactors.dtos import RequestRegisterEmailDTO, RequestCreateUserDTO
from accounts.models import Student,Instructor
from datetime import datetime


class UserStorage(UserStorageInterface):

    def register_email(self,request:RequestRegisterEmailDTO):
        if request.UserType.value == 'Student':
            dob_date = datetime.strptime(request.DOB, "%Y-%m-%d").date()
            student = Student.objects.create(name = request.name, email = request.email, dob = dob_date)
            student.save()


    def create_user(self,request:RequestCreateUserDTO):
        if request.username.value == "student":
            student = Student.objects.get(email = request.email)
            student.username = request.username
            student.password = request.password
            student.save()


    def get_user(self,request:RequestRegisterEmailDTO):
        pass


"""class RequestCreateUserDTO:
    usertype: UserType
    email: str
    username: str
    password: str
    confirm_password: str"""

