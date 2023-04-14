from django.urls import path 
from . import views


app_name = 'story'


urlpatterns = [
    path('list', views.StoryListView.as_view(), name='StoryList'),
    path('create', views.StoryCreateView.as_view(), name='StoryCreate'),
    path('update/<pk>', views.StoryUpdateView.as_view(), name='StoryUpdate'),
    path('delete/<pk>', views.StoryDeleteView.as_view(), name='StoryDelete'),
    path('detail/<pk>', views.StoryDetailView.as_view(), name='StoryDetail'),
    path('likes/<pk>', views.StoryLikesView.as_view(), name='StoryLikes'),
] 
