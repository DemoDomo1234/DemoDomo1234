from django.urls import path 
from . import views
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


app_name = 'post'

urlpatterns = [
    path('list', cache_page(CACHE_TTL)(views.PostListView.as_view()), name='PostList'),
    path('create', views.PostCreateView.as_view(), name='PostCreate'),
    path('update/<pk>', views.PostUpdateView.as_view(), name='PostUpdate'),
    path('delete/<pk>', views.PostDeleteView.as_view(), name='PostDelete'),
    path('likes/<pk>', views.PostLikesView.as_view(), name='PostLikes'),
    path('unlikes/<pk>', views.PostUnLikesView.as_view(), name='PostUnLikes'),
    path('detail/<pk>', views.PostDetailView.as_view(), name='PostDetail'), 
    path('image-create/<pk>', views.ImageCreateView.as_view(), name='ImageCreate'),
    path('image-update/<pk>', views.ImageUpdateView.as_view(), name='ImageUpdate'),
    path('image-delete/<pk>', views.ImageDeleteView.as_view(), name='ImageDelete'),

] 
