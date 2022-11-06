from .models import Coments
from django.shortcuts import redirect , get_object_or_404

class ComentMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        user = request.user
        coment = get_object_or_404(Coments , id=pk)
        if user.is_authenticated:
            if user == coment.author :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')
