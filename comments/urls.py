from django.urls import path 
from .views import (CommentCreateView, CommentUpdateView, CommentDeleteView, 
                    CommentLikesView, CommentUnLikesView, ReplyCommentView,
                    ReplyToReplyCommentView
                    )


app_name = 'comments'


urlpatterns = [
    path('create/<pk>/<obj>',CommentCreateView.as_view(), name='CommentCreate'),
    path('update/<pk>',CommentUpdateView.as_view(), name='CommentUpdate'),
    path('delete/<pk>',CommentDeleteView.as_view(), name='CommentDelete'),
    path('likes/<pk>',CommentLikesView.as_view(), name='CommentLikes'),
    path('un-likes/<pk>',CommentUnLikesView.as_view(), name='CommentUnLikes'),
    path('reply/<pk>',ReplyCommentView.as_view(), name='ReplyComment'),
    path('reply-to-reply/<pk>',ReplyToReplyCommentView.as_view(), name='ReplyToReplyComment'),
] 