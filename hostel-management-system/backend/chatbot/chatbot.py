import google.generativeai as genai
import os
from django.core.mail import send_mail

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
OWNER_EMAIL = "owner@hostel.edu"  # Change to the real owner/warden email

def get_chatbot_response(message):
    if not message:
        return "Please enter a message."
    msg = message.lower()

    # Escalate if a serious issue is detected
    serious_keywords = ["fire", "medical", "fight", "theft", "emergency", "urgent", "danger", "accident"]
    if any(word in msg for word in serious_keywords):
        # Send email to owner/warden
        send_mail(
            subject="URGENT Hostel Issue Reported",
            message=f"A serious issue was reported: {message}",
            from_email="noreply@hostel.edu",
            recipient_list=[OWNER_EMAIL],
            fail_silently=True,
        )
        return "This seems to be a serious issue. The hostel warden has been notified and will contact you soon."

    # Hostel-themed simple responses
    if os.environ.get("USE_SIMPLE_CHATBOT") == "1":
        if "hello" in msg or "hi" in msg:
            return "Hello! Welcome to the Hostel Management System. How can I assist you today?"
        if "room" in msg and "available" in msg:
            return "You can check room availability or request a room assignment. Would you like to proceed?"
        if "complaint" in msg:
            return "To submit a complaint, please use the complaint form or let me know your issue."
        if "request" in msg:
            return "You can submit a room or facility request using the request form."
        if "mess menu" in msg or "food" in msg:
            return "The mess menu is available on the notice board and the student portal."
        if "warden" in msg:
            return "You can contact the warden at warden@hostel.edu or visit the warden's office during office hours."
        if "goodbye" in msg or "bye" in msg:
            return "Goodbye! If you need further assistance, just ask."
        return "I'm here to help with hostel rooms, complaints, requests, and general queries. Please ask your question."

    # Otherwise, use Gemini
    if not GEMINI_API_KEY:
        return "Gemini API key is not set."
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(message)
        return response.text.strip()
    except Exception as e:
        return f"Error contacting Gemini API: {str(e)}"