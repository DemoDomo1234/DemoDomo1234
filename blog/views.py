from django.shortcuts import (render , redirect , get_object_or_404)
from django.views.generic import (ListView, CreateView, UpdateView,
								  DeleteView, DetailView)
from .models import (Blog, Story, Short, Post, List, PlayList, Image)
from django.urls import reverse_lazy
from django.contrib.postgres.search import TrigramSimilarity
from django.views import View
from taggit.models import Tag 
from django.db.models import Count
from .mixins import (BlogMixin, StoryMixin, ShortMixin, PostMixin,
					ListMixin, PlayListMixin, ImageMixin,)
from accounts.mixins import MyLoginRequiredMixin
import datetime 

class BlogListView(ListView):
	model = Blog
	context_object_name = 'post'
	template_name = 'blog/BlogList.html'
	def get_queryset(self):
		blog = self.model.objects.poblished()
		if 'search' in self.request.GET :
			search = self.request.GET.get('search')
			blog = blog.annotate(blog_search=TrigramSimilarity(
        	'titel', search),).filter(
        	blog_search__gt=0.3).order_by('-blog_search')
		return blog
	
class BlogDetailView(MyLoginRequiredMixin, DetailView):
	model = Blog
	template_name = 'blog/BlogDetail.html'

	def get_context_data(self, **kwargs):
		tag = self.model.tag.values_list('id' , flat = True)
		context = super().get_context_data(**kwargs)
		context['blogs'] = Blog.objects.filter(tag__in = tag ).exclude(
		id = self.kwargs['pk']).annotate(tag_count = Count('tag')).order_by('-tag_count')
		context['coments'] = Blog.objects.get(id=self.kwargs['pk']).comments.all()
		return context
	def blog_view(self):
		user = self.request.user
		if user not in self.model.views.all():
			self.model.views.add(user)
		else:
			self.model.views.remove(user)

class BlogCreateView(MyLoginRequiredMixin, CreateView):
	model = Blog
	fields = ('titel', 'body', 'image', 'poblished' , 'film' , 'tag')
	template_name = "blog/BlogCreate.html"
	
	def get_form(self, form_class=None):
		form = super(BlogCreateView, self).get_form(form_class)
		form['titel'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form       

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.save()
		for mytag in form.cleaned_data['tag'] :
			form.instance.tag.add(mytag)
		form.save()
		return super(BlogCreateView, self).form_valid(form)

class BlogUpdateView(BlogMixin, UpdateView):
	login_url = '/login/'
	model = Blog
	fields = ('titel', 'body', 'image', 'poblished', 'film', 'tag')
	template_name = "blog/BlogUpdate.html"

	def get_form(self, form_class=None):
		form = super(BlogUpdateView, self).get_form(form_class)
		form['titel'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    

class BlogDeleteView(BlogMixin, DeleteView):
	login_url = '/login/'
	model = Blog
	success_url = reverse_lazy("blog:BlogList")
	template_name = "blog/BlogDelete.html"

class BlogLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		blog = Blog.objects.get(id=pk)
		if user.is_authenticated:
			if user in blog.unlikes.all():
				blog.unlikes.remove(user)
			if user not in blog.likes.all():
				blog.likes.add(user)
			else:
				blog.likes.remove(user)
		else:
			return redirect('accounts:Login')

		return redirect('blog:BlogDetail' , blog.id)

class BlogUnLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		blog = Blog.objects.get(id=pk)
		if user.is_authenticated:
			if user in blog.likes.all():
				blog.likes.remove(user)
			if user not in blog.unlikes.all():
				blog.unlikes.add(user)
			else:
				blog.unlikes.remove(user)
		else:
			return redirect('accounts:Login')
		return redirect('blog:BlogDetail' , blog.id)

class BlogSavedView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		blog = Blog.objects.get(id=pk)
		if user.is_authenticated:
			if user not in blog.saved.all():
				blog.saved.add(user)
			else:
				blog.saved.remove(user)			
		else:
			return redirect('accounts:Login')

		return redirect('blog:BlogDetail' , blog.id)

class SavedListView(MyLoginRequiredMixin, ListView):
	model = Blog
	context_object_name = 'post'
	template_name = "blog/SavedList.html"
	def get_queryset(self):
		return Blog.objects.filter(saved = self.request.user)

class StoryListView(ListView):
	model = Story
	context_object_name = 'post'
	template_name = 'story/StoryList.html'

	def get_queryset(self):
		return Story.objects.all()

	def story_active(self):
		today = datetime.date.today()
		for model in Story.objects.all():
			fenish_day = model.time + relativedelta(day=7)
			if fenish_day > today:
				model.delete()

class StoryDetailView(MyLoginRequiredMixin, DetailView):
	model = Story
	template_name = 'story/StoryDetail.html'

	def get_context_data(self, **kwargs):
		tag = self.model.tag.values_list('id' , flat = True)
		context = super().get_context_data(**kwargs)
		context['blogs'] = Story.objects.filter(tag__in = tag ).exclude(
		id = self.kwargs['pk']).annotate(tag_count = Count('tag')).order_by('-tag_count')
		context['coments'] = Story.objects.get(id=self.kwargs['pk']).comments.all()
		return context

	def blog_view(self):
		user = self.request.user
		if user not in self.model.views.all():
			self.model.views.add(user)
		else:
			self.model.views.remove(user)

	def story_active(self):
		today = datetime.date.today()
		fenish_day = self.model.time + relativedelta(day=7)
		if fenish_day > today:
			self.model.delete()

class StoryCreateView(MyLoginRequiredMixin, CreateView):
	model = Story
	fields = ('body', 'files', 'tag')
	template_name = "story/StoryCreate.html"

	def get_form(self, form_class=None):
		form = super(StoryCreateView, self).get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(StoryCreateView, self).form_valid(form)

class StoryUpdateView(StoryMixin, UpdateView):
	model = Story
	fields = ('body' , 'files', 'tag')
	template_name = "story/StoryUpdate.html"
	def get_form(self, form_class=None):
		form = super(StoryUpdateView, self).get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    

class StoryDeleteView(StoryMixin, DeleteView):
    model = Story
    template_name = 'story/StoryDelete.html'
    success_url = reverse_lazy('blog:BlogList')

class StoryLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		story = Story.objects.get(id=pk)
		if user.is_authenticated:
			if user in story.unlikes.all():
				story.unlikes.remove(user)
			if user not in story.likes.all():
				story.likes.add(user)
			else:
				story.likes.remove(user)			
		else:
			return redirect('accounts:Login')

		return redirect('blog:StoryDetail', story.id)

class ShortListView(ListView):
    model = Short
    context_object_name = 'post'
    template_name = 'short/ShortList.html'

    def get_queryset(self):
        return Short.objects.all()

class ShortDetailView(MyLoginRequiredMixin, DetailView):
	model = Short
	template_name = 'short/ShortDetail.html'

	def get_context_data(self, **kwargs):
		tag = self.model.tag.values_list('id' , flat = True)
		context = super().get_context_data(**kwargs)
		context['blogs'] = Short.objects.filter(tag__in = tag ).exclude(
		id = self.kwargs['pk']).annotate(tag_count = Count('tag')).order_by('-tag_count')
		context['coments'] = Short.objects.get(id=self.kwargs['pk']).comments.all()
		return context
	def blog_view(self):
		user = self.request.user
		if user not in self.model.views.all():
			self.model.views.add(user)
		else:
			self.model.views.remove(user)

class ShortCreateView(MyLoginRequiredMixin, CreateView):
	model = Short
	fields = ('body', 'files', 'tag')
	template_name = "short/ShortCreate.html"

	def get_form(self, form_class=None):
		form = super(ShortCreateView, self).get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ShortCreateView, self).form_valid(form)

class ShortUpdateView(ShortMixin, UpdateView):
	model = Short
	fields = ('body', 'files', 'tag')
	template_name = "short/ShortUpdate.html"

	def get_form(self, form_class=None):
		form = super(ShortUpdateView, self).get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    

class ShortDeleteView(ShortMixin, DeleteView):
    model = Short
    template_name = 'short/ShortDelete.html'
    success_url = reverse_lazy('blog:BlogList')

class ShortLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		short = Short.objects.get(id=pk)
		if user.is_authenticated:
			if user in short.unlikes.all():
				short.unlikes.remove(user)
			if user not in short.likes.all():
				short.likes.add(user)
			else:
				short.likes.remove(user)			
		else:
			return redirect('accounts:Login')


		return redirect('blog:ShortDetail', short.id)

class ShortUnLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		short = Short.objects.get(id=pk)
		if user.is_authenticated:
			if user in short.likes.all():
				short.likes.remove(user)
			if user not in short.unlikes.all():
				short.unlikes.add(user)
			else:
				short.unlikes.remove(user)			
		else:
			return redirect('accounts:Login')

		return redirect('blog:ShortDetail', short.id)

class PostListView(ListView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/PostList.html'

    def get_queryset(self):
        return Post.objects.all()

class PostDetailView(MyLoginRequiredMixin, DetailView):
	model = Post
	template_name = 'post/PostDetail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['coments'] = Post.objects.get(id=self.kwargs['pk']).comments.all()
		return context
	def blog_view(self):
		user = self.request.user
		if user not in self.model.views.all():
			self.model.views.add(user)
		else:
			self.model.views.remove(user)

class PostCreateView(MyLoginRequiredMixin, CreateView):
	model = Post
	fields = ('body',)
	template_name = "post/PostCreate.html"

	def get_form(self, form_class=None):
		form = super(PostCreateView, self).get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(PostCreateView, self).form_valid(form)

class PostUpdateView(PostMixin, UpdateView):
	model = Post
	fields = ('body',)
	template_name = "post/PostUpdate.html"

	def get_form(self, form_class=None):
		form = super(PostUpdateView, self).get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    

class PostDeleteView(PostMixin, DeleteView):
    model = Post
    template_name = 'post/PostDelete.html'
    success_url = reverse_lazy('blog:BlogList')

class PostLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		post = Post.objects.get(id=pk)
		if user.is_authenticated:
			if user in post.unlikes.all():
				post.unlikes.remove(user)
			if user not in post.likes.all():
				post.likes.add(user)
			else:
				post.likes.remove(user)			
		else:
			return redirect('accounts:Login')


		return redirect('blog:PostDetail', post.id)

class PostUnLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		post = Post.objects.get(id=pk)
		if user.is_authenticated:
			if user in post.likes.all():
				post.likes.remove(user)
			if user not in post.unlikes.all():
				post.unlikes.add(user)
			else:
				post.unlikes.remove(user)			
		else:
			return redirect('accounts:Login')

		return redirect('blog:PostDetail', post.id)

class ListCreateView(MyLoginRequiredMixin, CreateView):
	model = List
	fields = ('body', 'titel')
	template_name = "list/ListCreate.html"

	def get_form(self, form_class=None):
		form = super(ListCreateView, self).get_form(form_class)
		form['titel'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form  

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ListCreateView, self).form_valid(form)

class ListUpdateView(ListMixin, UpdateView):
	model = List
	fields = ('body', 'titel')
	template_name = "list/ListUpdate.html"

	def get_form(self, form_class=None):
		form = super(ListUpdateView, self).get_form(form_class)
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
		form = super(PlayLitCreateView, self).get_form(form_class)
		form['titel'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form 

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(PlayLitCreateView, self).form_valid(form)

class PlayListUpdateView(PlayListMixin, UpdateView):
	model = PlayList
	fields = ('body', 'titel')
	template_name = "playlst/PlayListUpdate.html"

	def get_form(self, form_class=None):
		form = super(PlayListUpdateView, self).get_form(form_class)
		form['titel'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form 

class PlayListDeleteView(PlayListMixin, DeleteView):
    model = PlayList
    template_name = 'playlst/PlayListDelete.html'
    success_url = reverse_lazy('blog:BlogList')

class ImageCreateView(MyLoginRequiredMixin, CreateView):
	model = Image
	fields = ('image',)
	template_name = "image/ImageCreate.html"

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.post = Post.objects.get(id=self.kwargs['pk'])
		return super(ImageCreateView, self).form_valid(form)

class ImageUpdateView(ImageMixin, UpdateView):
	model = Image
	fields = ('image',)
	template_name = "image/ImageUpdate.html"

class ImageDeleteView(ImageMixin, DeleteView):
    model = Image
    template_name = 'image/ImageDelete.html'
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
		return Blog.objects.filter(playlists = my_play_list)

class MyListView(ListMixin, ListView):
	model = Blog
	context_object_name = 'post'
	template_name = 'list/MyList.html'

	def get_queryset(self):
		my_list = List.objects.get(id=self.kwargs['pk'])
		return Blog.objects.filter(lists = my_list)

class TagListView(ListView):
	model = Blog
	context_object_name = 'post'
	template_name = 'blog/TagList.html'

	def get_queryset(self):
		tag = Tag.objects.get(id=self.kwargs['pk'])
		return Blog.objects.filter(tag = tag)
