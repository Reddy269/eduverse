from accounts.interactors.ports import UserStorageInterface
from accounts.models import Student,Instructor
from datetime import datetime

from accounts.interactors.dtos import RequestRegisterUserDTO


class UserStorage(UserStorageInterface):

    def register_email(self,request):
        if request.UserType.value == 'Student':
            dob_date = datetime.strptime(request.DOB, "%Y-%m-%d").date()
            student = Student.objects.create(name = request.name, email = request.email, dob = dob_date)
            student.save()


    def create_user(self,request:RequestRegisterUserDTO):
        if request.user_type.value == "student":
            student = Student.objects.get(email = request.email)
            student.username = request.username
            student.password = request.password
            student.save()


    def get_user_id(self,email_or_username:str,usertype:str):
        if usertype == "instructor":
            return Instructor.objects.get(email = email_or_username).instructor_id
        elif usertype == "student":
            return Student.objects.get(email = email_or_username).user_id

    def delete_user(self):
        pass

    def get_user_profile(self,username:str,usertype:str):
        if usertype == "instructor":
            instructor = Instructor.objects.get(username = username)
            return [instructor.username,instructor.email,instructor.name,instructor.dob]
        return None




"""class RequestCreateUserDTO:
    usertype: UserType
    email: str
    username: str
    password: str
    confirm_password: str"""

