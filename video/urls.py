from django.urls import path 
from . import views
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


app_name = 'video'


urlpatterns = [
    path('', views.VideoListView.as_view(), name="VideoList"),
    path('create', views.VideoCreateView.as_view(), name='VideoCreate'),
    path('update/<pk>', views.VideoUpdateView.as_view(), name='VideoUpdate'),
    path('delete/<pk>', views.VideoDeleteView.as_view(), name='VideoDelete'),
    path('detail/<pk>', views.VideoDetailView.as_view(), name='VideoDetail'),
    path('likes/<pk>', views.VideoLikesView.as_view(), name='VideoLikes'),
    path('saved/<pk>', views.VideoSavedView.as_view(), name='VideoSaved'),
    path('un-likes/<pk>', views.VideoUnLikesView.as_view(), name='VideoUnLikes'),
    path('saved', views.SavedListView.as_view(), name='SavedList'),
] 
