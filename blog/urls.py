from django.urls import path 
from . import views
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


app_name = 'blog'

urlpatterns = [
    path('', cache_page(CACHE_TTL)(views.BlogListView.as_view()), name='BlogList'),
    path('blog/create', views.BlogCreateView.as_view(), name='BlogCreate'),
    path('blog/update/<pk>', views.BlogUpdateView.as_view(), name='BlogUpdate'),
    path('blog/delete/<pk>', views.BlogDeleteView.as_view(), name='BlogDelete'),
    path('blog/detail/<pk>', views.BlogDetailView.as_view(), name='BlogDetail'),
    path('blog/likes/<pk>', views.BlogLikesView.as_view(), name='BlogLikes'),
    path('blog/saved/<pk>', views.BlogSavedView.as_view(), name='BlogSaved'),
    path('blog/unlikes/<pk>', views.BlogUnLikesView.as_view(), name='BlogUnLikes'),
    path('blog/saved', cache_page(CACHE_TTL)(views.SavedListView.as_view()), name='savedlist'),
] 
