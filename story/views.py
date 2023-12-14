from django.shortcuts import redirect
from django.views.generic import (ListView, CreateView, UpdateView,
								  DeleteView, DetailView)
from .models import Story
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Count
from .mixins import StoryMixin
from accounts.mixins import LoginRequiredMixin


class StoryListView(ListView):
	model = Story
	context_object_name = 'post'
	template_name = 'story/StoryList.html'

	def get_queryset(self):
		return self.model.objects.all()


class StoryDetailView(LoginRequiredMixin, DetailView):
	model = Story
	template_name = 'story/StoryDetail.html'

	def get_context_data(self, **kwargs):
		tag = self.model.tag.values_list('id', flat=True)
		context = super().get_context_data(**kwargs)
		context['blogs'] = self.model.objects.filter(tag__in=tag).exclude(
		id=self.kwargs['pk']).annotate(tag_count=Count('tag')).order_by('-tag_count')
		context['comments'] = self.model.objects.get(id=self.kwargs['pk']).comments.all()
		return context


class StoryCreateView(LoginRequiredMixin, CreateView):
	model = Story
	fields = ('body', 'files', 'tag')
	template_name = "story/StoryCreate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class StoryUpdateView(StoryMixin, UpdateView):
	model = Story
	fields = ('body' , 'files', 'tag')
	template_name = "story/StoryUpdate.html"
	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    


class StoryDeleteView(StoryMixin, DeleteView):
    model = Story
    template_name = 'story/StoryDelete.html'
    success_url = reverse_lazy('chat:VideoList')


class StoryLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		story = Story.objects.get(id=pk)
		if user.is_authenticated:
			if user not in story.likes.all():
				story.likes.add(user)
			else:
				story.likes.remove(user)			
		else:
			return redirect('accounts:Login')

		return redirect('story:StoryDetail', story.id)

