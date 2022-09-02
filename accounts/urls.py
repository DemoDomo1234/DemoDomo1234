from django.urls import path 
from .views import Profile , SingupView , LoginView , LogoutView , UserList , Profile1 , folo , unfolo

app_name = "accounts"
urlpatterns = [
    path('LoginView',LoginView.as_view(), name='Login'),
    path('SingupView',SingupView.as_view(), name='Singup'),
    path('Profile<pk>',Profile.as_view(), name='Profile'),
    path('detail<pk>',Profile1.as_view(), name='Profile1'),
    path('user',UserList.as_view(), name='home'),
    path('logout', LogoutView , name='logout'),
    path('folo/<foloid>' , folo , name = 'folo'),
    path('unfolo/<foloid>' , unfolo , name = 'unfolo'),
] 