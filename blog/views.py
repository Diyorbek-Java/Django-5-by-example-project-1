from django.shortcuts import render
from .models import Post
from django.http import Http404

def post_list(request):
    posts=Post.published.all()
    return render(request,'blog/post/list.html',{'posts':posts})

def post_detail(request,id):
    pass