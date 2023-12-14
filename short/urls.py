from django.urls import path 
from . import views


app_name = 'short'


urlpatterns = [
    path('list', views.ShortListView.as_view(), name='ShortList'),
    path('create', views.ShortCreateView.as_view(), name='ShortCreate'),
    path('update/<pk>', views.ShortUpdateView.as_view(), name='ShortUpdate'),
    path('delete/<pk>', views.ShortDeleteView.as_view(), name='ShortDelete'),
    path('detail/<pk>', views.ShortDetailView.as_view(), name='ShortDetail'),
    path('likes/<pk>', views.ShortLikesView.as_view(), name='ShortLikes'),
    path('un-likes/<pk>', views.ShortUnLikesView.as_view(), name='ShortUnLikes'),
] 
