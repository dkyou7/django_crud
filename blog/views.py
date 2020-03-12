from django.shortcuts import render, get_object_or_404, redirect

# from django.views.generic.list import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic.detail import DetailView

# from django.urls import reverse_lazy

from .models import Post

# # Create your views here.
# class PostList(ListView):
#     model = Post                        # 모델 뭐쓸래?
#     template_name='blog/index.html'     # 어떤 template를 사용해볼래?
#     context_object_name = 'list'        # template 파라메타로 넘길 데이터 값은 뭐할래? default: object

# class PostDetail(DetailView):
#     model = Post
#     template_name = 'blog/detail.html'
#     context_object_name = 'detail'

# class PostCreate(CreateView):
#     model = Post
#     fields = "__all__"                          # 생성하거나, 수정할 필드,
#     template_name = 'blog/create.html'
#     context_object_name = 'hello'
#     success_url = reverse_lazy("create_done")   # 모든 처리가 다 끝나고 나서 어디로 이동할 것인가?

# class PostCreateDone(DetailView):
#     model = Post
#     template_name = 'blog/create_done.html'

# class PostCreateDone(ListView):
#     model = Post
#     template_name = 'blog/create_done.html'
#     context_object_name = 'createDone'      # 디폴트 컨텍스트 변수명 :  createDone

# class PostUpdate(UpdateView):
#     model = Post
#     fields = '__all__'                         # 필드 정해놓으면 글쓴이를 수정이 불가능하도록 만들 수 있다.
#     template_name = 'blog/update.html'      
#     success_url = reverse_lazy('posts')

# class PostDelete(DeleteView):
#     model = Post
#     template_name = 'blog/delete_done.html'
#     success_url = reverse_lazy('posts')         # 모든 처리가 다 끝나고 나서 어디로 이동할 것인가?



# 리스트의 함수형 뷰

def PostList(request):
    # Post 모델의 모든 데이터를 가지고 온다.
    post_list=Post.objects.all().order_by('updated')
    return render(request,'blog/index.html',{'list':post_list})

def PostDetail(request,pk):
    # Post 모델의 모든 데이터를 가지고 온다.
    post=get_object_or_404(Post,pk = pk)
    return render(request,'blog/detail.html',{'detail':post})
 
from .forms import PostForm

def PostCreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # mem = (
            #     # img = request.FILES("img")              # 이미지가 안되는데 어떻게 하면 되는지 알아보자!!
            #     title = request.POST['title']
            #     content = request.POST['content']
            # )
            return redirect('posts')
    else:
        form = PostForm()
    return render(request,'blog/create.html',{'form':form})
 
def PostUpdate(request, pk):
    post = get_object_or_404(Post,pk = pk)

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)         # 인스턴스를 포스트로 받는다.
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)                      # 기존에 썻던 내용을 받아야하기 때문에!
    return render(request,'blog/update.html',{'form':form})

def PostDelete(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts')