from django.shortcuts import render , redirect
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , ListView , DetailView
from .models import Coments , StoryComents
from django.urls import reverse_lazy
from django.http import HttpResponse

class BlogList(ListView):
	model = Coments
	context_object_name = 'blogpost'
	template_name = 'coments/list.html'
	def get_queryset(self):
		return Coments.objects.all()
	
class BlogCreate(CreateView):
	model = Coments
	fields = ('body',)
	template_name = "coments/create.html"

class BlogUpdate(UpdateView):
	model = Coments
	fields = ('body',)
	template_name = "coments/update.html"

class BlogDelete(DeleteView):
	model = Coments
	success_url = reverse_lazy("blog:BlogList")
	template_name = "coments/delete.html"

def like1(request , blogid):
	blog = Coments.objects.get(blogid = id)
	user = request.user
	if user in blog.likes.all():
		return HttpResponse('')
	blog.likes.add(user)
	return redirect('coments:BlogList')

def unlike1(request , blogid):
	blog = Coments.objects.get(blogid = id)
	user = request.user
	if user in blog.likes.all():
		blog.likes.remove(user)
		return redirect('coments:BlogList')

def like2(request , blogid):
	blog = Coments.objects.get(blogid = id)
	user = request.user
	if user in blog.likes.all():
		return HttpResponse('')
	blog.unlikes.add(user)
	return redirect('coments:BlogList')

def unlike2(request , blogid):
	blog = Coments.objects.get(blogid = id)
	user = request.user
	if user in blog.likes.all():
		blog.unlikes.remove(user)
		return redirect('coments:BlogList')

class StoryList(ListView):
	model = StoryComents
	context_object_name = 'blogpost'
	template_name = 'coments/storylist.html'
	def get_queryset(self):
		return StoryComents.objects.all()
	
class StoryCreate(CreateView):
	model = StoryComents
	fields = ('body',)
	template_name = "coments/storycreate.html"

class StoryUpdate(UpdateView):
	model = StoryComents
	fields = ('body',)
	template_name = "coments/storyupdate.html"

class StoryDelete(DeleteView):
	model = StoryComents
	success_url = reverse_lazy("blog:storylist")
	template_name = "coments/storydelete.html"

def like21(request , blogid):
	blog = StoryComents.objects.get(blogid = id)
	user = request.user
	if user in blog.likes.all():
		return HttpResponse('')
	blog.likes.add(user)
	return redirect('coments:storylist')

def unlike21(request , blogid):
	blog = StryComents.objects.get(blogid = id)
	user = request.user
	if user in blog.likes.all():
		blog.likes.remove(user)
		return redirect('coments:storylist')

def like22(request , blogid):
	blog = StoryComents.objects.get(blogid = id)
	user = request.user
	if user in blog.likes.all():
		return HttpResponse('')
	blog.unlikes.add(user)
	return redirect('coments:storylist')

def unlike22(request , blogid):
	blog = StoryComents.objects.get(blogid = id)
	user = request.user
	if user in blog.likes.all():
		blog.unlikes.remove(user)
		return redirect('coments:storylist')