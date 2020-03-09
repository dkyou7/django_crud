from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    template_name='blog/index.html'
    context_object_name = 'list'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'detail'

class PostCreate(CreateView):
    model = Post
    fields = "__all__"
    template_name = 'blog/create.html'
    success_url = reverse_lazy("posts")