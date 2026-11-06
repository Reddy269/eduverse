from catalog.interactors.ports.storage_interfaces import InstructorStorageInterface
from catalog.interactors.dtos import RequestOnboardInstructorDTO
from catalog.models import InstructorProfile


class InstructorStorage(InstructorStorageInterface):
    def save_profile(self,request:RequestOnboardInstructorDTO):
        instructor_profile = InstructorProfile.objects.create(
            username = request.username,
            display_name = request.display_name,
            email = request.email,
            dob = request.dob,
            bio = request.bio,
            expertise = request.category,
            display_profile_image = request.dp_file,
        )
        instructor_profile.save()

    def does_instructor_exist(self,instructor_id:int) -> bool:
        if InstructorProfile.objects.get(id = instructor_id).exists():
            return True
        else:
            return False



'''
class RequestOnboardInstructorDTO:
    username: str
    display_name: str
    email: str
    dob: str
    bio: str
    category: str
    dp_file: 


    def __post_init__(self):
        pass
        
class InstructorProfile(models.Model):
    username = models.CharField(max_length = 20,unique = True,null = True,blank = True)
    email = models.CharField(max_length = 20,unique = True,null = True,blank = True)
    dob = models.DateField(null=True,blank=True)
    display_name = models.CharField(max_length=100)
    bio = models.TextField(null=True,blank=True)
    display_profile_image = models.ImageField(upload_to="instructors/dp", blank=True)
    expertise = models.CharField(max_length=100,null=True,blank=True)

'''