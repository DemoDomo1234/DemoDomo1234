from .models import Blog
from story.models import Story
from short.models import Short
from post.models import Post


class BlogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, pk):
        blog = Blog.objects.get(id=pk)
        user = request.user
        if user in blog.views.all:
            blog.views.remove(user)
        else:
            blog.views.add(user)
        response = self.get_response(request)
        return response


class StoryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, pk):
        story = Story.objects.get(id=pk)
        user = request.user
        if user in story.views.all:
            story.views.remove(user)
        else:
            story.views.add(user)
        response = self.get_response(request)
        return response


class ShortMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request, pk):
        short = Short.objects.get(id=pk)
        user = request.user
        if user in short.views.all:
            short.views.remove(user)
        else:
            short.views.add(user)
        response = self.get_response(request)
        return response


class PostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, pk):
        post = Post.objects.get(id=pk)
        user = request.user
        if user in post.views.all:
            post.views.remove(user)
        else:
            post.views.add(user)
        response = self.get_response(request)
        return response