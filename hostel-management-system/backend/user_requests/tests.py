from django.test import TestCase
from .models import Request

class RequestModelTest(TestCase):
    def setUp(self):
        self.request = Request.objects.create(
            student_name="John Doe",
            room_number="101",
            request_type="Room Change",
            description="Requesting a room change due to personal reasons."
        )

    def test_request_creation(self):
        self.assertEqual(self.request.student_name, "John Doe")
        self.assertEqual(self.request.room_number, "101")
        self.assertEqual(self.request.request_type, "Room Change")
        self.assertEqual(self.request.description, "Requesting a room change due to personal reasons.")

    def test_string_representation(self):
        self.assertEqual(str(self.request), "Request by John Doe for Room 101")