from django.shortcuts import render , redirect
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , ListView , DetailView
from .models import Coments
from django.urls import reverse_lazy
from django.views import View
from .mixins import ComentMixin
from accounts.mixins import MyLoginRequiredMixin
from blog.models import Blog
from story.models import Story
from short.models import Short
from post.models import Post



class ComentCreateView(MyLoginRequiredMixin, CreateView):
	model = Coments
	fields = ('body',)
	template_name = "coments/ComentCreate.html"
	
	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form   

	def form_valid(self, form):
		form.instance.author = self.request.user
		my_id = self.kwargs['pk']
		try:
			coment = Blog.objects.get(id=my_id)
		except:
			try:
				coment = Post.objects.get(id=my_id)
			except:
				try:
					coment = Short.objects.get(id=my_id)
				except:
					coment = Story.objects.get(id=my_id)
		form.instance.content_object = coment
		return super().form_valid(form)


class OneComentsView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		coment = Coments.objects.get(id=pk)
		user = request.user
		if user.is_authenticated:
			coments = Coments.objects.filter(one_coments=coment)
			if request.method == 'POST':
				body=request.POST.get('body')
				new_coment=Coments.objects.create(body=body,
				one_respones=coment, author=user, content_type=coment.content_type,
				object_id=coment.object_id,)
				new_coment.save()
				return redirect('coment:detail', coment.id)
			else:
				return render(request, 'coments/OneComents.html', {'coments':coments})
		else:
			return redirect('accounts:Login')


class TowComentsView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		coment = Coments.objects.get(id=pk)
		user = request.user
		if user.is_authenticated:
			if request.method == 'POST':
				body = request.POST.get('body')
				new_coment = coment.objects.create(body=body, author=user,
				one_coments=coment.one_coments, tow_respones=coment, 
				content_type=coment.content_type, object_id=coment.object_id,)
				new_coment.save()
				return redirect('coment:detail', coment.one_coments.id)
			else:
				return render(request, 'coments/TowComents.html')
			
		else:
			return redirect('accounts:Login')


class ComentUpdateView(ComentMixin, UpdateView):
	model = Coments
	fields = ('body',)
	template_name = "coments/ComentUpdate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form 


class ComentDeleteView(ComentMixin, DeleteView):
	model = Coments
	success_url = reverse_lazy("blog:BlogList")
	template_name = "coments/ComentDelete.html"


class ComentLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		blog = Coments.objects.get(id=pk)
		if user.is_authenticated:
			if user in blog.unlikes.all():
				blog.unlikes.remove(user)
			if user not in blog.likes.all():
				blog.likes.add(user)
			else:
				blog.likes.remove(user)			
		else:
			return redirect('accounts:Login')


		return redirect('coments:ComentList')


class ComentUnLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		blog = Coments.objects.get(id=pk)
		if user.is_authenticated:
			if user in blog.likes.all():
				blog.likes.remove(user)
			if user not in blog.unlikes.all():
				blog.unlikes.add(user)
			else:
				blog.unlikes.remove(user)
		else:
			return redirect('accounts:Login')

		return redirect('coments:ComentList')

