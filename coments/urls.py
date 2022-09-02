from django.urls import path 
from .views import BlogCreate , BlogUpdate , BlogDelete , BlogList  , like1 , unlike1 , like2 , unlike2 ,   StoryCreate , StoryUpdate , StoryDelete , StoryList  , like21 , unlike21 , like22 , unlike22  

app_name = 'coments'
urlpatterns = [
    path('create',BlogCreate.as_view(), name='BlogCreate'),
    path('update<pk>',BlogUpdate.as_view(), name='BlogUpdate'),
    path('delete<pk>',BlogDelete.as_view(), name='BlogDelete'),
    path('list',BlogList.as_view(), name='BlogList'),
    path('like1/<blogid>' , like1 , name = 'like1'),
    path('unlike1/<blogid>' , unlike1 , name = 'unlike1'),
    path('like2/<blogid>' , like2 , name = 'like2'),
    path('unlike2/<blogid>' , unlike2 , name = 'unlike2'),
    path('createstory',StoryCreate.as_view(), name='StoryCreate'),
    path('updatestory<pk>',StoryUpdate.as_view(), name='StoryUpdate'),
    path('deletestory<pk>',StoryDelete.as_view(), name='StoryDelete'),
    path('liststory',StoryList.as_view(), name='storylist'),
    path('like21/<blogid>' , like21 , name = 'like21'),
    path('unlike21/<blogid>' , unlike21 , name = 'unlike21'),
    path('like22/<blogid>' , like22 , name = 'like22'),
    path('unlike22/<blogid>' , unlike22 , name = 'unlike22'),
] 