from django.urls import path 
from . import views
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


app_name = 'story'

urlpatterns = [
    path('list', cache_page(CACHE_TTL)(views.StoryListView.as_view()), name='StoryList'),
    path('create', views.StoryCreateView.as_view(), name='StoryCreate'),
    path('update/<pk>', views.StoryUpdateView.as_view(), name='StoryUpdate'),
    path('delete/<pk>', views.StoryDeleteView.as_view(), name='StoryDelete'),
    path('detail/<pk>', views.StoryDetailView.as_view(), name='StoryDetail'),
    path('likes/<pk>', views.StoryLikesView.as_view(), name='StoryLikes'),

] 
