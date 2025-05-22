from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rooms.views import RoomViewSet
from user_requests.views import RequestViewSet
from complaints.views import ComplaintViewSet
from chatbot.views import ChatbotView, chatbot_page
from .views import home  # <-- Add this import

router = DefaultRouter()
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'requests', RequestViewSet, basename='request')
router.register(r'complaints', ComplaintViewSet, basename='complaint')

urlpatterns = [
    path('', home, name='home'),
    path('chatbot/', chatbot_page, name='chatbot_page'),  # <-- Add this line
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/chatbot/', ChatbotView.as_view(), name='chatbot'),
]