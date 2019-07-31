from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserFollowView,UserPostListView



urlpatterns=[
    path('register/',views.register,name='blog-register'),
    path('profile/',views.profile,name='profile'),
    path('home/<str:username>/follow',UserFollowView.as_view(),name='follow'),
    path('',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('<str:username>/',UserPostListView.as_view(),name='user-posts'),
    
    
    
]