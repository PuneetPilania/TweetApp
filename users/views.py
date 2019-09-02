from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,ListView
from django.contrib.auth import get_user_model
from .models import Profile
from blog.models import Post
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

User=get_user_model()

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created ! You are now able to login.')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


# Two queryset 
class UserPostListView(LoginRequiredMixin,ListView):
    template_name='blog/user_posts.html'
    paginate_by=5
    

    def get_queryset(self):
        return User.objects.all()

    
    def get_context_data(self,*args,**kwargs):
        # Call clicked username

        users=get_object_or_404(User,username__iexact=self.kwargs.get("username"))
        context=super(UserPostListView, self).get_context_data(*args,**kwargs)
        context['users']=users
        context['posts']=Post.objects.filter(author=users).order_by('-date_posted')
        context['following']=Profile.objects.is_following(self.request.user, users)
        context['auth_user']=self.request.user
        return context



class UserFollowView(LoginRequiredMixin,View):
    def get(self,request,username,*args,**kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated:
            is_following = Profile.objects.toggle_follow(request.user, toggle_user)
        return redirect("user-posts",username=username)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')


    else:
        u_form = UserUpdateForm( instance=request.user)
        p_form = ProfileUpdateForm( instance=request.user.profile)
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'users/profile.html',context)






