from django.shortcuts import redirect
from django.views.generic import (ListView, CreateView, UpdateView,
								  DeleteView, DetailView)
from .models import Short
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Count
from .mixins import ShortMixin
from accounts.mixins import MyLoginRequiredMixin



class ShortListView(ListView):
    model = Short
    context_object_name = 'post'
    template_name = 'short/ShortList.html'

    def get_queryset(self):
        return self.model.objects.all()


class ShortDetailView(MyLoginRequiredMixin, DetailView):
	model = Short
	template_name = 'short/ShortDetail.html'

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


class ShortCreateView(MyLoginRequiredMixin, CreateView):
	model = Short
	fields = ('body', 'files', 'tag')
	template_name = "short/ShortCreate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class ShortUpdateView(ShortMixin, UpdateView):
	model = Short
	fields = ('body', 'files', 'tag')
	template_name = "short/ShortUpdate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
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
