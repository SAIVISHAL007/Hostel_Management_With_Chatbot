from django.test import TestCase
from .models import Complaint

class ComplaintModelTest(TestCase):

    def setUp(self):
        self.complaint = Complaint.objects.create(
            student_name="John Doe",
            room_number="101",
            complaint_text="The air conditioning is not working."
        )

    def test_complaint_creation(self):
        self.assertEqual(self.complaint.student_name, "John Doe")
        self.assertEqual(self.complaint.room_number, "101")
        self.assertEqual(self.complaint.complaint_text, "The air conditioning is not working.")

    def test_complaint_str(self):
        self.assertEqual(str(self.complaint), "Complaint from John Doe in room 101")