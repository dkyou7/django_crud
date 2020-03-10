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
    success_url = reverse_lazy("create_done")

class PostCreateDone(DetailView):
    model = Post
    template_name = 'blog/create_done.html'

class PostCreateDone(ListView):
    model = Post
    template_name = 'blog/create_done.html'
    context_object_name = 'createDone'      # 디폴트 컨텍스트 변수명 :  createDone

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/update.html'
    success_url = reverse_lazy('posts')

class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/delete_done.html'
    success_url = reverse_lazy('posts')         # 모든 처리가 다 끝나고 나서 어디로 이동할 것인가?