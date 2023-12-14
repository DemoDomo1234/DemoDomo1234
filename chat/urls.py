from django.urls import path
from chat import views
from video.views import VideoListView

app_name = "chat"


urlpatterns = [
    path('chat-view', views.ChatView.as_view(), name="Chat"),
    path('', VideoListView.as_view(), name="VideoList"),
]