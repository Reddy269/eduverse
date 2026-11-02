from accounts.interactors.ports import StorageValidationInterface
from accounts.models import Student,Instructor



class StoreValidation(StorageValidationInterface):
    def is_email_taken(self,email:str,usertype:str) -> bool:
        if usertype == "student":
            if Student.objects.filter(email=email).exists():
                return True
        elif usertype == "instructor":
            if Instructor.objects.filter(email=email).exists():
                return True
        return False
    def is_username_taken(self,username:str,usertype:str) -> bool:
        if usertype == "student":
            if Student.objects.filter(username=username).exists():
                return True
        elif usertype == "instructor":
            if Instructor.objects.filter(username=username).exists():
                return True
        return False
    def is_under_registration(self,email:str,usertype:str) -> bool:
        if usertype == "student":
            student = Student.objects.get(email=email)
            if student.username:
                return False
        elif usertype == "instructor":
            instructor = Instructor.objects.get(email=email)
            if instructor.username:
                return False
        return True




