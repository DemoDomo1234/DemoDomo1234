from .models import Comments
from django.shortcuts import redirect , get_object_or_404


class CommentMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        user = request.user
        comment = get_object_or_404(Comments, id=pk)
        if user.is_authenticated:
            if user == comment.author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('chat:VideoList')
        else:
            return redirect('accounts:Login')
