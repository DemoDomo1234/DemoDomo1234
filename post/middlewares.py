from .models import Post

class PostViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        id = request.path[-1]
        user = request.user
        try:
            post = Post.objects.get(id=id)
            if user not in post.views.all():
                post.views.add(user)
        except:
            pass
        return response