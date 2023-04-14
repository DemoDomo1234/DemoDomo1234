from django.shortcuts import redirect
from django.views.generic import (ListView, CreateView, UpdateView,
								  DeleteView, DetailView)
from .models import Blog
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Count
from .mixins import BlogMixin
from accounts.mixins import MyLoginRequiredMixin
from .documents import BlogDocument


class BlogListView(ListView):
	model = Blog
	context_object_name = 'post'
	template_name = 'blog/BlogList.html'

	def get_queryset(self):
		blog = {}
		if 'search' in self.request.GET :
			search = self.request.GET.get('search')
			blog = BlogDocument.search().filter("fuzzy", titel=search)
		return blog
	

class BlogDetailView(MyLoginRequiredMixin, DetailView):
	model = Blog
	template_name = 'blog/BlogDetail.html'

	def get_context_data(self, **kwargs):
		tag = self.model.tag.values_list('id' , flat = True)
		context = super().get_context_data(**kwargs)
		context['blogs'] = self.model.objects.filter(tag__in = tag ).exclude(
		id = self.kwargs['pk']).annotate(tag_count = Count('tag')).order_by('-tag_count')
		context['coments'] = self.model.objects.get(id=self.kwargs['pk']).comments.all()
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
		form = super().get_form(form_class)
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
		form = super().get_form(form_class)
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
		return self.model.objects.filter(saved = self.request.user)
