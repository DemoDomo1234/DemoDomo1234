from django.urls import path 
from .views import (ComentCreateView, ComentUpdateView, ComentDeleteView, 
                    ComentLikesView, ComentUnLikesView
                    )


app_name = 'coments'


urlpatterns = [
    path('create/<pk>',ComentCreateView.as_view(), name='ComentCreate'),
    path('update<pk>',ComentUpdateView.as_view(), name='ComentUpdate'),
    path('delete<pk>',ComentDeleteView.as_view(), name='ComentDelete'),
    path('likes<pk>',ComentLikesView.as_view() , name = 'ComentLikes'),
    path('unlikes<pk>',ComentUnLikesView.as_view() , name = 'ComentUnLikes'),
] 