from django.urls import path
from .views import PostListView, PostDetailsView, PostCreateView, POstUpdateView, PostDeleteView, UserPostListView
from . import views
urlpatterns = [
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailsView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', POstUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('about/', views.about, name="blog-about"),
    path('a_light/', views.a_light, name="a-light"),
]