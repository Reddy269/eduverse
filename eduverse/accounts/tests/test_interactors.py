import unittest

from accountz.interactors.create_instructor_interactor import CreateInstructorInteractor
from accountz.interactors.create_student_interactor import CreateStudentInteractor
from accountz.interactors.exceptions import (
    EmailAlreadyExists,
    InstructorNotFound,
    InvalidName,
    NotAllowed,
    StudentNotFound,
)
from accountz.interactors.get_instructor_interactor import GetInstructorInteractor
from accountz.interactors.get_student_interactor import GetStudentInteractor
from accountz.tests.fakes import (
    FakeAdminStorage,
    FakeInstructorStorage,
    FakeStudentStorage,
)

PASSWORD = "S3cure-pass-123"
ADMIN_ID = 99


class CreateStudentInteractorTests(unittest.TestCase):
    def setUp(self):
        self.storage = FakeStudentStorage()
        self.interactor = CreateStudentInteractor(storage=self.storage)

    def test_strips_name_and_normalises_email(self):
        student = self.interactor.create_student("  Asha ", " Asha@Example.COM ", PASSWORD)
        self.assertEqual(student.name, "Asha")
        self.assertEqual(student.email, "asha@example.com")

    def test_blank_name_is_rejected(self):
        with self.assertRaises(InvalidName):
            self.interactor.create_student("   ", "a@example.com", PASSWORD)

    def test_duplicate_email_is_rejected_case_insensitively(self):
        self.interactor.create_student("Asha", "asha@example.com", PASSWORD)
        with self.assertRaises(EmailAlreadyExists):
            self.interactor.create_student("Other", "ASHA@example.com", PASSWORD)


class GetStudentInteractorTests(unittest.TestCase):
    def setUp(self):
        self.students = FakeStudentStorage()
        self.admins = FakeAdminStorage(admin_ids=[ADMIN_ID])
        self.student = self.students.create_student("Asha", "asha@example.com", PASSWORD)
        self.interactor = GetStudentInteractor(
            student_storage=self.students, admin_storage=self.admins
        )

    def test_student_can_view_self(self):
        result = self.interactor.get_student(
            user_id=self.student.user_id, requesting_user_id=self.student.user_id
        )
        self.assertEqual(result, self.student)

    def test_other_user_is_forbidden(self):
        with self.assertRaises(NotAllowed):
            self.interactor.get_student(user_id=self.student.user_id, requesting_user_id=2)

    def test_admin_can_view_any_student(self):
        result = self.interactor.get_student(
            user_id=self.student.user_id, requesting_user_id=ADMIN_ID
        )
        self.assertEqual(result, self.student)

    def test_missing_student_raises_not_found_for_admin(self):
        with self.assertRaises(StudentNotFound):
            self.interactor.get_student(user_id=12345, requesting_user_id=ADMIN_ID)

    def test_permission_is_checked_before_existence(self):
        # A non-admin must not learn whether another user id exists.
        with self.assertRaises(NotAllowed):
            self.interactor.get_student(user_id=12345, requesting_user_id=2)


class CreateInstructorInteractorTests(unittest.TestCase):
    def setUp(self):
        self.instructors = FakeInstructorStorage()
        self.admins = FakeAdminStorage(admin_ids=[ADMIN_ID])
        self.interactor = CreateInstructorInteractor(
            instructor_storage=self.instructors, admin_storage=self.admins
        )

    def _create(self, requesting_user_id=ADMIN_ID, **overrides):
        data = dict(
            requesting_user_id=requesting_user_id,
            name="Ravi",
            email="ravi@example.com",
            password=PASSWORD,
            department="Physics",
        )
        data.update(overrides)
        return self.interactor.create_instructor(**data)

    def test_non_admin_is_forbidden(self):
        with self.assertRaises(NotAllowed):
            self._create(requesting_user_id=2)
        self.assertEqual(self.instructors.instructors, {})

    def test_admin_can_create(self):
        instructor = self._create()
        self.assertEqual(instructor.department, "Physics")

    def test_blank_department_becomes_none(self):
        self.assertIsNone(self._create(department="  ").department)

    def test_duplicate_email_is_rejected(self):
        self._create()
        with self.assertRaises(EmailAlreadyExists):
            self._create(name="Another", email="RAVI@example.com")

    def test_blank_name_is_rejected(self):
        with self.assertRaises(InvalidName):
            self._create(name=" ")


class GetInstructorInteractorTests(unittest.TestCase):
    def test_returns_instructor_or_raises(self):
        storage = FakeInstructorStorage()
        created = storage.create_instructor("Ravi", "ravi@example.com", PASSWORD, None)
        interactor = GetInstructorInteractor(storage=storage)
        self.assertEqual(interactor.get_instructor(user_id=created.user_id), created)
        with self.assertRaises(InstructorNotFound):
            interactor.get_instructor(user_id=1)


if __name__ == "__main__":
    unittest.main()
