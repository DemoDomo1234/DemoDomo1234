from django.urls import path 
from . import views


app_name = 'list'


urlpatterns = [
    path('blog/tag-list/<pk>', views.TagListView.as_view(), name='TagList'),
    path('create', views.ListCreateView.as_view(), name='ListCreate'),
    path('update/<pk>', views.ListUpdateView.as_view(), name='ListUpdate'),
    path('delete/<pk>', views.ListDeleteView.as_view(), name='ListDelete'),
    path('play-Lit-create', views.PlayListCreateView.as_view(), name='PlayListCreate'),
    path('play-list-update/<pk>', views.PlayListUpdateView.as_view(), name='PlayListUpdate'),
    path('my-list/<pk>', views.ListView.as_view(), name='List'),
    path('play-list-delete/<pk>', views.PlayListDeleteView.as_view(), name='PlayListDelete'),
    path('add-to-list/<pk>', views.AddToListView.as_view(), name='AddToList'),
    path('add-to-play-list/<pk>', views.AddToPlayListView.as_view(), name='AddToPlayList'),
    path('my-play-list/<pk>', views.PlayListView.as_view(), name='PlayList'),
] 
