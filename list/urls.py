from django.urls import path 
from . import views
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


app_name = 'list'

urlpatterns = [
  
    path('blog/tag-list/<pk>', cache_page(CACHE_TTL)(views.TagListView.as_view()), name='TagList'),
    path('create', views.ListCreateView.as_view(), name='ListCreate'),
    path('update/<pk>', views.ListUpdateView.as_view(), name='ListUpdate'),
    path('delete/<pk>', views.ListDeleteView.as_view(), name='ListDelete'),
    path('play-Lit-create', views.PlayListCreateView.as_view(), name='ListCreate'),
    path('play-list-update/<pk>', views.PlayListUpdateView.as_view(), name='PlayListUpdate'),
    path('my-list/<pk>', cache_page(CACHE_TTL)(views.MyListView.as_view()), name='MyList'),
    path('play-list-delete/<pk>', views.PlayListDeleteView.as_view(), name='PlayListDelete'),
    path('add-to-list/<pk>', views.AddToListView.as_view(), name='AddToList'),
    path('add-to-play-list/<pk>', views.AddToPlayListView.as_view(), name='AddToPlayList'),
    path('my-play-list/<pk>', cache_page(CACHE_TTL)(views.MyPlayListView.as_view()), name='MyPlayList'),
] 
