from django.db import models
from django.db.models.functions import Lower


# Create your models here.
course_status = [
    ("DRA","in-draft"),
    ("COM","completed"),
    ("PUB","published"),
]

class Course(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=3, choices=course_status, default="DRA")
    prerequisites = models.TextField(null=True,blank=True)
    overview = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField(null=True,blank=True)
    about_instructor = models.TextField(null=True,blank=True)
    listing_image_metadata = models.TextField(null=True,blank=True)
    preview_content_metadata = models.TextField(null=True,blank=True)


class Category(models.Model):
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
class CourseCategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    reference_order = models.IntegerField()
    reference_module = models.CharField(max_length=100)
    lesson_type = models.CharField(max_length=100)
    content_metadata = models.TextField()


FILE_TYPES = {".mp4":"videos",".pdf":"srticles"}

def file_path(instance, filename):
    ext = filename.split('.')[-1]
    path = FILE_TYPES.get(ext)
    return f"{path}/{filename}"

class Content(models.Model):
    name = models.CharField(max_length = 20)
    file = models.FileField(upload_to=file_path)



