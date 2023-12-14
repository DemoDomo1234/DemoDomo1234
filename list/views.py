from django.shortcuts import (render , redirect)
from django.views.generic import (ListView, CreateView, UpdateView,
								  DeleteView)
from .models import List, PlayList
from django.urls import reverse_lazy
from django.views import View
from taggit.models import Tag 
from .mixins import ListMixin, PlayListMixin
from accounts.mixins import LoginRequiredMixin
from video.models import Video



class ListCreateView(LoginRequiredMixin, CreateView):
	model = List
	fields = ('body', 'title')
	template_name = "list/ListCreate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['title'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form  

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class ListUpdateView(ListMixin, UpdateView):
	model = List
	fields = ('body', 'title')
	template_name = "list/ListUpdate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['title'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form 


class ListDeleteView(ListMixin, DeleteView):
    model = List
    template_name = 'list/ListDelete.html'
    success_url = reverse_lazy('chat:VideoList')


class PlayListCreateView(LoginRequiredMixin, CreateView):
	model = PlayList
	fields = ('body', 'title')
	template_name = "play_list/PlayListCreate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['title'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form 

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class PlayListUpdateView(PlayListMixin, UpdateView):
	model = PlayList
	fields = ('body', 'title')
	template_name = "play_list/PlayListUpdate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['title'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form 


class PlayListDeleteView(PlayListMixin, DeleteView):
    model = PlayList
    template_name = 'play_list/PlayListDelete.html'
    success_url = reverse_lazy('chat:VideoList')


class AddToListView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		if user.is_authenticated:
			lists = List.objects.filter(user=request.user)
			if request.method == 'POST':
				ids=request.POST.getlist('myid')
				video = Video.objects.get(id=pk)
				for myid in ids:
					my_list = List.objects.get(id=myid)
					if my_list not in video.lists.all():
						video.lists.add(my_list)
					else:
						video.lists.remove(my_list)
				return redirect('chat:VideoList')
			else :
				return render(request, 'list/AddToList.html', {'post':lists})
		else:
			return redirect('accounts:Login')


class AddToPlayListView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		if user.is_authenticated:
			playlists = PlayList.objects.filter(user=request.user)
			video = Video.objects.get(id=pk)
			if user == video.author:
				if request.method == 'POST':
					if request.user == video.author:
						ids=request.POST.getlist('id')
						for myid in ids:
							play_list = PlayList.objects.get(id=myid)
							if play_list not in video.playlists.all():
								video.playlists.add(play_list)
							else:
								video.playlists.remove(play_list)
						return redirect('chat:VideoList')
					else:
						return redirect('chat:VideoList')
				else :
					return render(request, 'play_list/AddToPlayList.html', {'post':playlists})
			else:
				return redirect('chat:VideoList')
		else:
			return redirect('accounts:Login')


class PlayListView(ListView):
	model = Video
	context_object_name = 'post'
	template_name = 'play_list/PlayList.html'

	def get_queryset(self):
		my_play_list = PlayList.objects.get(id=self.kwargs['pk'])
		return my_play_list.play_list.all()


class ListView(ListMixin, ListView):
	model = Video
	context_object_name = 'post'
	template_name = 'list/List.html'

	def get_queryset(self):
		my_list = List.objects.get(id=self.kwargs['pk'])
		return Video.objects.filter(lists=my_list)


class TagListView(ListView):
	model = Video
	context_object_name = 'post'
	template_name = 'video/TagList.html'

	def get_queryset(self):
		tag = Tag.objects.get(id=self.kwargs['pk'])
		return Video.objects.filter(tag=tag)

