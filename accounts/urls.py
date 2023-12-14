from django.urls import path 
from . import views


app_name = "accounts"


urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='Login'),
    path('sing-up', views.SingUpView.as_view(), name='Sing_up'),
    path('profile/<pk>', views.ProfileView.as_view(), name='Profile'),
    path('edit-profile/<pk>', views.EditProfileView.as_view(), name='EditProfile'),
    path('user-video-list', views.UserVideoListView.as_view(), name='UserVideoList'),
    path('logout', views.UserLogoutView.as_view(), name='Logout'),
    path('follow/<pk>', views.FollowView.as_view(), name='Follow'),
    path('notification/<pk>', views.NotificationView.as_view(), name='Notification'),
    path('create-code/<pk>', views.CreateCodeView.as_view(), name='CreateCode'),
    path('check-code/<pk>', views.CheckCodeView.as_view(), name='CheckCode'),
    path('change-password/<pk>', views.ChangePasswordView.as_view(), name='ChangePassword'),
] 