from .models import (Blog, Story, Short, Post, List, PlayList, Image)
from django.shortcuts import redirect , get_object_or_404

class BlogMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        blog = get_object_or_404(Blog , id=pk)
        user = request.user
        if user.is_authenticated:
            if user == blog.author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')

class StoryMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        story = get_object_or_404(Story , id=pk)
        user = request.user
        if user.is_authenticated:
            if user == story.user :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')
            
class ShortMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        short = get_object_or_404(Short , id=pk)
        user = request.user
        if user.is_authenticated:
            if user == short.user :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')

class PostMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post , id=pk)
        user = request.user
        if user.is_authenticated:
            if user == post.user :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')

class ListMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        lists = get_object_or_404(List , id=pk)
        user = request.user
        if user.is_authenticated:
            if user == lists.user :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')

class PlayListMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        playlist = get_object_or_404(PlayList , id=pk)
        user = request.user
        if user.is_authenticated:
            if user == playlist.user :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')

class ImageMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        image = get_object_or_404(Image , id=pk)
        user = request.user
        if user.is_authenticated:
            if user == image.user :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')
