from django.shortcuts import (render , redirect)
from django.views.generic import (ListView, CreateView, UpdateView,
								  DeleteView)
from .models import List, PlayList
from django.urls import reverse_lazy
from django.views import View
from taggit.models import Tag 
from .mixins import ListMixin, PlayListMixin
from accounts.mixins import MyLoginRequiredMixin
from blog.models import Blog



class ListCreateView(MyLoginRequiredMixin, CreateView):
	model = List
	fields = ('body', 'titel')
	template_name = "list/ListCreate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['titel'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form  

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class ListUpdateView(ListMixin, UpdateView):
	model = List
	fields = ('body', 'titel')
	template_name = "list/ListUpdate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['titel'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form 


class ListDeleteView(ListMixin, DeleteView):
    model = List
    template_name = 'list/ListDelete.html'
    success_url = reverse_lazy('blog:BlogList')


class PlayListCreateView(MyLoginRequiredMixin, CreateView):
	model = PlayList
	fields = ('body', 'titel')
	template_name = "playlst/PlayLitCreate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['titel'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form 

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class PlayListUpdateView(PlayListMixin, UpdateView):
	model = PlayList
	fields = ('body', 'titel')
	template_name = "playlst/PlayListUpdate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['titel'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form 


class PlayListDeleteView(PlayListMixin, DeleteView):
    model = PlayList
    template_name = 'playlst/PlayListDelete.html'
    success_url = reverse_lazy('blog:BlogList')


class AddToListView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		if user.is_authenticated:
			lists = List.objects.filter(user=request.user)
			if request.method == 'POST' :
				ids=request.POST.getlist('myid')
				blog = Blog.objects.get(id=pk)
				for myid in ids:
					mylist = List.objects.get(id=myid)
					if mylist not in blog.lists.all():
						blog.lists.add(mylist)
					else:
						blog.lists.remove(mylist)
				return redirect('blog:BlogList')
			else :
				return render(request, 'list/AddToList.html' , {'post':lists})
		else:
			return redirect('accounts:Login')


class AddToPlayListView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		if user.is_authenticated:
			playlists = PlayList.objects.filter(user=request.user)
			blog = Blog.objects.get(id=pk)
			if user == blog.author :
				if request.method == 'POST' :
					if request.user == blog.author:
						ids=request.POST.getlist('myid')
						for myid in ids:
							myplaylist = PlayList.objects.get(id=myid)
							if myplaylist not in blog.playlists.all():
								blog.playlists.add(myplaylist)
							else:
								blog.playlists.remove(myplaylist)
						return redirect('blog:BlogList')
					else:
						return redirect('blog:BlogList')
				else :
					return render(request, 'playlist/AddToPlayList.html' , {'post':playlists})
			else:
				return redirect('blog:BlogList')
		else:
			return redirect('accounts:Login')


class MyPlayListView(ListView):
	model = Blog
	context_object_name = 'post'
	template_name = 'playlist/MyPlayList.html'

	def get_queryset(self):
		my_play_list = PlayList.objects.get(id=self.kwargs['pk'])
		return my_play_list.play_list.all()


class MyListView(ListMixin, ListView):
	model = Blog
	context_object_name = 'post'
	template_name = 'list/MyList.html'

	def get_queryset(self):
		my_list = List.objects.get(id=self.kwargs['pk'])
		return my_list.list.all()


class TagListView(ListView):
	model = Blog
	context_object_name = 'post'
	template_name = 'blog/TagList.html'

	def get_queryset(self):
		tag = Tag.objects.get(id=self.kwargs['pk'])
		return tag.tad.all()

