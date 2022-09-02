from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic import ListView , CreateView , UpdateView , DeleteView ,  DetailView
from .models import Blog , Tag , Story
from django.urls import reverse_lazy
from django.contrib.postgres.search import TrigramSimilarity
from .forms import SearchForm

class BlogList(ListView):
    model = Blog
    context_object_name = 'post'
    template_name = 'blog/BlogList.html'


    def get_queryset(self , **kwargs):
        post = Blog.objects.poblished()
        request = super(BlogList , self).get_context_data(**kwargs)
        request['form'] = searchForm()
        if 'search'  in request.GET :
            form = SearchForm(request.GET)
            if form.is_valid():
                search = form.cleaned_data['search']
                post = post.annotate(blogsearch = TrigramSimilarity('titel', search),).filter(blogsearch__gt = 0)
        return render(request , 'blog/search.html' , {'form' : form , 'post' : post})


class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/BlogDetail.html'
    def views(request , pk):
        blog = Blog.objects.get(pk = id)
        blog.views = request.user
        blog.save()

class BlogCreate(CreateView):
	model = Blog
	fields = ('titel', 'body', 'image', 'poblish' , 'film')
	template_name = "blog/create.html"

class BlogUpdate(UpdateView):
	model = Blog
	fields = ('titel', 'body', 'image', 'poblish' , 'film')
	template_name = "blog/update.html"

class BlogDelete(DeleteView):
	model = Blog
	success_url = reverse_lazy("blog:BlogList")
	template_name = "blog/delete.html"

def like1(request, postid):
    post = Blog.objects.get(postid = id)
    user = request.user
    if user not in post.likes.all():
        return HttpResponse('')
    post.likes.add(user)
    return redirect('blog:BlogDetail', postid)

def unlike1(request, postid):
    post = Blog.objects.get(postid = id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        return redirect('blog:BlogDetail', postid)

def search(request):
    post = Blog.objects.poblished()
    form = searchform()
    if 'search'  in request.GET :
        form = searchform(request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            blog = blog.annotate(blogsearch = TrigramSimilarity('titel', search),).filter(blogsearch__gt = 0)
    return render(request , 'blog/search.html' , {'form' : form , 'post' : post})

class SavedList(ListView):
	model = Blog
	context_object_name = 'post'
	template_name = "accounts/userlist.html"
	def get_queryset(self):
		return Blog.objects.filter(saved = self.request.user)

def like2(request, postid):
    post = Blog.objects.get(postid = id)
    user = request.user
    if user not in post.likes.all():
        return HttpResponse('')
    post.unlikes.add(user)
    return redirect('blog:BlogDetail', postid)
      
def unlike2(request, postid):
    post = Blog.objects.get(postid = id)
    user = request.user
    if user in post.likes.all():
        post.unlikes.remove(user)
        return redirect('blog:BlogDetail', postid)

def saved(request, postid):
    post = Blog.objects.get(postid = id)
    user = request.user
    if user not in post.likes.all():
        return HttpResponse('')
    post.saved.add(user)
    return redirect('blog:BlogDetail', postid)
     
def unsaved(request, postid):
    post = Blog.objects.get(postid = id)
    user = request.user
    if user in post.likes.all():
        post.saved.remove(user)
        return redirect('blog:BlogDetail', postid)

class TagCreate(CreateView):
	model = Tag
	fields = ('tag')
	template_name = "blog/createtag.html"

class TagUpdate(UpdateView):
	model = Tag
	fields = ('tag')
	template_name = "blog/updatetag.html"

class StoryList(ListView):
    model = Story
    context_object_name = 'post'
    template_name = 'blog/BlogList.html'

    def get_queryset(self):
        return Story.objects.all()

class StoryCreate(CreateView):
	model = Story
	fields = ('body', 'files')
	template_name = "blog/create.html"

class StoryUpdate(UpdateView):
	model = Story
	fields = ('body' , 'files')
	template_name = "blog/update.html"

def story_like(request , storyid):
    story = Story.objects.get(storyid = id)
    user = request.user
    if user not in story.likes.all():
        story.likes.add(user)
        return redirect('blog:storylist')

def story_unlike(request , storyid):
    story = Story.objects.get(storyid = id)
    user = request.user
    if user in story.likes.all():
        story.likes.remove(user)
        return redirect('blog:storylist')

class StoryDelete(DeleteView) :
    model = Story
    template_name = 'blog\storydelete.html'
    success_url = reverse_lazy('blog:BlogList')
