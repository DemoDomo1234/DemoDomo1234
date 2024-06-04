from .models import Video
from django.shortcuts import redirect , get_object_or_404


class VideoMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        video = get_object_or_404(Video, id=pk)
        user = request.user
        if user.is_authenticated:
            if user == video.author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('video:VideoList')
        else:
            return redirect('accounts:Login')
