from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('coments/', include('coments.urls')),
    path('accounts/', include('accounts.urls')),
    path('list', include('list.urls')),
    path('post', include('post.urls')),
    path('short', include('short.urls')),
    path('story', include('story.urls')),
    path('reset_password', auth_view.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_send', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
