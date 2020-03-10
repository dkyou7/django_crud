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
