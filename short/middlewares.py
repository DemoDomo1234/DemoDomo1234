from .models import Short

class ShortViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        id = request.path[-1]
        user = request.user
        try:
            short = Short.objects.get(id=id)
            if user not in short.views.all():
                short.views.add(user)
        except:
            pass
        return response