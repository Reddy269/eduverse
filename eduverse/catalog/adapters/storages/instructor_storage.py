from catalog.interactors.ports.storage_interfaces import InstructorStorageInterface
from catalog.interactors.dtos import RequestOnboardInstructorDTO
from catalog.models import Instructor


class InstructorStorage(InstructorStorageInterface):
    def save_profile(self,request:RequestOnboardInstructorDTO):
        instructor_profile = Instructor.objects.create(
            id = request.id,
            username = request.username,
            name = request.display_name,
            email = request.email,
            dob = request.dob,
            bio = request.bio,
            expertise = request.category,
            display_profile_pic = request.dp_picture,
        )
        instructor_profile.save()

    '''
        class RequestOnboardInstructorDTO:
    id: str
    username: str
    display_name: str
    email: str
    dob: date
    bio: Optional[str] | None
    category: Optional[str] | None
    dp_picture: Optional[UploadedFile] | None
    
        class Instructor(models.Model):
        id = models.CharField(primary_key=True)
        username = models.CharField(max_length = 20)
        email = models.EmailField(max_length = 150)
        name = models.CharField(max_length = 20)
        dob = models.DateField(null=True, blank=True)
        display_profile_pic = models.ImageField(null=True, blank=True)
        bio = models.TextField()
        experience = models.TextField()
        '''


    def get_profile(self,request:RequestOnboardInstructorDTO) :
        pass

    def does_instructor_exist(self,instructor_id:int) -> bool:
        if Instructor.objects.get(id = instructor_id).exists():
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