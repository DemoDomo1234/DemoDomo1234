from django.shortcuts import render , redirect
from django.views.generic import UpdateView , FormView , ListView , DetailView , CreateView
from .models import User 
from django.urls import reverse_lazy
from django.contrib.auth import logout
from blog.models import Blog
from django.contrib.auth.views import LoginView
from django.views import View
from .mixins import UserMixin, MyLoginRequiredMixin
from blog.models import (Blog, Story, Short, Post, List, PlayList, Image)

class EditProfileView(UserMixin, UpdateView):
	model = User
	template_name = "accounts/EditProfile.html"
	fields = ('password', 'email', 'body', 'image', 'name')
	success_url = reverse_lazy("blog:BlogList")

	def get_form(self, form_class=None):
		form = super(EditProfileView, self).get_form(form_class)
		form['email'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['name'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['password'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form   

class ProfileView(UserMixin, DetailView):
	model = User
	template_name = "accounts/Profile.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['lists'] = List.objects.filter(user=self.request.user)
		context['palylists'] = PlayList.objects.filter(user=self.request.user)
		return context

class SingupView(CreateView):
	model = User
	fields = ('password', 'email', 'body', 'image', 'name')
	template_name = "accounts/Singup.html"
	success_url = reverse_lazy("blog:BlogList")

	def get_form(self, form_class=None):
		form = super(SingupView, self).get_form(form_class)
		form['email'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['name'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['password'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form   

	def form_valid(self, form):
		password = form.cleaned_data['password']
		is_str = False
		is_num = False
		for x in password :
			if x.isalpha() :
				is_str = True		
		for x in password :
			if x.isdigit() :
				is_num = True
		if len(password) < 8 and is_num == True and is_str == True:
			form.instance.set_password(password)
		return super(SingupView, self).form_valid(form)

class UserLoginView(LoginView):
	model = User
	template_name = "accounts/Login.html"
	success_url = reverse_lazy("blog:BlogList")

	def get_form(self, form_class=None):
		form = super(UserLoginView, self).get_form(form_class)
		form['username'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['password'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form   

class UserListView(UserMixin, ListView):
	model = Blog
	context_object_name = 'post'
	template_name = "accounts/UserList.html"
	def get_queryset(self):
		return Blog.objects.filter(author = self.request.user)

class FolowView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		account = User.objects.get(id=pk)
		if user.is_authenticated:
			if user not in account.folower.all():
				account.folower.add(user)
			else:
				account.folower.remove(user)			
		else:
			return redirect('accounts:Login')

		return redirect('accounts:Profile' , account.id)

class NotyView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		account = User.objects.get(id=pk)
		if user.is_authenticated:
			if user not in account.notifications.all():
				account.notifications.add(user)
			else:
				account.notifications.remove(user)			
		else:
			return redirect('accounts:Login')

		return redirect('accounts:Profile' , account.id)

class UserLogoutView(View):
	def dispatch(self, request, *args, **kwargs):
		logout(self.request)
		return redirect('blog:BlogList')

class ChangePassowrdView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = User.objects.get(id=pk)
		myuser = request.user
		if myuser.is_authenticated:
			if myuser.id == user.id :
				if request.method == 'POST':
					old_password = request.POST.get('old_password')
					new_password1 = request.POST.get('new_password1')
					new_password2 = request.POST.get('new_password2')
					is_str = False
					is_num = False
					for x in new_password1 :
						if x.isalpha() :
							is_str = True		
					for x in new_password1 :
						if x.isdigit() :
							is_num = True

					if user.check_password(old_password):
						if new_password1 == new_password2 and len(new_password1) < 8 and  is_num == True and is_str == True:
							user.set_password(new_password1)
				else:
					return render(request, 'accounts/ChangePassowrd.html')
			else:
				return redirect('blog:BlogList')
		else:
			return redirect('accounts:Login')
