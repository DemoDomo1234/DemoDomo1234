from .models import User
from django.shortcuts import redirect , get_object_or_404


class UserMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        request_user = request.user
        user = get_object_or_404(User , id=pk)
        if request_user.is_authenticated:
            if request_user.id == user.id :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('video:VideoList')
        else:
            return redirect('accounts:Login')


class LoginRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('accounts:Login')