from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView, MessengerView,MessegeDeleteView
from . import views



urlpatterns=[
    path('',BlogListView.as_view(),name='blog-home'),
    
    path('post/<int:pk>/',BlogDetailView.as_view(),name='blog-detail'),
    path('post/<int:pk>/update/',BlogUpdateView.as_view(),name='blog-update'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='blog-delete'),
    path('new/',BlogCreateView.as_view(),name='blog-create'),
    path('about/',views.about,name='blog-about'),
    path('search/',views.search,name='Search'),
    path('messege/<str:user>/',MessengerView.as_view(),name='messege'),
    path('messege/<int:pk>/delete/',MessegeDeleteView.as_view(),name='messege-delete'),
    
]





