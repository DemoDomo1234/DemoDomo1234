from .models import Short
from django.shortcuts import redirect , get_object_or_404



class ShortMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        short = get_object_or_404(Short, id=pk)
        user = request.user
        if user.is_authenticated:
            if user == short.user:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('chat:VideoList')
        else:
            return redirect('accounts:Login')
