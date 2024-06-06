from .models import Story

class StoryViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        id = request.path[-1]
        user = request.user
        try:
            story = Story.objects.get(id=id)
            if user not in story.views.all():
                story.views.add(user)
        except:
            pass
        return response