from typing import Optional

from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction

from accounts.interactors.exceptions import EmailAlreadyExists
from interactors.ports.storage_interfaces import InstructorDTO
from interactors.ports.storage_interfaces import (
    InstructorStorageInterface,
)
from accounts.models import Instructor
from accounts.storages.utils import is_email_taken


class InstructorStorage(InstructorStorageInterface):

    def get_instructor(self, user_id: int) -> Optional[InstructorDTO]:
        instructor = Instructor.objects.filter(user_id=user_id).first()
        if instructor is None:
            return None
        return self._to_dto(instructor)

    def create_instructor(
        self, name: str, email: str, password: str, department: Optional[str]
    ) -> InstructorDTO:
        User = get_user_model()
        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    username=email, email=email, password=password
                )
                instructor = Instructor.objects.create(
                    user=user, name=name, email=email, department=department
                )
        except IntegrityError:
            raise EmailAlreadyExists
        return self._to_dto(instructor)

    def is_email_taken(self, email: str) -> bool:
        return is_email_taken(email)

    @staticmethod
    def _to_dto(instructor: Instructor) -> InstructorDTO:
        return InstructorDTO(
            user_id=instructor.user_id,
            name=instructor.name,
            email=instructor.email,
            department=instructor.department,
        )
