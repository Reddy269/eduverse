import uuid

from django.conf import settings
from django.db import models, transaction


class Student(models.Model):
    user_id  =models.CharField(max_length=16, unique=True, null=True, blank=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    dob = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True , unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Student<{self.user_id}: {self.name}>"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)
            if not self.user_id:
                self.user_id = f"STU-{self.created_at:%y}-{self.pk:06d}"
                super().save(update_fields=["user_id"])



class Instructor(models.Model):
    user_id = models.CharField(max_length=16, unique=True, null=True, blank=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    dob = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Instructor<{self.user_id}: {self.name}>"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)
            if not self.user_id:
                self.user_id = f"IN-{self.created_at:%y}-{self.pk:06d}"
                super().save(update_fields=["user_id"])


class Admin(models.Model):
    user_id = models.CharField(max_length=16, unique=True, null=True, blank=True, editable=False)
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def save(self,*args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)
            if not self.user_id:
                self.user_id = f"AD-{self.created_at:%y}-{self.pk:06d}"
                super().save(update_fields=["user_id"])
