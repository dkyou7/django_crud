from django.urls import path #, reverse_lazy
# from .views import PostList,PostDetail,PostCreate,PostUpdate,PostDelete,PostCreateDone
from . import views

urlpatterns = [
    # path('',PostList.as_view(),name='posts'),
    # path('<int:pk>/',PostDetail.as_view(),name='details'),
    # path('create/',PostCreate.as_view(),name='create'),
    # path('createDone/',PostCreateDone.as_view(),name='create_done'),
    # path('update/<int:pk>/',PostUpdate.as_view(),name='update'),
    # path('delete/<int:pk>/',PostDelete.as_view(),name='delete'),

    path('',views.PostList,name="posts"),
    path('<int:pk>/',views.PostDetail,name='details'),
    path('create/',views.PostCreate,name='create'),
    path('update/<int:pk>/',views.PostUpdate,name='update'),
    path('delete/<int:pk>/',views.PostDelete,name='delete'),
]
