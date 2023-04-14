from .models import User
from django.shortcuts import redirect , get_object_or_404


class UserMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        user = request.user
        myuser = get_object_or_404(User , id=pk)
        if user.is_authenticated:
            if user.id == myuser.id :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')


class MyLoginRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('accounts:Login')