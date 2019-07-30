from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserDetailView


urlpatterns=[
    path('register/',views.register,name='blog-register'),
    path('profile/',views.profile,name='profile'),
    
    path('',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('<str:username>/',UserDetailView.as_view(),name='detail'),
    
    
]