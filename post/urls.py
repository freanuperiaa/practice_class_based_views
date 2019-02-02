from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('posts/', views.PostListView.as_view(), name='post'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('addpost/', views.PostCreateView.as_view(), name='addpost'),
    path('posts/<int:pk>/edit_post/', views.PostUpdateView.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
]