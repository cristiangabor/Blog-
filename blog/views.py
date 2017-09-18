from django.shortcuts import render, get_object_or_404
from .models import Post
from django.conf import settings
from django.shortcuts import redirect
from django.utils import timezone
from .forms import PostForm
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required
# Create your views here.

def contact(request):
    about_me = """
    I am a young Python enthusiast from Romania, Timisoara, with 2 years of experience
    in python programming. I am interested in making usefull tools with the help of programming. My next
    dream is to build an electric motobike controlled by raspberry pi.

    """


    return render(request, 'blog/contact.html', {"me":about_me})

def archive(request):

    posts = Post.objects.all()
    return render(request, 'blog/archive.html', {'posts':posts})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # For search button
    query = request.GET.get("q") # get guerry
    if query: # if anyquerry is there then execute...
        query_list=Post.objects.filter(title__contains = query)
        return render(request, 'blog/post_list.html', {'posts':query_list})
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None ,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
