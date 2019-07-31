from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView,UserBlogListView
from . import views



urlpatterns=[
    path('',BlogListView.as_view(),name='blog-home'),
    path('<str:username>/',UserBlogListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='blog-detail'),
    path('post/<int:pk>/update/',BlogUpdateView.as_view(),name='blog-update'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='blog-delete'),
    path('new/',BlogCreateView.as_view(),name='blog-create'),
    path('about/',views.about,name='blog-about'),
    
]





