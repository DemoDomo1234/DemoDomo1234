from .models import Story
from django.shortcuts import redirect , get_object_or_404



class StoryMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        story = get_object_or_404(Story, id=pk)
        user = request.user
        if user.is_authenticated:
            if user == story.user:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('video:VideoList')
        else:
            return redirect('accounts:Login')
    