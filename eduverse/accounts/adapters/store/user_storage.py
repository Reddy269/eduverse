from accounts.interactors.ports import UserStorageInterface
from accounts.models import Student,Instructor
from datetime import datetime

from accounts.interactors.dtos import RequestRegisterUserDTO
from accounts.interactors.exceptions import InvalidUserTypeError
from accounts.interactors.exceptions import IdentifierDoesNotExistError
from accounts.interactors.dtos import UserProfileDTO


class UserStorage(UserStorageInterface):

    def register_email(self,request):
        if request.UserType.value == 'Student':
            dob_date = datetime.strptime(request.DOB, "%Y-%m-%d").date()
            student = Student.objects.create(name = request.name, email = request.email, dob = dob_date)
            student.save()


    def create_user(self,request:RequestRegisterUserDTO):
        if request.user_type.value == "student":
            student = Student.objects.create(
                name = request.name,
                email = request.email,
                dob = request.dob,
                username = request.username,
                password = request.password,


            )

        elif request.user_type.value == "instructor":
            instructor = Instructor.objects.create(
                name = request.name,
                email = request.email,
                dob = request.dob,
                username = request.username,
                password = request.password,
            )

        else:
            raise InvalidUserTypeError()


    def get_user_id(self,identifier:str,user_type:str,identifier_type:str)->int:
        if user_type =="student":
            if identifier_type == "username":
                student = Student.objects.get(username = identifier)
            elif identifier_type == "email":
               student = Student.objects.get(email = identifier)
            else:
               raise IdentifierDoesNotExistError('invalid identifier type')
            return student.user_id
        elif user_type =="instructor":
            if identifier_type == "username":
                instructor = Instructor.objects.get(username = identifier)
            elif identifier_type == "email":
                instructor = Instructor.objects.get(email = identifier)
            else:
                raise IdentifierDoesNotExistError('invalid identifier type')
            return instructor.user_id
        else :
            raise InvalidUserTypeError('invalid user type')


    def delete_user(self):
        pass

    def get_user_profile(self,user_id:str,user_type:str)->UserProfileDTO:
        if user_type == "instructor":
            instructor = Instructor.objects.get(user_id = user_id)
            instructor_profile = UserProfileDTO(user_id = user_id,
                                                name = instructor.name,
                                                email = instructor.email,
                                                username=instructor.username,
                                                dob = instructor.dob)
            return instructor_profile
        elif user_type == "student":
            student = Student.objects.get(user_id = user_id)
            student_profile = UserProfileDTO(user_id = user_id,
                                             name = student.name,
                                             email = student.email,
                                             username = student.username,
                                             dob = student.dob
                                             )
            return student_profile

        else:
            raise InvalidUserTypeError('invalid user type')

    '''
    class UserProfileDTO:
    user_id: str
    name: str
    email: str
    username: str
    dob: date
    

user_id = models.CharField(max_length=16, unique=True, null=True, blank=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    dob = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    '''

    def get_password(self,identifier:str,usertype:str,identifier_type:str)->str:
        if usertype == "instructor":
            if identifier_type == "username":
                instructor = Instructor.objects.get(username = identifier)
            elif identifier_type == "email":
                instructor = Instructor.objects.get(email = identifier)
            else:
                raise IdentifierDoesNotExistError('invalid identifier type')
            return instructor.password
        elif usertype == "student":
            if identifier_type == "username":
                student = Student.objects.get(username = identifier)
            elif identifier_type == "email":
                student = Student.objects.get(email = identifier)
            else:
                raise IdentifierDoesNotExistError('invalid identifier type')
            return student.password
        else :
            raise InvalidUserTypeError('invalid user type')





"""class RequestCreateUserDTO:
    usertype: UserType
    email: str
    username: str
    password: str
    confirm_password: str"""

'''
     @abstractmethod
    def create_user(self,request:RequestRegisterUserDTO):
        pass
    @abstractmethod
    def get_user_id(self,identifier:str,user_type:str,identifier_type:str):
        pass

    @abstractmethod
    def register_email(self, request):
        pass
    @abstractmethod
    def delete_user(self):
        pass

    @abstractmethod
    def get_user_profile(self,username:str,usertype:str):
        pass

    @abstractmethod
    def get_password(self,identifier:str,usertype:str,identifier_type:str):
        pass

'''
