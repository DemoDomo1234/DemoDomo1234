from django.urls import path 
from . import views


app_name = 'post'


urlpatterns = [
    path('list', views.PostListView.as_view(), name='PostList'),
    path('create', views.PostCreateView.as_view(), name='PostCreate'),
    path('update/<pk>', views.PostUpdateView.as_view(), name='PostUpdate'),
    path('delete/<pk>', views.PostDeleteView.as_view(), name='PostDelete'),
    path('likes/<pk>', views.PostLikesView.as_view(), name='PostLikes'),
    path('un-likes/<pk>', views.PostUnLikesView.as_view(), name='PostUnLikes'),
    path('detail/<pk>', views.PostDetailView.as_view(), name='PostDetail'), 
    path('image-create/<pk>', views.ImageCreateView.as_view(), name='ImageCreate'),
    path('image-update/<pk>', views.ImageUpdateView.as_view(), name='ImageUpdate'),
    path('image-delete/<pk>', views.ImageDeleteView.as_view(), name='ImageDelete'),
] 
