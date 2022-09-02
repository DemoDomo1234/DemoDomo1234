from django.urls import path 
from .views import ( BlogCreate , BlogUpdate , BlogDelete ,
BlogList , BlogDetail , like1 , search , unlike1 , SavedList ,
saved , unsaved , unlike2 , like2  , TagCreate , TagUpdate ,
StoryCreate , StoryUpdate , story_like , story_unlike )

app_name = 'blog'
urlpatterns = [
    path('blog/create',BlogCreate.as_view(), name='BlogCreate'),
    path('blog/update<pk>',BlogUpdate.as_view(), name='BlogUpdate'),
    path('blog/delete<pk>',BlogDelete.as_view(), name='BlogDelete'),
    path('',BlogList.as_view(), name='BlogList'),
    path('blog/detail<pk>',BlogDetail.as_view() , name = 'BlogDetail'),
    path('like1/<postid>', like1, name='like1'),
    path('unlike1/<postid>', unlike1, name='unlike1'),
    path('search', search , name='search'),
    path('like2/<postid>', like2, name='like2'),
    path('unlike2/<postid>', unlike2, name='unlike2'),
    path('saved/<postid>', saved, name='saved'),
    path('unsaved/<postid>', unsaved, name='unsave'),
    path('blog/saved', SavedList.as_view() , name='savedlist'),
    path('blog/createtag',TagCreate.as_view(), name='TagCreate'),
    path('blog/updatetag<pk>',TagUpdate.as_view(), name='TagUpdate'),
    path('blog/story', SavedList.as_view() , name='storylist'),
    path('blog/createstory',TagCreate.as_view(), name='StoryCreate'),
    path('blog/updatestory<pk>',TagUpdate.as_view(), name='StoryUpdate'),
    path('likestory/<postid>', story_like , name='likestory'),
    path('unlikestory/<postid>', story_unlike , name='unlikestory'),
    #path('delete/<pk>' , StoryDelet.as_view() , name = 'deletestory'),
] 

