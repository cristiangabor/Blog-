from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from django.utils import timezone
from .forms import PostForm, ContactForm
# Create your views here.

def contact(request):
    form_class = ContactForm
    return render(request, 'blog/contact.html', {'form': form_class,})

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

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
