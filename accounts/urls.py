from django.urls import path 
from . import views


app_name = "accounts"


urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='Login'),
    path('singup', views.SingupView.as_view(), name='Singup'),
    path('profile/<pk>' , views.ProfileView.as_view(), name='Profile'),
    path('edit-profile/<pk>' , views.EditProfileView.as_view(), name='EditProfile'),
    path('user-list', views.UserListView.as_view(), name='UserList'),
    path('logout', views.UserLogoutView.as_view(), name='Logout'),
    path('folow/<pk>', views.FolowView.as_view(), name='Folow'),
    path('noty/<pk>', views.NotyView.as_view(), name='Noty'),
    path('create-code/<pk>', views.CreateCodeView.as_view(), name='CreateCode'),
    path('check-code/<pk>', views.CheckCodeView.as_view(), name='CheckCode'),
    path('change-passowrd/<pk>', views.ChangePassowrdView.as_view(), name='ChangePassowrd'),
] 