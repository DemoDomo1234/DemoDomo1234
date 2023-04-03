from django.urls import path 
from . import views
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


app_name = 'short'

urlpatterns = [
   
    path('list', cache_page(CACHE_TTL)(views.ShortListView.as_view()), name='ShortList'),
    path('create', views.ShortCreateView.as_view(), name='ShortCreate'),
    path('update/<pk>', views.ShortUpdateView.as_view(), name='ShortUpdate'),
    path('delete/<pk>', views.ShortDeleteView.as_view(), name='ShortDelete'),
    path('detail/<pk>', views.ShortDetailView.as_view(), name='ShortDetail'),
    path('likes/<pk>', views.ShortLikesView.as_view(), name='ShortLikes'),
    path('unlikes/<pk>', views.ShortUnLikesView.as_view(), name='ShortUnLikes'),
] 
