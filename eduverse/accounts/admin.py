from django.contrib import admin

from accounts.models import Admin, Instructor, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ( "name", "email", "created_at")
    search_fields = ("name", "email")


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ( "name", "email",  "created_at")
    search_fields = ("name", "email", "department")


@admin.register(Admin)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ( "user_id", "username")
    search_fields = ( "user_id", "username")
