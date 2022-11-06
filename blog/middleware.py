from .models import (Blog, Story, Short, Post)

class BlogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request, pk):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        blog = Blog.objects.get(id=pk)
        user = request.user
        if user in blog.views.all:
            blog.views.remove(user)
        else:
            blog.views.add(user)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

class StoryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request, pk):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        story = Story.objects.get(id=pk)
        user = request.user
        if user in story.views.all:
            story.views.remove(user)
        else:
            story.views.add(user)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

class ShortMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request, pk):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        Short = short.objects.get(id=pk)
        user = request.user
        if user in short.views.all:
            short.views.remove(user)
        else:
            short.views.add(user)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

class PostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request, pk):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        post = Post.objects.get(id=pk)
        user = request.user
        if user in post.views.all:
            post.views.remove(user)
        else:
            post.views.add(user)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response