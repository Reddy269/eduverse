from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Union, BinaryIO
from datetime import date

from django.core.files.uploadedfile import UploadedFile

from .exceptions import InvalidCategoryException

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

#course-related DTOs
@dataclass
class RequestDraftCourseDTO:
    title: str
    overview: Optional[str]
    category:List[str] # ex: 'Development>databsed design' has to be part of predefined Category model
                        # if secondary category not in model : instructor can give own category:
                        # the secondary category is dealt with during approval process
    thumbnail_file: Optional[UploadedFile] = None

@dataclass
class RequestUpdateDraftDTO:
    title: Optional[str]
    overview: Optional[str]
    prerquisites: Optional[str]
    outcomes: Optional[str]
    duration: Optional[str]
    about_instructor: Optional[str]
    preview_content_file: Optional[UploadedFile] = None

@dataclass
class CourseDTO:
    # all the course details : need this DTO for checking during status changes and
    title: str



@dataclass
class RequestGetCourseDTO:
    title: str

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














