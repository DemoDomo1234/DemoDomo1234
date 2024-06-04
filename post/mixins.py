from .models import Post, Image
from django.shortcuts import redirect , get_object_or_404



class PostMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        user = request.user
        if user.is_authenticated:
            if user == post.user:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('video:VideoList')
        else:
            return redirect('accounts:Login')


class ImageMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        image = get_object_or_404(Image, id=pk)
        user = request.user
        if user.is_authenticated:
            if user == image.user:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('video:VideoList')
        else:
            return redirect('accounts:Login')
