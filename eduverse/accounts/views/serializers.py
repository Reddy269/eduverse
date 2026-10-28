from django.contrib.auth import password_validation
from rest_framework import serializers


class CreateStudentRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=8, max_length=128)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class CreateInstructorRequestSerializer(CreateStudentRequestSerializer):
    department = serializers.CharField(
        max_length=100, required=False, allow_blank=True, allow_null=True, default=None
    )


class StudentResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()


class InstructorResponseSerializer(StudentResponseSerializer):
    department = serializers.CharField(allow_null=True)
