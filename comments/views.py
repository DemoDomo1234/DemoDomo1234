from django.shortcuts import render , redirect
from django.views.generic import CreateView , UpdateView , DeleteView , ListView , DetailView
from .models import Comments
from django.urls import reverse_lazy
from django.views import View
from .mixins import CommentMixin
from accounts.mixins import LoginRequiredMixin
from video.models import Video
from story.models import Story
from short.models import Short
from post.models import Post


class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comments
	fields = ('body',)
	template_name = "comments/CommentCreate.html"
	
	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form   

	def form_valid(self, form):
		form.instance.author = self.request.user
		id = self.kwargs['pk']
		obj = self.kwargs['obj']
		if obj == 'obj_video':
			comment = Video.objects.get(id=id)
		elif obj == 'obj_post':
			comment = Post.objects.get(id=id)
		elif obj == 'obj_short':
			comment = Short.objects.get(id=id)
		elif obj == 'obj_story':
			comment = Story.objects.get(id=id)

		form.instance.content_object = comment
		return super().form_valid(form)


class ReplyCommentView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		comment = Comments.objects.get(id=pk)
		user = request.user
		if user.is_authenticated:
			comments = Comments.objects.filter(reply=comment)
			if request.method == 'POST':
				body=request.POST.get('body')
				new_comment=Comments.objects.create(body=body,
				reply=comment, author=user, content_type=comment.content_type,
				object_id=comment.object_id,)
				new_comment.save()
				return redirect('comment:detail', comment.id)
			else:
				return render(request, 'comments/ReplyComment.html', {'comments':comments})
		else:
			return redirect('accounts:Login')


class ReplyToReplyCommentView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		comment = Comments.objects.get(id=pk)
		user = request.user
		if user.is_authenticated:
			if request.method == 'POST':
				body = request.POST.get('body')
				new_comment = Comments.objects.create(body=body, author=user,
				reply=comment.reply, reply_to_reply=comment, 
				content_type=comment.content_type, object_id=comment.object_id,)
				new_comment.save()
				return redirect('comment:detail', comment.reply.id)
			else:
				return render(request, 'comments/ReplyToReplyComment.html')		
		else:
			return redirect('accounts:Login')


class CommentUpdateView(CommentMixin, UpdateView):
	model = Comments
	fields = ('body',)
	template_name = "comments/CommentUpdate.html"

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form['body'].field.widget.attrs.update({'class' : 'btn btn-outline-light'})
		return form 


class CommentDeleteView(CommentMixin, DeleteView):
	model = Comments
	success_url = reverse_lazy("chat:VideoList")
	template_name = "comments/CommentDelete.html"


class CommentLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		comment = Comments.objects.get(id=pk)
		if user.is_authenticated:
			if user in comment.un_likes.all():
				comment.un_likes.remove(user)
			if user not in comment.likes.all():
				comment.likes.add(user)
			else:
				comment.likes.remove(user)			
		else:
			return redirect('accounts:Login')


		return redirect('chat:VideoList')


class CommentUnLikesView(View):
	def dispatch(self, request, pk, *args, **kwargs):
		user = request.user
		comment = Comments.objects.get(id=pk)
		if user.is_authenticated:
			if user in comment.likes.all():
				comment.likes.remove(user)
			if user not in comment.un_likes.all():
				comment.un_likes.add(user)
			else:
				comment.un_likes.remove(user)
		else:
			return redirect('accounts:Login')

		return redirect('chat:VideoList')

