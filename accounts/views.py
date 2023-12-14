from django.shortcuts import render , redirect
from django.views.generic import UpdateView , ListView, DetailView, CreateView
from .models import User, Following, OTPCode
from django.urls import reverse_lazy
from django.contrib.auth import logout
from video.models import Video
from django.contrib.auth.views import LoginView
from django.views import View
from .mixins import UserMixin
from list.models import  List, PlayList
from .tasks import send_mail_task
from random import randint


class EditProfileView(UserMixin, UpdateView):
	model = User
	template_name = "accounts/EditProfile.html"
	fields = ('body', 'email', 'image', 'name')
	success_url = reverse_lazy("chat:VideoList")

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['email'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['name'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form   


class ProfileView(UserMixin, DetailView):
	model = User
	template_name = "accounts/Profile.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['lists'] = List.objects.filter(user__id=self.request.user.id)
		context['paly_lists'] = PlayList.objects.filter(user__id=self.request.user.id)
		context['following'] = Following.nodes.get(user_id=self.request.user.id).followers.all()

		return context


class SingUpView(CreateView):
	model = User
	fields = ('password', 'email', 'body', 'image', 'name')
	template_name = "accounts/Sing_up.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['email'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['name'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['password'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form   

	def form_valid(self, form):
		password = form.cleaned_data['password']
		is_str = False
		is_num = False
		for x in password:
			if x.isalpha():
				is_str = True		
		for x in password:
			if x.isdigit():
				is_num = True
		if len(password) > 8 and is_num == True and is_str == True:
			form.instance.set_password(password)
		else:
			return redirect('accounts:Sing_up')
		return super().form_valid(form)

	def get_success_url(self):
		print(self.object.pk)
		return reverse_lazy('accounts:CreateCode', kwargs={'pk': self.object.pk})


class CreateCodeView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = User.objects.get(pk=pk)
		code = randint(1000, 9999)
		new_code = OTPCode.objects.create(user=user, code=code)
		new_code.save()
		massages = str(code)
		send_mail_task.delay(massages, user.email)
		return redirect('accounts:CheckCode', new_code.id)


class CheckCodeView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		code = OTPCode.objects.get(pk=pk)
		if request.method == 'POST':
			user_code = request.POST.get('code')
			user = User.objects.get(id=code.user.id)
			if code.code == user_code:
				user.is_active = True
				user.save()
				return redirect('accounts:Login')
		else:
			return render(request, 'accounts/CheckCode.html')


class UserLoginView(LoginView):
	model = User
	template_name = "accounts/Login.html"
	success_url = reverse_lazy("chat:VideoList")

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['username'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['password'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form   


class UserVideoListView(ListView):
	model = Video
	context_object_name = 'post'
	template_name = "accounts/UserVideoList.html"
	
	def get_queryset(self):
		return self.model.objects.filter(author=self.request.user)


class FollowView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		account = User.objects.get(id=pk)
		if user.is_authenticated:
			follower = Following.nodes.get(user_id=user.id)
			following = Following.nodes.get(user_id=account.id)
			if user not in account.follower.all():
				account.follower.add(user)
				follower.followers.connect(following)
			else:
				account.follower.remove(user)	
				follower.followers.disconnect(following)		
		else:
			return redirect('accounts:Login')

		return redirect('accounts:Profile', account.id)


class NotificationView(View):
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

		return redirect('accounts:Profile', account.id)


class UserLogoutView(View):
	def dispatch(self, request, *args, **kwargs):
		logout(self.request)
		return redirect('chat:VideoList')


class ChangePasswordView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = User.objects.get(id=pk)
		request_user = request.user
		if request_user.is_authenticated:
			if request_user.id == user.id:
				if request.method == 'POST':
					old_password = request.POST.get('old_password')
					new_password = request.POST.get('new_password')
					new_password_confirm = request.POST.get('new_password_confirm')
					is_str = False
					is_num = False
					for x in new_password:
						if x.isalpha():
							is_str = True		
					for x in new_password:
						if x.isdigit():
							is_num = True

					if user.check_password(old_password):
						if new_password == new_password_confirm and len(new_password) < 8 and  is_num == True and is_str == True:
							user.set_password(new_password)
				else:
					return render(request, 'accounts/ChangePassword.html')
			else:
				return redirect('chat:VideoList')
		else:
			return redirect('accounts:Login')
