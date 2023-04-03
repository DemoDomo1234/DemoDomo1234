from .models import List, PlayList
from django.shortcuts import redirect , get_object_or_404



class ListMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        lists = get_object_or_404(List , id=pk)
        user = request.user
        if user.is_authenticated:
            if user == lists.user :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')


class PlayListMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        playlist = get_object_or_404(PlayList , id=pk)
        user = request.user
        if user.is_authenticated:
            if user == playlist.user :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('blog:BlogList')
        else:
            return redirect('accounts:Login')
