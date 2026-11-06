from dataclasses import dataclass
from enum import Enum
from typing import Optional, List
from datetime import date

from django.core.files.uploadedfile import UploadedFile

from .exceptions import (EmptyTitleException,
                         EmptyCategoryException, InvalidLessonTypeException,
                         InvalidUpdateRequestException, InvalidInputException, )

class LessonType(str, Enum):
    VIDEO = "video"
    ARTICLE = "article"

class ItemType(str, Enum):
    LESSON = "lesson"
    QUIZ = "quiz"
class QuestionType(str, Enum):
    MCQ = "MCQ"
    CODING = "CODING"

class Scope(str, Enum):
    LESSON = "lesson"
    MODULE = "module"
    FINAL = "final"

class CourseStatus(str, Enum):
    DRAFT = "in-draft"
    PUBLISHED = "published"
    COMPLETED = "completed"
    PENDING = "pending-approval"

class FileType(Enum):
    VIDEO = (".mp4", ".webm", ".mov")
    ARTICLE = (".pdf", ".txt", ".md")




#lesson-related DTOs
@dataclass
class RequestCreateLessonDTO:
    title: str
    description: Optional[str]
    lesson_type: str

    def __post_init__(self):

        if self.title is None:
            raise InvalidInputException()

        try:
            self.lesson_type = LessonType(self.lesson_type)
        except ValueError:
            InvalidLessonTypeException(self.lesson_type)

class RequestAssignContentToLessonDTO:
    lesson_id: int
    content_id: int

class RequestUpdateLessonDTO:
    title: Optional[str]
    description: Optional[str]
    lesson_type: Optional[str]
    def _post_init__(self):
        try:
            self.lesson_type = LessonType(self.lesson_type)
        except ValueError:
            InvalidLessonTypeException(self.lesson_type)


'''
class Lesson(models.Model):
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE, null = True, blank = True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    content = models.OneToOneField(Content, on_delete=models.PROTECT , null=True,blank=True)
    lesson_type = models.CharField(max_length=100)

'''

#section-related DTOs
@dataclass
class RequestAddSectionDTO:
    title: str
    description: Optional[str]
    estimated_duration: Optional[int]

    def _post_init__(self):
        if not self.title.strip():
            raise InvalidInputException()


'''
class Section(models.Model):
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE, null= True, blank = True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    estimated_duration = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

'''
#course-related DTOs
@dataclass
class RequestDraftCourseDTO:
    title: str
    overview: Optional[str]
    category:List[int] # ex: 'Development>databsed design' has to be part of predefined Category model
                        # if secondary category not in model : instructor can give own category:
                        # the secondary category is dealt with during approval process
    thumbnail_file: Optional[UploadedFile] = None

    def __post_init__(self):
        if self.category is None:
            raise EmptyCategoryException()
        if self.title is None:
            raise EmptyTitleException()

@dataclass
class RequestUpdateDraftDTO:
    id: int
    instructor_id: int
    title: Optional[str]
    overview: Optional[str]
    prerequisites: Optional[str]
    outcomes: Optional[str]
    overview : Optional[str]
    duration: Optional[str]
    about_instructor: Optional[str]
    thumbnail_image: Optional[UploadedFile]
    preview_content_file: Optional[UploadedFile]
    category: Optional[List[int]]

    def _post_init__(self):
        if self.id is None:
            raise InvalidUpdateRequestException
@dataclass
class RequestUpdateCategoryDTO:
    category : List[int]
    # ex: 'Development>databsed design' has to be part of predefined Category model
    # if secondary category not in model : instructor can give own category:
    # the secondary category is dealt with during approval process

@dataclass
class CourseDTO:
    # all the course details : need this DTO for checking during status changes and
    id: int
    title: str
    status: CourseStatus
    prerequisites: Optional[str]
    overview: Optional[str]
    outcomes: Optional[str]
    duration: Optional[str]
    overview : Optional[str]
    outcomes : Optional[str]
    about_instructor: Optional[str]
    thumbnail_image: Optional[UploadedFile]
    preview_content_file: Optional[UploadedFile]



'''
course_status = [
    ("DRA","in-draft"),
    ("COM","completed"),
    ("PEN","pending-approval"),
    ("PUB","published"),
]
class Course(models.Model):
    id  = models.AutoField(primary_key=True)
    instructor = models.ForeignKey(InstructorProfile,on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=100,unique=True)
    status = models.CharField(max_length=3, choices=course_status, default="DRA")
    prerequisites = models.TextField(null=True,blank=True)
    overview = models.TextField()
    outcomes = models.TextField(null=True,blank=True)
    duration = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    about_instructor = models.TextField(null=True,blank=True)
    thumbnail_image = models.ImageField(null=True,blank=True)
    preview_content_file = models.FileField(null=True,blank=True)
    course_code = models.CharField(max_length=100,null=True,blank=True)
'''



@dataclass
class RequestGetCourseDTO:
    id : Optional[int]
    title: Optional[str]

'''
class Course(models.Model):
    instructor = models.ForeignKey(InstructorProfile,on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=3, choices=course_status, default="DRA")
    prerequisites = models.TextField(null=True,blank=True)
    overview = models.TextField()
    outcomes = models.TextField(null=True,blank=True)
    duration = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    about_instructor = models.TextField(null=True,blank=True)
    thumbnail_image = models.ImageField(null=True,blank=True)
    preview_content_file = models.FileField(null=True,blank=True)
    course_code = models.CharField(max_length=100,null=True,blank=True)
'''

#Onboarding-related DTOs
@dataclass
class RequestOnboardInstructorDTO:
    username: str
    display_name: str
    email: str
    dob: date
    bio: str
    category: str
    dp_file: Optional[UploadedFile]


    def __post_init__(self):
        pass

@dataclass
class RequestInstructorProfileDTO:
    username: str

@dataclass
class ProfileDTO:
    username: str
    email: str
    display_name: str
    dob: date


#content-related DTOs

@dataclass
class RequestAddContentDTO:
    name: str
    content_type: str
    content: UploadedFile

    def __post_init__(self):

        def __post_init__(self):
            if not self.name or not self.name.strip():
                raise InvalidInputException
            self.name = self.name.strip()

            if not self.content_type or not str(self.content_type).strip():
                raise InvalidInputException

            if self.content is None:
                raise InvalidInputException
            if not getattr(self.content, "name", None):
                raise InvalidInputException
            if self.content.size == 0:
                raise InvalidInputException

            try:
                self.content_type = LessonType(self.content_type)
            except ValueError:
                raise InvalidLessonTypeException(self.content_type)


'''
def file_path(instance, filename):
    return f"{instance.content_type}/{filename}"

class Content(models.Model):
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.PROTECT, null=True,blank=True)
    name = models.CharField(max_length = 20)
    content_type = models.CharField(max_length = 20,choices = [(t.value,t.name) for t in LessonType])
    file = models.FileField(upload_to=file_path)
'''













