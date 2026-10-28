"""In-memory storages so interactors can be tested with no database and no Django."""
from accountz.interactors.storage_interfaces.admin_storage_interface import (
    AdminStorageInterface,
)
from accountz.interactors.storage_interfaces.dtos import (
    AdminDTO,
    InstructorDTO,
    StudentDTO,
)
from accountz.interactors.storage_interfaces.instructor_storage_interface import (
    InstructorStorageInterface,
)
from accountz.interactors.storage_interfaces.student_storage_interface import (
    StudentStorageInterface,
)


class FakeStudentStorage(StudentStorageInterface):
    def __init__(self):
        self.students = {}
        self._next_id = 1

    def get_student(self, user_id):
        return self.students.get(user_id)

    def create_student(self, name, email, password):
        dto = StudentDTO(user_id=self._next_id, name=name, email=email)
        self.students[dto.user_id] = dto
        self._next_id += 1
        return dto

    def is_email_taken(self, email):
        return any(s.email == email for s in self.students.values())


class FakeInstructorStorage(InstructorStorageInterface):
    def __init__(self):
        self.instructors = {}
        self._next_id = 1000

    def get_instructor(self, user_id):
        return self.instructors.get(user_id)

    def create_instructor(self, name, email, password, department):
        dto = InstructorDTO(
            user_id=self._next_id, name=name, email=email, department=department
        )
        self.instructors[dto.user_id] = dto
        self._next_id += 1
        return dto

    def is_email_taken(self, email):
        return any(i.email == email for i in self.instructors.values())


class FakeAdminStorage(AdminStorageInterface):
    def __init__(self, admin_ids=()):
        self.admins = {
            uid: AdminDTO(user_id=uid, name="Admin", email=f"admin{uid}@example.com")
            for uid in admin_ids
        }

    def get_admin(self, user_id):
        return self.admins.get(user_id)

    def is_admin(self, user_id):
        return user_id in self.admins
