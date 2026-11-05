from django.db import models
from django.db.models.functions import Lower
from catalog.interactors.dtos import LessonType

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"), "parent",
                name = "unique_parent_child",
            ),
        ]

class InstructorProfile(models.Model):
    username = models.CharField(max_length = 20,unique = True,null = True,blank = True)
    email = models.CharField(max_length = 20,unique = True,null = True,blank = True)
    dob = models.DateField(null=True,blank=True)
    display_name = models.CharField(max_length=100)
    bio = models.TextField(null=True,blank=True)
    display_profile_image = models.ImageField(upload_to="instructors/", blank=True)
    expertise = models.CharField(max_length=100,null=True,blank=True)


# Create your models here.
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


class CourseCategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

def file_path(instance, filename):
    return f"{instance.content_type}/{filename}"

class Content(models.Model):
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.PROTECT, null=True,blank=True)
    name = models.CharField(max_length = 20)
    content_type = models.CharField(max_length = 20,choices = [(t.value,t.name) for t in LessonType])
    file = models.FileField(upload_to=file_path)

class Lesson(models.Model):
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE, null = True, blank = True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    content = models.OneToOneField(Content, on_delete=models.PROTECT , null=True,blank=True)
    lesson_type = models.CharField(max_length=100)

class Section(models.Model):
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE, null= True, blank = True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    estimated_duration = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

class CourseSection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    reference_order = models.IntegerField(null=True,blank=True)

class LessonSection(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    reference_order = models.IntegerField(null=True,blank=True)

FILE_TYPES = {".mp4":"videos",".pdf":"articles"}

class Test(models.Model):
    file = models.FileField(upload_to="test/yo")

