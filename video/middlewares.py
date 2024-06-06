from .models import Video

class VideoViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        id = request.path[-1]
        user = request.user
        try:
            video = Video.objects.get(id=id)
            if user not in video.views.all():
                video.views.add(user)
        except:
            pass
        return response