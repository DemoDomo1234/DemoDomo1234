from django.shortcuts import redirect
from django.views.generic import (ListView, CreateView, UpdateView,
								  DeleteView, DetailView)
from .models import Video
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Count
from .mixins import VideoMixin
from accounts.mixins import LoginRequiredMixin
from .documents import VideoDocument


class VideoListView(ListView):
	model = Video
	context_object_name = 'post'
	template_name = 'video/VideoList.html'

	def get_queryset(self):
		video = {}
		if 'search' in self.request.GET:
			search = self.request.GET.get('search')
			video = VideoDocument.search().filter("fuzzy", title=search)
		return video
	

class VideoDetailView(LoginRequiredMixin, DetailView):
	model = Video
	template_name = 'video/VideoDetail.html'

	def get_context_data(self, **kwargs):
		tag = self.model.tag.values_list('id', flat=True)
		context = super().get_context_data(**kwargs)
		context['videos'] = self.model.objects.filter(tag__in=tag).exclude(
		id = self.kwargs['pk']).annotate(tag_count=Count('tag')).order_by('-tag_count')
		context['comments'] = self.model.objects.get(id=self.kwargs['pk']).comments.all()
		return context


class VideoCreateView(LoginRequiredMixin, CreateView):
	model = Video
	fields = ('title', 'body', 'image', 'published', 'film', 'tag')
	template_name = "video/VideoCreate.html"
	
	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['title'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form       

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.save()
		for tag in form.cleaned_data['tag'] :
			form.instance.tag.add(tag)
		form.save()
		return super(VideoCreateView, self).form_valid(form)


class VideoUpdateView(VideoMixin, UpdateView):
	login_url = '/login/'
	model = Video
	fields = ('title', 'body', 'image', 'published', 'film', 'tag')
	template_name = "Video/VideoUpdate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['title'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		form['tag'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form    


class VideoDeleteView(VideoMixin, DeleteView):
	login_url = '/login/'
	model = Video
	success_url = reverse_lazy("video:VideoList")
	template_name = "video/VideoDelete.html"


class VideoLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		video = Video.objects.get(id=pk)
		if user.is_authenticated:
			if user in video.un_likes.all():
				video.un_likes.remove(user)
			if user not in video.likes.all():
				video.likes.add(user)
			else:
				video.likes.remove(user)
		else:
			return redirect('accounts:Login')

		return redirect('video:VideoDetail', video.id)


class VideoUnLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		video = Video.objects.get(id=pk)
		if user.is_authenticated:
			if user in video.likes.all():
				video.likes.remove(user)
			if user not in video.un_likes.all():
				video.un_likes.add(user)
			else:
				video.un_likes.remove(user)
		else:
			return redirect('accounts:Login')
		return redirect('video:VideoDetail', video.id)


class VideoSavedView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		video = Video.objects.get(id=pk)
		if user.is_authenticated:
			if user not in video.saved.all():
				video.saved.add(user)
			else:
				video.saved.remove(user)			
		else:
			return redirect('accounts:Login')

		return redirect('video:VideoDetail', video.id)


class SavedListView(LoginRequiredMixin, ListView):
	model = Video
	context_object_name = 'post'
	template_name = "video/SaveList.html"
	def get_queryset(self):
		return self.model.objects.filter(saved = self.request.user)
