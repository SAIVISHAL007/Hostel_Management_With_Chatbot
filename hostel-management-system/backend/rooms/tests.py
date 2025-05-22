from django.test import TestCase
from .models import Room

class RoomModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Room.objects.create(room_number="101", capacity=2, is_available=True)
        Room.objects.create(room_number="102", capacity=3, is_available=False)

    def test_room_creation(self):
        room = Room.objects.get(room_number="101")
        self.assertEqual(room.capacity, 2)
        self.assertTrue(room.is_available)

    def test_room_availability(self):
        available_room = Room.objects.filter(is_available=True).count()
        self.assertEqual(available_room, 1)

    def test_room_capacity(self):
        room = Room.objects.get(room_number="102")
        self.assertEqual(room.capacity, 3)
        self.assertFalse(room.is_available)