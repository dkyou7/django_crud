from django.urls import path,reverse_lazy
from .views import PostList,PostDetail,PostCreate

urlpatterns = [
    path('',PostList.as_view(),name='posts'),
    path('<int:pk>/',PostDetail.as_view(),name='details'),
    path('create/',PostCreate.as_view(),name='create'),
]
