[toc]

# [Django] CRUD 만들어보기

## 1. VSCODE에서 가상환경 설치 및 서버 실행해보기

```bash
$ python -m venv 'venv' #가상환경 생성

$ source venv/scripts/activate # 가상환경 실행

(myvenv) # 가상환경 켜짐
# 꺼짐은 deactivate

$ pip3 install django # django 설치, 필자는 2.1.5 버전을 좋아한다.
# 따라서 pip3의 django==2.1.5 버전을 설치하였음
# pip3 install django==2.1.5

$ django-admin startproject 'config' . # 프로젝트 생성
# 이때 manage.py가 위치한 프로젝트 안(BASE_DIR)으로 들어간다. 

$ python manage.py startapp 'blog' # app 생성

$ python manage.py runserver # http://127.0.0.1:8000/
# vscode에 있는 liveserver 등 extension들도 로컬 서버를 지원한다. 
```

## 2. settings.py 코딩

1. INSTALLED_APPS 설정

```python
INSTALLED_APPS = [
    ...
    'blog',
]
```

2. TEMPLATES 설정

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        # 템플릿 확장을 위한 경로 설정
        ...
    }
]
```

3. 언어 설정

```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

4. 정적 이미지 및 미디어 경로 설정

```python
# (필수) 정적 이미지, css, js 를 설정해야하므로 추가해야 함.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
) 

# (선택) 이미지나 동영상을 보관할 미디어 파일 경로를 설정하려면 추가할 것.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

- `config/urls.py`

```python
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static # <-- 추가
from django.conf import settings # <-- 추가 

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # <-- 추가
```

5. DB 구조 틀 생성

```bash
$ python manage.py migrate
```

![image](https://user-images.githubusercontent.com/26649731/76175819-a87d0680-61f1-11ea-9dd0-92f5f6bbff27.png)

- 전체 디렉토리 구조이다.

![image](https://user-images.githubusercontent.com/26649731/76175879-e9751b00-61f1-11ea-88ec-9210a480035c.png)

## 3. [M]odel 코딩

- CRUD를 위한 모델을 코딩해야 한다.

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # blank= 유효성과 관련되어 있다. (validation-related) form.is_valid()가 호출될 때 폼 유효성 검사에 사용된다.
    # null= DB와 관련되어 있다. (database-related) 주어진 데이터베이스 컬럼이 null 값을 가질 것인지 아닌지를 정의한다.
    img = models.ImageField(upload_to='media',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 관리자 페이지에서 보고싶은 것
    def __str__(self):
        return self.title +" " + self.content
```

```bash
$ python manage.py makemigrations blog
$ python manage.py migrate blog
```

- admin 페이지 설정

```bash
$ python manage.py createsuperuser
```

```python
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
```

![image](https://user-images.githubusercontent.com/26649731/76177589-14626d80-61f8-11ea-849e-82099b8574b9.png)

- self 에서 지정해준 대로 관리자 목록이 표시되는 것을 볼 수 있다.
- 조금 더 예쁘게 하기 위해서 관리자페이지를 커스터마이징해보자.

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','img','content']
    list_display_links=['id','title']

# admin.site.register(Post)
```

![image](https://user-images.githubusercontent.com/26649731/76177970-1bd64680-61f9-11ea-87d9-493d810ee40e.png)

- 좀더 자세한 커스터마이징은 [여기](https://wayhome25.github.io/django/2017/03/22/django-ep8-django-admin/)에서 적용해볼 수 있다.

- 적용 후의 관리자 페이지이다.

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','img','content']
    list_display_links=['id','title']
    list_filter = ['created','updated']
    list_editable = ['content']
    # list_per_page = 50
    # default : 100

# admin.site.register(Post)
```

![image](https://user-images.githubusercontent.com/26649731/76182129-08ca7300-6207-11ea-908b-227d2eca1ad6.png)

## 4. [V]iew 코딩

- 뷰 작성 -> url 작성으로 순서를 진행해본다.
- 뷰 작성은 generic 뷰를 사용할 것이다.~~클래스뷰 자료는 많이 없다.~~
  - 그래서 클래스 뷰로 코딩해보기로 했다!!

### 4.1 CBV(Class-Based View) 코딩

- create 이후에 details 로 가고싶은데 어떻게 해야할지 모르겠다. 이거 공부해보기!
- 지금은 create 이후 바로 리스트를 띄워준다. 아직 해결 못함..

- 클래스 뷰를 이용하기 위해서는 장고에서 클래스뷰를 어떻게 활용했는지 알아야 한다.

```python
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
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('posts')         # 모든 처리가 다 끝나고 나서 어디로 이동할 것인가?
```

```python
from django.urls import path,reverse_lazy
from .views import PostList,PostDetail,PostCreate,PostUpdate,PostDelete,PostCreateDone

urlpatterns = [
    path('',PostList.as_view(),name='posts'),
    path('<int:pk>/',PostDetail.as_view(),name='details'),
    path('create/',PostCreate.as_view(),name='create'),
    path('createDone/',PostCreateDone.as_view(),name='create_done'),
    path('update/<int:pk>/',PostUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',PostDelete.as_view(),name='delete'),
]

```

### 4.2 FBV(Function-Based View) 코딩



## 5. [T]emplates 코딩

- update, delete, create 같은 경우에는 form 문을 사용하였다.

- list, detail 같은 경우 `{}` `{%%}` 을 적절히 활용하여 데이터 표기를 진행하였다.

- Create

```html
<!-- blog/create.html -->

<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" class="btn btn-primary" value="제출">
</form>
```

```html
<!-- blog/create_done.html -->

<h1>글 등록 성공!</h1>
{{object.title}}
<a href="{% url 'posts' %}">목록으로</a>
```

- Read

```html
<!-- blog/detail.html -->

<div>제목 : {{detail.title}}</div><br>
내용 : {{detail.content}}

<a href="{% url 'update' detail.id %}">수정하기</a>
<a href="{% url 'delete' detail.id %}">삭제하기</a>
```

- update

```html
<!-- blog/update.html -->

<form action="" method="post">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value="Update" class="btn btn-info btn-sm">
</form>
```

- delete

```html
<!-- blog/delete.html -->

<form action="" method="post">
    {% csrf_token %}
    <div class="alert alert-danger">Do you want to delete Post  "{{object.title}}"?</div>
    <input type="submit" value="Delete" class="btn btn-danger">
</form>
```

