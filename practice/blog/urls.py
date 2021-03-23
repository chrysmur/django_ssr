from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'), # django expexts pk
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('about', views.about, name='blog-about')
]