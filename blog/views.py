from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views import View
from .models import Post
from django.urls import reverse_lazy


# All Post List View
class BlogListView(LoginRequiredMixin,ListView):
	model=Post
	template_name='blog/home.html'
	context_object_name='posts'
	ordering=['-date_posted']
	paginate_by=5




	def get_context_data(self,*args,**kwargs):
		im_following = self.request.user.profile.get_following() 
		posts1=Post.objects.filter(author__in=im_following).order_by('-date_posted')
		posts2=Post.objects.filter(author=self.request.user).order_by('-date_posted')

		if posts1:
			posts=posts1 | posts2
		else:
			posts=posts2

		return {'posts': posts}




		
# Post detail
class BlogDetailView(LoginRequiredMixin,DetailView):
	model=Post



class BlogCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields = ['content','image','video']


	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields=['content','image','video']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True

		return False


class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post
	success_url='/home'

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False






def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})