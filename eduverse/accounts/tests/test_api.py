from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accountz.models import Admin

PASSWORD = "S3cure-pass-123"


class AccountsAPITests(APITestCase):

    def _make_admin(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="root@example.com", email="root@example.com", password=PASSWORD
        )
        Admin.objects.create(user=user, name="Root", email="root@example.com")
        return user

    def _register_student(self, email="stu@example.com", name="Stu"):
        return self.client.post(
            reverse("accounts:student-create"),
            {"name": name, "email": email, "password": PASSWORD},
            format="json",
        )

    # ---- registration & login ----
    def test_register_student(self):
        response = self._register_student()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], "stu@example.com")
        self.assertNotIn("password", response.data)

    def test_register_with_duplicate_email_returns_409(self):
        self._register_student()
        response = self._register_student()
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_register_with_bad_input_returns_400(self):
        response = self.client.post(
            reverse("accounts:student-create"),
            {"name": "", "email": "not-an-email", "password": "x"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_returns_token(self):
        self._register_student()
        response = self.client.post(
            reverse("accounts:login"),
            {"username": "stu@example.com", "password": PASSWORD},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    # ---- student detail ----
    def test_student_detail_requires_authentication(self):
        response = self.client.get(reverse("accounts:student-detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_student_can_view_self_but_not_others(self):
        me = self._register_student("me@example.com", "Me").data["user_id"]
        other = self._register_student("other@example.com", "Other").data["user_id"]
        user = get_user_model().objects.get(id=me)
        self.client.force_authenticate(user=user)

        self.assertEqual(
            self.client.get(reverse("accounts:student-detail", args=[me])).status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            self.client.get(reverse("accounts:student-detail", args=[other])).status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_admin_can_view_any_student_and_gets_404_for_missing(self):
        student_id = self._register_student().data["user_id"]
        self.client.force_authenticate(user=self._make_admin())

        ok = self.client.get(reverse("accounts:student-detail", args=[student_id]))
        self.assertEqual(ok.status_code, status.HTTP_200_OK)
        missing = self.client.get(reverse("accounts:student-detail", args=[99999]))
        self.assertEqual(missing.status_code, status.HTTP_404_NOT_FOUND)

    # ---- instructors ----
    def _instructor_payload(self, email="ravi@example.com"):
        return {
            "name": "Ravi",
            "email": email,
            "password": PASSWORD,
            "department": "Physics",
        }

    def test_non_admin_cannot_create_instructor(self):
        student_id = self._register_student().data["user_id"]
        self.client.force_authenticate(user=get_user_model().objects.get(id=student_id))
        response = self.client.post(
            reverse("accounts:instructor-create"), self._instructor_payload(), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_creates_and_anyone_authenticated_can_view_instructor(self):
        admin = self._make_admin()
        self.client.force_authenticate(user=admin)
        created = self.client.post(
            reverse("accounts:instructor-create"), self._instructor_payload(), format="json"
        )
        self.assertEqual(created.status_code, status.HTTP_201_CREATED)
        self.assertEqual(created.data["department"], "Physics")

        student_id = self._register_student().data["user_id"]
        self.client.force_authenticate(user=get_user_model().objects.get(id=student_id))
        detail = self.client.get(
            reverse("accounts:instructor-detail", args=[created.data["user_id"]])
        )
        self.assertEqual(detail.status_code, status.HTTP_200_OK)

    def test_unknown_instructor_returns_404(self):
        self.client.force_authenticate(user=self._make_admin())
        response = self.client.get(reverse("accounts:instructor-detail", args=[99999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
