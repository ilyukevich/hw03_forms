#from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Group
from .forms import PostForm
from django.contrib.auth.decorators import login_required
#import datetime as dt


def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    """view function for community page"""
    group = get_object_or_404(Group, slug=slug)
    #posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


# revision2
# close pages from unauthorized users
@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
        return render(request, 'new.html', {'form': form})
    form = PostForm(request.POST)
    if not form.is_valid():
        return render(request, 'new.html', {'form': form})
    form = form.save(commit=False)
    form.author = request.user
    form.save()
    return redirect('/')




