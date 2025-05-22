# Hostel_Management_With_Chatbot


# Hostel Management System

## Overview
The Hostel Management System is a Django-based web application designed to streamline hostel operations for students and administrators. It provides real-time room availability, online request and complaint management, and features an interactive AI-powered chatbot for student queries.

The chatbot leverages the **Gemini API** for intelligent, context-aware responses, making the system more helpful and engaging for users.
**Users can switch between light and dark mode** for a personalized experience.

## Technologies Used
- **Backend:** Django (Python)
- **Database:** MySQL
- **AI Integration:** Gemini API (for chatbot responses)
- **Frontend:** Django Templates (Bootstrap for styling)

## Features
- **Room Availability Check:** Instantly view available rooms.
- **Online Request Submission:** Submit and track service requests online.
- **Complaint Management:** File and manage complaints with ease.
- **Light/Dark Mode:** Users can toggle between light and dark themes on all main pages.
- **AI Chatbot:** Ask questions and get instant answers via the chatbot, powered by Gemini API.
- **Admin Panel:** Manage all data and users through Django’s built-in admin interface.

## Project Structure
```
hostel-management-system
└── backend
    ├── hostel_management
    ├── rooms
    ├── user_requests
    ├── complaints
    ├── chatbot
    ├── manage.py
    ├── requirements.txt
    └── templates
        ├── home.html
        └── chatbot.html
└── README.md
```

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd hostel-management-system/backend
```

### 2. Install Dependencies
- Make sure you are in the `backend` directory.
- Create a file named `requirements.txt` with the following content:
  ```
  Django==4.1.3
  djangorestframework==3.14.0
  mysqlclient==2.1.0
  django-cors-headers==3.13.0
  python-dotenv==0.21.0
  tensorflow==2.10.0
  nltk==3.7
  ```
- Then install all dependencies with:

```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables

- **You must generate a Gemini API key** from [Google AI Studio](https://aistudio.google.com/app/apikey) or your Google Cloud Console.
- Create a file named `api.env` in the `backend` directory.
- Add your Gemini API key:
  ```
  GEMINI_API_KEY=your_gemini_api_key_here
  ```
- **Note:** The chatbot uses the **Gemini 2.0 Flash** model for fast, high-quality responses.
- The chatbot will use this key to access the Gemini API for generating responses.

### 4. Apply Migrations and Create Superuser
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Django Server
```sh
python manage.py runserver
```

## Accessing the Application

- **Dashboard Home:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Rooms API:** [http://127.0.0.1:8000/api/rooms/](http://127.0.0.1:8000/api/rooms/)
- **Complaints API:** [http://127.0.0.1:8000/api/complaints/](http://127.0.0.1:8000/api/complaints/)
- **Requests API:** [http://127.0.0.1:8000/api/requests/](http://127.0.0.1:8000/api/requests/)
- **Chatbot Web Interface:** [http://127.0.0.0:8000/chatbot/](http://127.0.0.1:8000/chatbot/)
- **Chatbot API (POST only):** [http://127.0.0.1:8000/api/chatbot/](http://127.0.0.1:8000/api/chatbot/)

## How the Chatbot Works

- The chatbot interface is available at `/chatbot/`.
- When a user submits a question, the backend sends the message to the Gemini API using the provided API key.
- The Gemini API returns a context-aware response, which is displayed in the chat window.
- All communication with the Gemini API is handled securely on the backend.

## Theming

- Both the dashboard and chatbot pages support **light and dark mode**.
- Users can toggle the theme using the "Switch to Light/Dark Mode" button in the navbar.


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.

---

**Interactive Demo:**  
Try asking the chatbot about hostel facilities, room availability, or any general student query to see the Gemini-powered responses in action!
