from django.test import TestCase
from .chatbot import get_chatbot_response

class ChatbotTests(TestCase):
    def test_chatbot_response(self):
        # Test for a known query
        response = get_chatbot_response("What are the room availability details?")
        self.assertIn("available", response.lower())

    def test_chatbot_unknown_query(self):
        # Test for an unknown query
        response = get_chatbot_response("Unknown question?")
        self.assertEqual(response, "I'm sorry, I didn't understand that.")

    def test_chatbot_greeting(self):
        # Test for a greeting
        response = get_chatbot_response("Hello")
        self.assertIn("hello", response.lower())  # Check if the response contains a greeting

    def test_chatbot_farewell(self):
        # Test for a farewell
        response = get_chatbot_response("Goodbye")
        self.assertIn("goodbye", response.lower())  # Check if the response contains a farewell message