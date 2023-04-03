from .models import Blog
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
