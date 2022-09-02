from django.shortcuts import render , redirect
from django.views.generic import UpdateView , FormView , ListView , DetailView , CreateView
from .models import account 
from .forms import SingupForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from blog.models import Blog
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

class Profile(UpdateView):
	model = account
	template_name = "accounts/profile.html"
	fields = ('password', 'last_name', 'frest_name', 'email',  'address',  'body', 'image', 'date_of_birth', 'gender')
	success_url = reverse_lazy("blog:BlogList")

class Profile1(DetailView):
	model = account
	template_name = "accounts/profile1.html"

class SingupView(CreateView):
	form_class = SingupForm
	template_name = "accounts/Singup.html"
	success_url = reverse_lazy("blog:BlogList")

class LoginView(LoginView):
	model = account
	template_name = "accounts/Login.html"
	success_url = reverse_lazy("blog:BlogList")

class UserList(ListView):
	model = Blog
	context_object_name = 'post'
	template_name = "accounts/userlist.html"
	def get_queryset(self):
		return Blog.objects.filter(author = self.request.user)
	
def LogoutView(request):
		logout(request)
		return redirect('blog:BlogList')

def folo(request , foloid):
	blog = account.objects.get(id = foloid)
	user = request.user
	if user in blog.folower.all():
		return HttpResponse('')
	blog.folower.add(user)
	return redirect('accounts:Profile1' , foloid)

def unfolo(request , foloid):
	blog = account.objects.get(id = foloid)
	user = request.user
	if user in blog.folower.all():
		blog.folower.remove(user)
		return redirect('accounts:Profile1' , foloid)
	else:
		return HttpResponse('')
