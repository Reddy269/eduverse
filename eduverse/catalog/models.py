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

class Instructor(models.Model):
    id = models.CharField(primary_key=True)
    username = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 150)
    name = models.CharField(max_length = 20)
    dob = models.DateField(null=True, blank=True)
    display_profile_pic = models.ImageField(null=True, blank=True)
    bio = models.TextField()
    expertise = models.TextField()


class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, null=True)
    id = models.AutoField(primary_key=True)


class CourseCategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



'''
class Instructor(models.Model):
    user_id = models.CharField(max_length=16, unique=True, null=True, blank=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    dob = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

'''