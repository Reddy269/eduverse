import uuid

from django.conf import settings
from django.db import models


class Student(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Student<{self.user_id}: {self.name}>"


class Instructor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="instructor_profile"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    department = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Instructor<{self.user_id}: {self.name}>"


class Admin(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="admin_profile"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Admin<{self.user_id}: {self.name}>"
